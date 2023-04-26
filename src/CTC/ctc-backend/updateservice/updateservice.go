package updateservice

import (
	"time"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/route"
	"github.com/shopspring/decimal"
)

type UpdateService struct {
	data              *datastore.DataStore
	routeGen          *route.RouteCalculator
	stop              chan bool
	lastTrainBlockMap map[string]map[int]int
	lastHoldMap       map[int]int
}

// New update service
func NewUpdateService(data *datastore.DataStore) *UpdateService {
	service := UpdateService{
		data:              data,
		routeGen:          route.NewRouteCalculator(data),
		stop:              make(chan bool),
		lastTrainBlockMap: make(map[string]map[int]int),
		lastHoldMap:       make(map[int]int),
	}

	return &service
}

// Starts running the update service
func (s *UpdateService) Start() {
	go s.updateLoop()
}

// Stop running the update service
func (s *UpdateService) Stop() {
	s.stop <- true
}

func (s *UpdateService) updateLoop() {
	for {
		select {
		case <-s.stop:
			return
		default:
			s.doUpdate()
		}
	}
}

func (s *UpdateService) doUpdate() {
	// Update train locations
	s.updateTrainAssignments()
	// Check if auto mode
	if s.data.AutoMode {
		// In auto mode
		trainRouteMap := make(map[int][]int) // map[trainID]routeInBlockIDs
		blockUseMap := make(map[int][]int)   // map[blockID]assignedTrainIDs
		stationHoldsMap := make(map[int]int) // map[trainID]blockOfCurrentStation
		holdBlocks := make(map[int]bool)     // map[blockID]hold?
		trains := s.data.Trains.GetSlice()
		// Update stops for each train
		for i := range trains {
			if len(trains[i].Stops) > 0 && len(trains[i].Location.Blocks) > 0 {
				location := trains[i].Location.Blocks[len(trains[i].Location.Blocks)-1]
				if location == trains[i].Stops[0].Station.BlockID {
					// At station
					// Assign block to be held
					stationHoldsMap[trains[i].ID] = trains[i].Stops[0].Station.BlockID
					holdBlocks[trains[i].Stops[0].Station.BlockID] = true

					// Remove stop
					train := s.data.Trains.Get(trains[i].ID)
					train.Stops = train.Stops[1:]
					s.data.Trains.Set(train.ID, train)
				}
			}
			if len(trains[i].Stops) == 0 {
				// Return to yard
				train := s.data.Trains.Get(trains[i].ID)
				train.Stops = append(train.Stops, common.TrainStop{
					Station: common.Station{
						Name:    "YARD",
						Side:    common.STATIONSIDE_BOTH,
						BlockID: 0,
					},
					Time: s.data.TimeKeeper.GetSimulationTime(),
				})
				s.data.Trains.Set(trains[i].ID, train)
			}
		}

		// Get all ideal routes for trains
		for _, v := range trains {
			if len(v.Stops) > 0 {
				// Get route
				destinationBlock := s.data.Lines.Get(v.Line).Blocks.Get(v.Stops[0].Station.BlockID)
				route := s.routeGen.CalculateRoute(v, destinationBlock)
				trainRouteMap[v.ID] = route
				for i := range route {
					use := blockUseMap[route[i]]
					use = append(use, v.ID)
					blockUseMap[route[i]] = use
				}
			}
		}
		// Check prior holds
		for trainid, blockid := range s.lastHoldMap {
			train := s.data.Trains.Get(trainid)
			if len(train.Stops) > 0 {
				dur := s.getTimeToDestination(train.Line, trainRouteMap[trainid])
				if train.Stops[0].Time.Sub(s.data.TimeKeeper.GetSimulationTime()) > dur {
					stationHoldsMap[trainid] = blockid
					holdBlocks[blockid] = true
				}
			}
		}
		s.lastHoldMap = stationHoldsMap

		// Update authorities
		s.updateAuthorities(trainRouteMap, blockUseMap, holdBlocks)
		// Update suggested speeds
		s.updateSpeeds(trainRouteMap, holdBlocks)
	}
}

// The function that follows below has come straight from the depths of hell.
// Before continuing, understand that there is no turning back. Continuing to read this
// may cause incurable mental insanity. You have been warned.
func (s *UpdateService) updateAuthorities(routeMap map[int][]int, useMap map[int][]int, holdsMap map[int]bool) {
	// Reset all authorities
	lines := s.data.Lines.GetSlice()
	for i := range lines {
		line := lines[i].Name
		blocks := s.data.Lines.Get(line).Blocks.GetSlice()
		for j := range blocks {
			s.data.Lines.SetBlockAuthority(line, blocks[j].Number, 0)
		}
	}
	// Set new authorities
	for train := range routeMap {
		route := routeMap[train]
		// Check each block in route to see if another train wants it
		for i := 0; i < len(route); i++ {
			usedTrains := useMap[route[i]]
			hasAuthority := true
			if len(usedTrains) > 1 {
				// Used by at least 1 other train, find out if this train has priority
				for j := range usedTrains {
					otherRoute := routeMap[usedTrains[j]]
					for k := range otherRoute {
						if otherRoute[k] == route[i] {
							if k < i {
								hasAuthority = false
							} else if k == i {
								// Trains are in a stalemate. Select lowest train ID
								if usedTrains[j] < train {
									hasAuthority = false
								}
							}
						}
					}
				}
			}
			if !hasAuthority {
				// Set new stop for the route
				routeMap[train] = route[:i-1]
				route = routeMap[train]
			}
		}
		// Generate authorities
		line := s.data.Trains.Get(train).Line
		for i := range route {
			authority := len(route) - i - 1
			if holdsMap[route[i]] == true {
				authority = 0
			}
			s.data.Lines.SetBlockAuthority(line, route[i], authority)
		}
	}
}

func (s *UpdateService) updateSpeeds(routeMap map[int][]int, holdsMap map[int]bool) {
	// Clear all speeds
	lines := s.data.Lines.GetSlice()
	for i := range lines {
		line := lines[i].Name
		blocks := s.data.Lines.Get(line).Blocks.GetSlice()
		for j := range blocks {
			speed := blocks[j].SpeedLimit
			if holdsMap[blocks[j].Number] == true {
				speed = decimal.Zero
			}
			s.data.Lines.SetBlockSpeed(line, blocks[j].Number, speed)
		}
	}
}

/*
	func (s *UpdateService) getDistanceToRouteEnd(line string, route []int) decimal.Decimal {
		distance := decimal.NewFromInt(0)
		lineData := s.data.Lines.Get(line)
		for i := range route {
			distance.Add(lineData.Blocks.Get(route[i]).Length)
		}
		return distance
	}

	func (s *UpdateService) getMaxSpeedFromDistance(distance decimal.Decimal) decimal.Decimal {
		acceleration, _ := decimal.NewFromString(MAX_TRAIN_DESCELERATION_STR)
		speed := acceleration.Mul(decimal.NewFromInt(2))
		speed = speed.Mul(distance)
		half, _ := decimal.NewFromString("0.5")
		speed = speed.Pow(half)
		return speed
	}
*/
func (s *UpdateService) updateTrainAssignments() {
	newMap := make(map[string]map[int]int)
	lines := s.data.Lines.GetLineNames()
	for _, line := range lines {
		newMap[line] = make(map[int]int)
		blocks := s.data.Lines.Get(line).Blocks.GetSlice()
		for _, block := range blocks {
			lastTrain := s.lastTrainBlockMap[line][block.Number]
			if block.Occupied && lastTrain == -1 {
				// Train just entered block
				if line == "Red" && block.Number == 9 {
					trains := s.data.Trains.GetFrontendSlice()
					if len(trains) > 0 && trains[len(trains)-1].Line == "Red" {
						newMap[line][block.Number] = trains[len(trains)-1].ID
						continue
					}
				} else if line == "Green" && block.Number == 63 {
					trains := s.data.Trains.GetFrontendSlice()
					if len(trains) > 0 && trains[len(trains)-1].Line == "Green" {
						newMap[line][block.Number] = trains[len(trains)-1].ID
						continue
					}
				}
				isSwitch, swt := s.routeGen.IsSwitchBlock(block.Number, s.data.Lines.Get(line))
				if isSwitch {
					switch swt.Side {
					case common.BLOCKSIDE_ASCEND:
						switch block.Number {
						case swt.Source:
							if s.lastTrainBlockMap[line][swt.Source-1] > 0 {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Source-1]
							} else {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.GetDestination()]
							}
						case swt.Destination1:
							if s.lastTrainBlockMap[line][swt.Source] > 0 {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Source]
							} else {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Destination1+1]
							}
						case swt.Destination2:
							if s.lastTrainBlockMap[line][swt.Source] > 0 {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Source]
							} else {
								switch block.Direction {
								case common.BLOCKDIRECTION_ASCENDING:
									newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Destination2-1]
								case common.BLOCKDIRECTION_BIDIRECTIONAL:
									newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Destination2+1]
								case common.BLOCKDIRECTION_DESCENDING:
									newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Destination2+1]
								}
							}
						}
					case common.BLOCKSIDE_DESCEND:
						switch block.Number {
						case swt.Source:
							if s.lastTrainBlockMap[line][swt.Source+1] > 0 {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Source+1]
							} else {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.GetDestination()]
							}
						case swt.Destination1:
							if s.lastTrainBlockMap[line][swt.Source] > 0 {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Source]
							} else {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Destination1-1]
							}
						case swt.Destination2:
							if s.lastTrainBlockMap[line][swt.Source] > 0 {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Source]
							} else {
								switch block.Direction {
								case common.BLOCKDIRECTION_ASCENDING:
									newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Destination2+1]
								case common.BLOCKDIRECTION_BIDIRECTIONAL:
									newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Destination2-1]
								case common.BLOCKDIRECTION_DESCENDING:
									newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Destination2-1]
								}
							}
						}
					}
				} else {
					if block.Direction == common.BLOCKDIRECTION_ASCENDING {
						if block.Number == 0 {
							// Is starting block
							newMap[line][block.Number] = s.data.Trains.Get(s.data.GetNextTrainID() - 1).ID
						} else {
							newMap[line][block.Number] = s.lastTrainBlockMap[line][block.Number-1]
						}
					} else if block.Direction == common.BLOCKDIRECTION_BIDIRECTIONAL {
						if block.Number == 0 {
							// Is starting block
							newMap[line][block.Number] = s.data.Trains.Get(s.data.GetNextTrainID() - 1).ID
						} else {
							if s.lastTrainBlockMap[line][block.Number-1] != -1 {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][block.Number-1]
							} else if s.lastTrainBlockMap[line][block.Number+1] != -1 {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][block.Number+1]
							} else {
								// No trains on adacent blocks, something went wrong!
								newMap[line][block.Number] = s.lastTrainBlockMap[line][block.Number]
							}
						}
					} else if block.Direction == common.BLOCKDIRECTION_DESCENDING {
						if block.Number == 0 {
							// Is starting block
							newMap[line][block.Number] = s.data.Trains.Get(s.data.GetNextTrainID() - 1).ID
						} else {
							newMap[line][block.Number] = s.lastTrainBlockMap[line][block.Number+1]
						}
					}
				}
			} else if !block.Occupied && lastTrain != -1 {
				// Train just left block
				newMap[line][block.Number] = -1
			} else {
				// No change occured
				newMap[line][block.Number] = lastTrain
			}
		}
	}
	/* // Code for debugging this function
	printMap := make(map[string]map[int]int)
	for line, blocks := range newMap {
		printMap[line] = make(map[int]int)
		for id, train := range blocks {
			if train != -1 {
				printMap[line][id] = train
			}
		}
	}
	for line, blocks := range printMap {
		if len(blocks) > 0 {
			fmt.Print(line)
			for id, train := range blocks {
				fmt.Print("[", id, ":", train, "] ")
			}
			fmt.Println()
		}
	} */

	// Update values and cache result
	s.data.Trains.ResetTrainLocations()
	for _, blocks := range newMap {
		for blockID, trainID := range blocks {
			if trainID > 0 {
				s.data.Trains.AddTrainLocationBlock(trainID, blockID)
			}
		}
	}
	s.lastTrainBlockMap = newMap
}

func (s *UpdateService) getTimeToDestination(line string, route []int) time.Duration {
	durationSum, _ := time.ParseDuration("0s")
	for i := range route {
		block := s.data.Lines.Get(line).Blocks.Get(route[i])
		dt := block.Length.Div(block.SpeedLimit)
		str := dt.String() + "s"
		dur, _ := time.ParseDuration(str)
		durationSum += dur
	}
	return durationSum
}
