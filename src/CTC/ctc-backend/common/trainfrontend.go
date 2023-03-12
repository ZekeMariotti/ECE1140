package common

type TrainFrontend struct {
	ID       int                 `json:"id"`
	Line     string              `json:"line"`
	Driver   string              `json:"driver"`
	Location TrainLocation       `json:"location"`
	Stops    []TrainStopFrontend `json:"stops"`
}
