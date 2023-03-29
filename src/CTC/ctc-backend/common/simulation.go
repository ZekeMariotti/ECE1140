package common

import "time"

type Simulation struct {
	Speed int       `json:"speed"`
	Time  time.Time `json:"time"`
}
