package datastore

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
)

type DataStore struct {
	Lines      common.SafeLineMap  `json:"lines"`
	Trains     common.SafeTrainMap `json:"trains"`
	TimeKeeper *common.TimeKeeper  `json:"timekeeper"`
}

func NewDataStore() *DataStore {
	ds := DataStore{
		Lines:  *common.NewSafeLineMap(),
		Trains: *common.NewSafeTrainMap(),
	}
	return &ds
}
