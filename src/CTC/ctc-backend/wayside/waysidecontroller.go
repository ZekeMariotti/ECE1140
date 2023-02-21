package wayside

import (
	"encoding/json"
	"io"
	"log"
	"net/http"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
)

type WaysideController struct {
	Address string
	Line    string
	data    *datastore.DataStore
	stop    chan bool
}

func NewWaysideController(address string, line string, data *datastore.DataStore) *WaysideController {
	wc := WaysideController{
		Address: address,
		Line:    line,
		data:    data,
		stop:    make(chan bool),
	}

	return &wc
}

func (c *WaysideController) StartServices() {
	go c.updateService()
}

func (c *WaysideController) StopServices() {
	c.stop <- true
}

func (c *WaysideController) updateService() {
	for {
		select {
		case <-c.stop:
			return
		default:
			c.getBlocks()
		}

	}
}

func (c *WaysideController) getBlocks() {
	resp, err := http.Get(c.Address + "/blocks")
	if err != nil {
		log.Default().Println(err)
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)

	blocks := make([]WaysideBlock, 0)
	json.Unmarshal(body, &blocks)

	for _, v := range blocks {
		line := c.data.Lines.Get(c.Line)
		block := line.Blocks.Get(v.Number)
		block.Occupied = v.Occupied
		block.Signal = v.Signal
		line.Blocks.Set(block.Number, block)
		c.data.Lines.Set(line.Name, line)
	}
}

func (c *WaysideController) getSwitches() {
	resp, err := http.Get(c.Address + "/switches")
	if err != nil {
		log.Default().Println(err)
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)

	switches := make([]WaysideSwitch, 0)
	json.Unmarshal(body, &switches)

	for _, v := range switches {
		line := c.data.Lines.Get(c.Line)
		for i, v := range line.Switches
	}
}
