package common

import "sync"

type Switch struct {
	Source       int `json:"source"`
	Destination1 int `json:"destination1"`
	Destination2 int `json:"destination2"`
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
