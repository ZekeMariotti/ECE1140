package wayside

type WaysideToCTC struct {
	Switches   map[string]bool `json:"Switches"`
	Lights     map[string]bool `json:"Lights"`
	Occupancy  map[string]bool `json:"Occupancy"`
	BrokenRail map[string]bool `json:"BrokenRail"`
	Gates      map[string]bool `json:"Gates"`
}
