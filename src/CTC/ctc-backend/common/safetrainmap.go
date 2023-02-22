package common

import (
	"sync"

	"golang.org/x/exp/maps"
)

// Implements a go-routine safe map for storing trains
type SafeTrainMap struct {
	data map[string]Train
	mute sync.Mutex
}

func NewSafeTrainMap() *SafeTrainMap {
	m := SafeTrainMap{
		data: make(map[string]Train),
		mute: sync.Mutex{},
	}
	return &m
}

func (m *SafeTrainMap) Get(key string) Train {
	m.mute.Lock()
	defer m.mute.Unlock()

	return m.data[key]
}

func (m *SafeTrainMap) Set(key string, value Train) {
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

func (m *SafeTrainMap) GetSlice() []Train {
	m.mute.Lock()
	defer m.mute.Unlock()

	return maps.Values(m.data)
}
