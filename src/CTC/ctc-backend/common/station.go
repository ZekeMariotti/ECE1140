package common

type Station struct {
	Name    string      `json:"name"`
	Side    StationSide `json:"side"`
	BlockID int         `json:"blockid"`
}
