package datastore

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
)

type DataStore struct {
	Lines      []*common.Line     `json:"lines"`
	Trains     []*common.Train    `json:"trains"`
	TimeKeeper *common.TimeKeeper `json:"timekeeper"`
}

func NewDataStore() *DataStore {
	ds := DataStore{
		Lines:  make([]*common.Line, 0),
		Trains: make([]*common.Train, 0),
	}
	return &ds
}
