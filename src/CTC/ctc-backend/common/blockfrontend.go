package common

import "github.com/shopspring/decimal"

type BlockFrontend struct {
	Number         int             `json:"number"`
	Line           string          `json:"line"`
	Section        string          `json:"section"`
	Length         decimal.Decimal `json:"length"`
	Signal         BlockSignal     `json:"signal"`
	Occupied       bool            `json:"occupied"`
	SuggestedSpeed decimal.Decimal `json:"suggestedspeed"`
	Authority      int             `json:"authority"`
	Open           bool            `json:"open"`
}
