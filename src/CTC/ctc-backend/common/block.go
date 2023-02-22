package common

import "github.com/shopspring/decimal"

// Represents a single block on a train track
type Block struct {
	Number              int             `json:"number"`
	Line                string          `json:"line"`
	Section             string          `json:"section"`
	Length              decimal.Decimal `json:"length"`
	Grade               decimal.Decimal `json:"grade"`
	SpeedLimit          decimal.Decimal `json:"speedlimit"`
	Direction           BlockDirection  `json:"direction"`
	Elevation           decimal.Decimal `json:"elevation"`
	CumulativeElevation decimal.Decimal `json:"cumulative-elevation"`
	Underground         bool            `json:"underground"`
	Crossing            bool            `json:"crossing"`
	Station             *Station        `json:"station"`
	Switch              *Switch         `json:"switch"`
	Signal              BlockSignal     `json:"signal"`
	Occupied            bool            `json:"occupied"`
	SuggestedSpeed      decimal.Decimal `json:"suggested-speed"`
	Authority           int             `json:"authority"`
	Open                bool            `json:"open"`
}
