package common

import (
	"sync"

	"github.com/shopspring/decimal"
	"golang.org/x/exp/maps"
)

// Implements a go-routine safe map for storing blocks
type SafeBlockMap struct {
	data map[int]Block
	mute sync.Mutex
}

func NewSafeBlockMap() *SafeBlockMap {
	m := SafeBlockMap{
		data: make(map[int]Block),
		mute: sync.Mutex{},
	}
	return &m
}

func NewSafeBlockMapFromSlice(slice []Block) *SafeBlockMap {
	m := SafeBlockMap{
		data: make(map[int]Block),
		mute: sync.Mutex{},
	}

	for _, v := range slice {
		m.data[v.Number] = v
	}

	return &m
}

func (m *SafeBlockMap) Get(key int) Block {
	m.mute.Lock()
	defer m.mute.Unlock()

	return m.data[key]
}

func (m *SafeBlockMap) Set(key int, value Block) {
	m.mute.Lock()
	defer m.mute.Unlock()

	m.data[key] = value
}

func (m *SafeBlockMap) HasKey(key int) bool {
	m.mute.Lock()
	defer m.mute.Unlock()

	_, ok := m.data[key]
	return ok
}

func (m *SafeBlockMap) GetSlice() []Block {
	m.mute.Lock()
	defer m.mute.Unlock()

	return maps.Values(m.data)
}

func (m *SafeBlockMap) GetCopy() map[int]Block {
	m.mute.Lock()
	defer m.mute.Unlock()

	return maps.Clone(m.data)
}

func (m *SafeBlockMap) SetBlockInfo(key int, occupied bool, signal BlockSignal) {
	m.mute.Lock()
	defer m.mute.Unlock()

	block := m.data[key]
	block.Occupied = occupied
	block.Signal = signal
	m.data[key] = block
}

func (m *SafeBlockMap) SetBlockOpen(key int, open bool) {
	m.mute.Lock()
	defer m.mute.Unlock()

	block := m.data[key]
	block.Open = open
	m.data[key] = block
}

func (m *SafeBlockMap) GetMaxID() int {
	m.mute.Lock()
	defer m.mute.Unlock()

	keys := maps.Keys(m.data)
	max := keys[0]
	for i := range keys {
		if i > max {
			max = i
		}
	}

	return max
}

func (m *SafeBlockMap) SetBlockAuthority(key int, authority int) {
	m.mute.Lock()
	defer m.mute.Unlock()

	block := m.data[key]
	block.Authority = authority
	m.data[key] = block
}

func (m *SafeBlockMap) SetBlockSpeed(key int, speed decimal.Decimal) {
	m.mute.Lock()
	defer m.mute.Unlock()

	block := m.data[key]

	if speed.Cmp(block.SpeedLimit) > 0 {
		speed = block.SpeedLimit
	}

	block.SuggestedSpeed = speed
	m.data[key] = block
}

func (m *SafeBlockMap) SetBlockOccupancy(key int, occupancy bool) {
	m.mute.Lock()
	defer m.mute.Unlock()

	block := m.data[key]
	block.Occupied = occupancy
	m.data[key] = block
}
