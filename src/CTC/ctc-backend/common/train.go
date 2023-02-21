package common

type Train struct {
	ID       int32       `json:"id"`
	Line     string      `json:"line"`
	Driver   string      `json:"driver"`
	Location []*Block    `json:"location"`
	Stops    []TrainStop `json:"stops"`
}
