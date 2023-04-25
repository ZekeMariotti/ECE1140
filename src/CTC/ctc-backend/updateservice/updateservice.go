package updateservice

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/route"
)

type UpdateService struct {
	data              *datastore.DataStore
	routeGen          *route.RouteCalculator
	stop              chan bool
	lastTrainBlockMap map[string]map[int]int
}

// New update service
func NewUpdateService(data *datastore.DataStore) *UpdateService {
	service := UpdateService{
		data:              data,
		routeGen:          route.NewRouteCalculator(data),
		stop:              make(chan bool),
		lastTrainBlockMap: make(map[string]map[int]int),
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
		// Get all ideal routes for trains
		trainRouteMap := make(map[int][]int)
		blockUseMap := make(map[int][]int)
		trains := s.data.Trains.GetSlice()
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
		// Update authorities
		s.updateAuthorities(trainRouteMap, blockUseMap)
		// Update suggested speeds
		s.updateSpeeds(trainRouteMap)
	}
}

// The function that follows below has come straight from the depths of hell.
// Before continuing, understand that there is no turning back. Continuing to read this
// may cause incurable mental insanity. You have been warned.
func (s *UpdateService) updateAuthorities(routeMap map[int][]int, useMap map[int][]int) {
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
			s.data.Lines.SetBlockAuthority(line, route[i], authority)
		}
	}
}

func (s *UpdateService) updateSpeeds(routeMap map[int][]int) {
	// Clear all speeds
	lines := s.data.Lines.GetSlice()
	for i := range lines {
		line := lines[i].Name
		blocks := s.data.Lines.Get(line).Blocks.GetSlice()
		for j := range blocks {
			s.data.Lines.SetBlockSpeed(line, blocks[j].Number, blocks[j].SpeedLimit)
		}
	}
	// Add new speeds

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
					isSource := swt.Source == block.Number
					if block.Direction == common.BLOCKDIRECTION_ASCENDING {
						switch swt.Side {
						case common.BLOCKSIDE_ASCEND:
							if isSource {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][block.Number-1]
							} else {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Source]
							}
						case common.BLOCKSIDE_DESCEND:
							if isSource {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Source+1]
							} else {
								if s.lastTrainBlockMap[line][swt.Destination1] != -1 {
									newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Destination1]
								} else {
									newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Destination2]
								}
							}
						}
					} else if block.Direction == common.BLOCKDIRECTION_BIDIRECTIONAL {
						switch swt.Side {
						case common.BLOCKSIDE_ASCEND:
							if isSource {
								if s.lastTrainBlockMap[line][swt.GetDestination()] != -1 {
									newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.GetDestination()]
								} else if s.lastTrainBlockMap[line][block.Number-1] != -1 {
									newMap[line][block.Number] = s.lastTrainBlockMap[line][block.Number-1]
								}
							} else {
								if s.lastTrainBlockMap[line][block.Number+1] != -1 {
									newMap[line][block.Number] = s.lastTrainBlockMap[line][block.Number+1]
								} else {
									newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Source]
								}
							}
						case common.BLOCKSIDE_DESCEND:
							if isSource {
								if s.lastTrainBlockMap[line][swt.GetDestination()] != -1 {
									newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.GetDestination()]
								} else if s.lastTrainBlockMap[line][block.Number+1] != -1 {
									newMap[line][block.Number] = s.lastTrainBlockMap[line][block.Number+1]
								}
							} else {
								if s.lastTrainBlockMap[line][block.Number-1] != -1 {
									newMap[line][block.Number] = s.lastTrainBlockMap[line][block.Number-1]
								} else {
									newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.Source]
								}
							}
						}
					} else if block.Direction == common.BLOCKDIRECTION_DESCENDING {
						switch swt.Side {
						case common.BLOCKSIDE_ASCEND:
							if isSource {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.GetDestination()]
							} else {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][block.Number+1]
							}
						case common.BLOCKSIDE_DESCEND:
							if isSource {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][block.Number+1]
							} else {
								newMap[line][block.Number] = s.lastTrainBlockMap[line][swt.GetDestination()]
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
