package common

import (
	"sync"

	"golang.org/x/exp/maps"
)

// Implements a go-routine safe map for storing train lines
type SafeLineMap struct {
	data map[string]Line
	mute sync.Mutex
}

func NewSafeLineMap() *SafeLineMap {
	m := SafeLineMap{
		data: make(map[string]Line),
		mute: sync.Mutex{},
	}
	return &m
}

func (m *SafeLineMap) Get(key string) Line {
	m.mute.Lock()
	defer m.mute.Unlock()

	return m.data[key]
}

func (m *SafeLineMap) Set(key string, value Line) {
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

func (m *SafeLineMap) GetSlice() []Line {
	m.mute.Lock()
	defer m.mute.Unlock()

	return maps.Values(m.data)
}

func (m *SafeLineMap) SetBlockInfo(line string, blockInfo []BlockInfo) {
	m.mute.Lock()
	defer m.mute.Unlock()

	l := m.data[line]
	l.SetBlockInfos(blockInfo)
	m.data[line] = l
}

func (m *SafeLineMap) SetSwitchPositions(line string, positions []SwitchInfo) {
	m.mute.Lock()
	defer m.mute.Unlock()

	l := m.data[line]
	l.SetSwitchPositions(positions)
	m.data[line] = l
}

func (m *SafeLineMap) GetOutputs(line string) []BlockOutput {
	m.mute.Lock()
	defer m.mute.Unlock()

	l := m.data[line]
	return l.GetBlockOutputs()
}

func (m *SafeLineMap) GetOutput() []LineOutput {
	m.mute.Lock()
	defer m.mute.Unlock()

	out := make([]LineOutput, 0)

	for _, val := range m.data {
		out = append(out, val.GetLineOutput())
	}

	return out
}

func (m *SafeLineMap) GetLineNames() []string {
	m.mute.Lock()
	defer m.mute.Unlock()

	return maps.Keys(m.data)
}

func (m *SafeLineMap) GetStations(line string) []string {
	m.mute.Lock()
	defer m.mute.Unlock()

	l := m.data[line]
	return l.GetStations()
}

func (m *SafeLineMap) GetBlocks(line string) []BlockFrontend {
	m.mute.Lock()
	defer m.mute.Unlock()

	l := m.data[line]
	return l.GetBlocks()
}
