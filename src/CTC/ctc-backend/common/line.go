package common

type Line struct {
	Name   string    `json:"name"`
	Blocks []BlockID `json:"blocks"`
}
