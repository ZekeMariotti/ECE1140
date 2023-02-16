package common

import "time"

type Train struct {
	ID     int32       `json:"id"`
	Line   string      `json:"line"`
	Driver string      `json:"driver"`
	Stops  []TrainStop `json:"stops"`
}

type TrainStop struct {
	Station string    `json:"station"`
	Time    time.Time `json:"time"`
}
