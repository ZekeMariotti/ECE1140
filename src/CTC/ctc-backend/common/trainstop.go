package common

import "time"

type TrainStop struct {
	Station Station   `json:"station"`
	Time    time.Time `json:"time"`
}
