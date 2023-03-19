package common

import "github.com/shopspring/decimal"

type BlockOutput struct {
	Block          int             `json:"block"`
	Authority      int             `json:"authority"`
	SuggestedSpeed decimal.Decimal `json:"suggested-speed"`
	Open           bool            `json:"open"`
}
