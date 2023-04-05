package wayside

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
)

type WaysideController struct {
	address string
	line    string
	data    *datastore.DataStore
	stop    chan bool
}

func NewWaysideController(address string, line string, data *datastore.DataStore) *WaysideController {
	wc := WaysideController{
		address: address,
		line:    line,
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
			c.getSwitches()
		}

	}
}

func (c *WaysideController) getBlocks() {
	resp, err := http.Get(c.address + "/wayside")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)

	blocks := make([]common.BlockInfo, 0)
	json.Unmarshal(body, &blocks)

	c.data.Lines.SetBlockInfo(c.line, blocks)
}

func (c *WaysideController) getSwitches() {
	resp, err := http.Get(c.address + "/switches")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)

	switches := make([]common.SwitchInfo, 0)
	json.Unmarshal(body, &switches)

	c.data.Lines.SetSwitchPositions(c.line, switches)
}
