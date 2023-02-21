package wayside

type WaysideSwitch struct {
	Source              int `json:"source"`
	ActiveDestination   int `json:"active-destination"`
	InactiveDestination int `json:"inactive-destination"`
}
