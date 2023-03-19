package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func main() {
	ws := NewWaysideHttp(9080, 8090)
	ws.StartCTC()
	ws.Serve()

	// Keep open
	for {
	}
}

type SwitchInfo struct {
	Source   int `json:"source"`
	Dest1    int `json:"destination1"`
	Dest2    int `json:"destination2"`
	Position int `json:"position"`
}

type BlockInfo struct {
	Block    int         `json:"block"`
	Occupied bool        `json:"occupied"`
	Signal   BlockSignal `json:"signal"`
}

type BlockSignal string

const (
	BLOCKSIGNAL_GREEN  BlockSignal = "Green"
	BLOCKSIGNAL_YELLOW BlockSignal = "Yellow"
	BLOCKSIGNAL_RED    BlockSignal = "Red"
)

type WaysideHttp struct {
	port       int
	router     *gin.Engine
	blocks     []BlockInfo
	switches   []SwitchInfo
	simulation json.RawMessage
	ctcout     json.RawMessage
	ctcPort    int
	stop       chan bool
}

func NewWaysideHttp(port int, ctcPort int) *WaysideHttp {
	s := WaysideHttp{
		port:    port,
		router:  gin.Default(),
		ctcPort: ctcPort,
		stop:    make(chan bool),
	}
	s.router.Use(cors.Default())
	s.setupRoutes()
	return &s
}

func (s *WaysideHttp) Serve() {
	url := fmt.Sprintf("0.0.0.0:%d", s.port)
	s.router.Run(url)
}

// ----- From CTC -----
func (s *WaysideHttp) StartCTC() {
	go s.ctcloop()
}

func (s *WaysideHttp) StopCTC() {
	s.stop <- true
}

func (s *WaysideHttp) ctcloop() {
	for {
		select {
		case <-s.stop:
			return
		default:
			s.getCtcValues()
		}
	}
}

func (s *WaysideHttp) getCtcValues() {
	url := fmt.Sprintf("http://127.0.0.1:%d", s.ctcPort)
	respBlocks, err1 := http.Get(url + "/api/line/Red/blocks")
	respSim, err2 := http.Get(url + "/api/simulation")
	if err1 != nil || err2 != nil {
		fmt.Println(err1, "\n", err2)
		return
	}
	defer respBlocks.Body.Close()
	defer respSim.Body.Close()

	ctcBlocks := new(json.RawMessage)
	bodyBlocks, _ := io.ReadAll(respBlocks.Body)
	json.Unmarshal(bodyBlocks, ctcBlocks)
	s.ctcout = *ctcBlocks

	ctcSim := new(json.RawMessage)
	bodySim, _ := io.ReadAll(respSim.Body)
	json.Unmarshal(bodySim, ctcSim)
	s.simulation = *ctcSim
}

// ----- To CTC & UI -----
func (s *WaysideHttp) setupRoutes() {
	s.router.GET("/blocks", s.getBlocks)
	s.router.GET("/switches", s.getSwitches)
	s.router.GET("/ctc/lines", s.getCtcLines)
	s.router.GET("/ctc/simulation", s.getCtcSimulation)
	s.router.PUT("/blocks", s.putBlocks)
	s.router.PUT("/switches", s.putSwitches)
}

func (s *WaysideHttp) getCtcLines(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, string(s.ctcout))
}

func (s *WaysideHttp) getCtcSimulation(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, string(s.simulation))
}

func (s *WaysideHttp) getBlocks(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, s.blocks)
}

func (s *WaysideHttp) putBlocks(c *gin.Context) {
	body, _ := io.ReadAll(c.Request.Body)
	blocks := make([]BlockInfo, 0)
	json.Unmarshal(body, &blocks)
	s.blocks = blocks
}

func (s *WaysideHttp) getSwitches(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, s.switches)
}

func (s *WaysideHttp) putSwitches(c *gin.Context) {
	body, _ := io.ReadAll(c.Request.Body)
	switches := make([]SwitchInfo, 0)
	json.Unmarshal(body, &switches)
	s.switches = switches
}
