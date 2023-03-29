package common

type LineOutput struct {
	Name   string        `json:"name"`
	Blocks []BlockOutput `json:"blocks"`
}
