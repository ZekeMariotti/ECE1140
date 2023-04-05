package common

import "sync"

type Switch struct {
	Source       int       `json:"source"`
	Destination1 int       `json:"destination1"`
	Destination2 int       `json:"destination2"`
	Side         BlockSide `json:"blockside"`
	currentDest  int
	mute         sync.Mutex
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

func (s *Switch) GetNextBlocks(block int) []int {
	if block == s.Source {
		return []int{s.Destination1, s.Destination2}
	}
	if block == s.Destination1 || block == s.Destination2 {
		return []int{s.Source}
	}
	return []int{-1}
}
