package common

type TrainLocation struct {
	Blocks []int `json:"blocks"`
}

func (l *TrainLocation) ExtendLocation(block int) {
	l.Blocks = append(l.Blocks, block)
}

func (l *TrainLocation) RemoveTail() {
	l.Blocks = l.Blocks[1:]
}
