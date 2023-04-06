package datastore

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
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
		ID:       frontend.ID,
		Line:     frontend.Line,
		Driver:   frontend.Driver,
		Location: frontend.Location,
		Stops:    make([]common.TrainStop, len(frontend.Stops)),
	}

	line := d.Lines.Get(frontend.Line)

	for i, v := range frontend.Stops {
		result.Stops[i] = common.TrainStop{
			Station: line.GetStationByName(v.Station),
			Time:    v.Time.Time,
		}
	}

	return result
}
