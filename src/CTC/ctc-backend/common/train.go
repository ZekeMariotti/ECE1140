package common

type Train struct {
	ID       int           `json:"id"`
	Line     string        `json:"line"`
	Driver   string        `json:"driver"`
	Location TrainLocation `json:"location"`
	Stops    []TrainStop   `json:"stops"`
}
