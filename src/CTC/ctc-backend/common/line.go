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
