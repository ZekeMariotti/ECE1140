package common

import "sync"

type Switch struct {
	ID                    int       `json:"id"`
	Source                int       `json:"source"`
	Destination1          int       `json:"destination1"`
	Destination1Enterable bool      `json:"destination1-enterable"`
	Destination2          int       `json:"destination2"`
	Destination2Enterable bool      `json:"destination2-enterable"`
	Side                  BlockSide `json:"blockside"`
	currentDest           int
	mute                  sync.Mutex
}

func (s *Switch) SetPosition(destination int) bool {
	s.mute.Lock()
	defer s.mute.Unlock()

	if destination == s.Destination1 || destination == s.Destination2 {
		s.currentDest = destination
		return true
	} else {
		return false
	}
}

func (s *Switch) GetDestination() int {
	return s.currentDest
}

func (s *Switch) GetNextBlocks(block int) []int {
	if block == s.Source {
		result := make([]int, 0)
		if s.Destination1Enterable {
			result = append(result, s.Destination1)
		}
		if s.Destination2Enterable {
			result = append(result, s.Destination2)
		}
		return result
	}
	if block == s.Destination1 || block == s.Destination2 {
		return []int{s.Source}
	}
	return []int{-1}
}

func (s *Switch) UpdateDestinationFromWayside(wayside bool) {
	if wayside {
		s.currentDest = s.Destination2
	} else {
		s.currentDest = s.Destination1
	}
}
