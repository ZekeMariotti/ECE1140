package main

import "encoding/json"

type Data struct {
	Blocks   json.RawMessage
	Switches json.RawMessage
}
