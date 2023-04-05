package common

type TrainStopFrontend struct {
	Station string   `json:"station"`
	Time    StopTime `json:"time"`
}

func TrainStopsToFrontend(stops []TrainStop) []TrainStopFrontend {
	result := make([]TrainStopFrontend, len(stops))
	for i, v := range stops {
		result[i] = TrainStopFrontend{
			Station: v.Station.Name,
			Time:    StopTime{v.Time},
		}
	}
	return result
}
