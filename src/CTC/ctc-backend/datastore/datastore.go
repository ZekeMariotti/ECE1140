package datastore

import (
	"sort"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/shopspring/decimal"
)

type DataStore struct {
	Lines      common.SafeLineMap  `json:"lines"`
	Trains     common.SafeTrainMap `json:"trains"`
	TimeKeeper *common.TimeKeeper  `json:"timekeeper"`
	AutoMode   bool                `json:"auto"`
}

func NewDataStore() *DataStore {
	ds := DataStore{
		Lines:    *common.NewSafeLineMap(),
		Trains:   *common.NewSafeTrainMap(),
		AutoMode: true,
	}
	return &ds
}

func (d *DataStore) GetNextTrainID() int {
	trains := d.Trains.GetSlice()
	// Get next train ID
	currentLast := 0
	for _, v := range trains {
		if v.ID > currentLast {
			currentLast = v.ID
		}
	}
	return currentLast + 1
}

func (d *DataStore) TrainFrontendToBackend(frontend common.TrainFrontend) common.Train {
	result := common.Train{
		ID:            frontend.ID,
		Line:          frontend.Line,
		Driver:        frontend.Driver,
		Location:      frontend.Location,
		Stops:         make([]common.TrainStop, len(frontend.Stops)),
		ReadyDispatch: false,
	}

	line := d.Lines.Get(frontend.Line)
	stops := frontend.Stops

	sort.Slice(stops, func(i, j int) bool {
		return stops[i].Time.Time.Before(stops[j].Time.Time)
	})

	for i, v := range frontend.Stops {
		result.Stops[i] = common.TrainStop{
			Station: line.GetStationByName(v.Station),
			Time:    v.Time.Time,
		}
	}

	// Append station for last before yard
	switch frontend.Line {
	case "Green":
		result.Stops = append(result.Stops, common.TrainStop{
			Station: line.GetStationByName("OVERBROOK"),
			Time:    d.TimeKeeper.GetSimulationTime(),
		})
	case "Red":
		result.Stops = append(result.Stops, common.TrainStop{
			Station: line.GetStationByName("HERRON AVE"),
			Time:    d.TimeKeeper.GetSimulationTime(),
		})
	}

	return result
}

func (d *DataStore) GetThroughput(line string) decimal.Decimal {
	passengers := decimal.NewFromInt32(int32(d.Lines.GetPassengers(line)))
	hours := decimal.NewFromFloat(d.TimeKeeper.GetElapsedTime().Hours())
	throughput := passengers.Div(hours)
	return throughput
}
