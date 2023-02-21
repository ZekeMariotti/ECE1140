package datastore

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
)

type DataStore struct {
	Lines      SafeLineMap        `json:"lines"`
	Trains     SafeTrainMap       `json:"trains"`
	TimeKeeper *common.TimeKeeper `json:"timekeeper"`
}

func NewDataStore() *DataStore {
	ds := DataStore{
		Lines:  *NewSafeLineMap(),
		Trains: *NewSafeTrainMap(),
	}
	return &ds
}
