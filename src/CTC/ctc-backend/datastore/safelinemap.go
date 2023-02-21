package datastore

import (
	"sync"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"golang.org/x/exp/maps"
)

// Implements a go-routine safe map for storing train lines
type SafeLineMap struct {
	data map[string]common.Line
	mute sync.Mutex
}

func NewSafeLineMap() *SafeLineMap {
	m := SafeLineMap{
		data: make(map[string]common.Line),
		mute: sync.Mutex{},
	}
	return &m
}

func (m *SafeLineMap) Get(key string) common.Line {
	m.mute.Lock()
	defer m.mute.Unlock()

	return m.data[key]
}

func (m *SafeLineMap) Set(key string, value common.Line) {
	m.mute.Lock()
	defer m.mute.Unlock()

	m.data[key] = value
}

func (m *SafeLineMap) HasKey(key string) bool {
	m.mute.Lock()
	defer m.mute.Unlock()

	_, ok := m.data[key]
	return ok
}

func (m *SafeLineMap) GetSlice() []common.Line {
	m.mute.Lock()
	defer m.mute.Unlock()

	return maps.Values(m.data)
}
