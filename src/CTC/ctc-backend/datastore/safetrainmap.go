package datastore

import (
	"sync"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"golang.org/x/exp/maps"
)

// Implements a go-routine safe map for storing trains
type SafeTrainMap struct {
	data map[string]common.Train
	mute sync.Mutex
}

func NewSafeTrainMap() *SafeTrainMap {
	m := SafeTrainMap{
		data: make(map[string]common.Train),
		mute: sync.Mutex{},
	}
	return &m
}

func (m *SafeTrainMap) Get(key string) common.Train {
	m.mute.Lock()
	defer m.mute.Unlock()

	return m.data[key]
}

func (m *SafeTrainMap) Set(key string, value common.Train) {
	m.mute.Lock()
	defer m.mute.Unlock()

	m.data[key] = value
}

func (m *SafeTrainMap) HasKey(key string) bool {
	m.mute.Lock()
	defer m.mute.Unlock()

	_, ok := m.data[key]
	return ok
}

func (m *SafeTrainMap) GetSlice() []common.Train {
	m.mute.Lock()
	defer m.mute.Unlock()

	return maps.Values(m.data)
}
