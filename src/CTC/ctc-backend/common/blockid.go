package common

type BlockID struct {
	Line    string `json:"line"`
	Section string `json:"section"`
	Number  int    `json:"number"`
}
