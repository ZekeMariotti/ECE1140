package wayside

import "github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"

type WaysideBlock struct {
	Number   int                `json:"number"`
	Occupied bool               `json:"occupied"`
	Signal   common.BlockSignal `json:"signal"`
}
