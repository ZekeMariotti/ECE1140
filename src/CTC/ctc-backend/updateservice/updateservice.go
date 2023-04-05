package updateservice

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/route"
	"github.com/shopspring/decimal"
)

type UpdateService struct {
	data     *datastore.DataStore
	routeGen *route.RouteCalculator
	stop     chan bool
}

// New update service
func NewUpdateService(data *datastore.DataStore) *UpdateService {
	service := UpdateService{
		data:     data,
		routeGen: route.NewRouteCalculator(data),
		stop:     make(chan bool),
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
	// Check if auto mode
	if s.data.AutoMode {
		// In auto mode
		// Get all ideal routes for trains
		trainRouteMap := make(map[int][]int)
		blockUseMap := make(map[int][]int)
		for _, v := range s.data.Trains.GetSlice() {
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
	for train, route := range routeMap {
		// Check each block in route to see if another train wants it
		for i := range route {
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
	for train, route := range routeMap {
		line := s.data.Trains.Get(train).Line
		for i := range route {
			// Calculate suggested speed
			blocks := route[i:]
			distance := s.getDistanceToRouteEnd(line, blocks)
			speed := s.getMaxSpeedFromDistance(distance)
			// Set suggested speed
			s.data.Lines.SetBlockSpeed(line, route[i], speed)
		}

	}
}

func (s *UpdateService) getDistanceToRouteEnd(line string, route []int) decimal.Decimal {
	distance := decimal.Zero
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
