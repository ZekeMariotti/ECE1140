package common

type Line struct {
	Name     string        `json:"name"`
	Blocks   *SafeBlockMap `json:"blocks"`
	Switches []*Switch     `json:"switches"`
	Stations []*Station    `json:"stations"`
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
