package common

type Line struct {
	Name     string     `json:"name"`
	Blocks   []*Block   `json:"blocks"`
	Switches []*Switch  `json:"switches"`
	Stations []*Station `json:"stations"`
}
