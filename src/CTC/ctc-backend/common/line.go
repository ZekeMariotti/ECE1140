package common

import (
	"sort"
)

type Line struct {
	Name     string        `json:"name"`
	Blocks   *SafeBlockMap `json:"blocks"`
	Switches []Switch      `json:"switches"`
	Stations []Station     `json:"stations"`
}

func NewLineFromSlice(name string, blocks []Block, switches []Switch, stations []Station) *Line {
	l := Line{
		Name:     name,
		Blocks:   NewSafeBlockMap(),
		Switches: make([]Switch, len(switches)),
		Stations: make([]Station, len(stations)),
	}

	for _, v := range blocks {
		l.Blocks.Set(v.Number, v)
	}
	for i := range switches {
		l.Switches[i] = switches[i]
	}
	for i := range stations {
		l.Stations[i] = stations[i]
	}

	return &l
}

func (l *Line) SetBlockInfos(occupancies []BlockInfo) {
	for _, v := range occupancies {
		l.Blocks.SetBlockInfo(v.Block, v.Occupied, v.Signal)
	}
}

func (l *Line) SetSwitchPositions(positions []SwitchInfo) {
	for _, v := range positions {
		for _, w := range l.Switches {
			if w.Source == v.Source {
				w.SetPosition(v.Position)
			}
		}
	}
}

// Returns suggested speed, authority, and operational status per block
func (l *Line) GetBlockOutputs() []BlockOutput {
	blocks := l.Blocks.GetSlice()
	result := make([]BlockOutput, len(blocks))
	for i, v := range blocks {
		out := BlockOutput{
			Block:          v.Number,
			Authority:      v.Authority,
			SuggestedSpeed: v.SuggestedSpeed,
			Open:           v.Open,
		}
		result[i] = out
	}
	sort.Slice(result, func(i, j int) bool {
		return result[i].Block < result[j].Block
	})
	return result
}

// Returns suggested speed, authority, and operational status for one block
func (l *Line) GetBlockOutput(ID int) BlockOutput {
	block := l.Blocks.Get(ID)
	return BlockOutput{
		Block:          block.Number,
		Authority:      block.Authority,
		SuggestedSpeed: block.SuggestedSpeed,
		Open:           block.Open,
	}
}

func (l *Line) GetLineOutput() LineOutput {
	out := LineOutput{
		Name:   l.Name,
		Blocks: l.GetBlockOutputs(),
	}
	return out
}

func (l *Line) GetStations() []string {
	result := make([]string, len(l.Stations))
	for i := range l.Stations {
		result[i] = l.Stations[i].Name
	}
	return result
}

func (l *Line) GetBlocks() []BlockFrontend {
	blocks := l.Blocks.GetSlice()
	result := make([]BlockFrontend, len(blocks))
	for i, v := range blocks {
		result[i] = BlockFrontend{
			Number:         v.Number,
			Line:           v.Line,
			Section:        v.Section,
			Length:         v.Length,
			Signal:         v.Signal,
			Occupied:       v.Occupied,
			SuggestedSpeed: v.SuggestedSpeed,
			Authority:      v.Authority,
			Open:           v.Open,
		}
	}
	sort.Slice(result, func(i, j int) bool {
		return result[i].Number < result[j].Number
	})
	return result
}

func (l *Line) GetStationByName(name string) Station {
	for i, v := range l.Stations {
		if v.Name == name {
			return l.Stations[i]
		}
	}

	// Failed
	return Station{}
}
