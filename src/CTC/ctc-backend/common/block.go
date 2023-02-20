package common

import "github.com/shopspring/decimal"

type Block struct {
	ID                  BlockID         `json:"blockid"`
	Length              int             `json:"length"`
	Grade               decimal.Decimal `json:"grade"`
	SpeedLimit          int             `json:"speedlimit"`
	Elevation           decimal.Decimal `json:"elevation"`
	CumulativeElevation decimal.Decimal `json:"cumulative-elevation"`
	Underground         bool            `json:"underground"`
	Station             Station         `json:"station"`
	Switch              Switch          `json:"switch"`
}
