package common

type Line struct {
	Name     string        `json:"name"`
	Blocks   *SafeBlockMap `json:"blocks"`
	Switches []*Switch     `json:"switches"`
	Stations []*Station    `json:"stations"`
}
