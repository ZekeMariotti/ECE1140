package common

type Switch struct {
	Source       BlockID   `json:"source"`
	Destinations []BlockID `json:"destinations"`
}
