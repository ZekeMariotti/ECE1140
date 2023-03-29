package common

type BlockInfo struct {
	Block    int         `json:"block"`
	Occupied bool        `json:"occupied"`
	Signal   BlockSignal `json:"signal"`
}
