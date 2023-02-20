package datastore

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
)

type DataStore struct {
	Blocks     []common.Block     `json:"blocks"`
	Lines      []common.Line      `json:"lines"`
	Stations   []common.Station   `json:"stations"`
	Trains     []common.Train     `json:"trains"`
	TimeKeeper *common.TimeKeeper `json:"timekeeper"`
}

func NewDataStore() *DataStore {
	ds := DataStore{}
	return &ds
}
