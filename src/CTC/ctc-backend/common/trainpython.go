package common

type TrainPython struct {
	ID   int    `json:"id"`
	Line string `json:"line"`
}

func TrainToPython(train Train) TrainPython {
	t := TrainPython{
		ID:   train.ID,
		Line: train.Line,
	}
	return t
}
