package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"

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

type WaysideHttp struct {
	port       int
	router     *gin.Engine
	blocks     json.RawMessage
	switches   json.RawMessage
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
	url := fmt.Sprintf("127.0.0.1:%d", s.ctcPort)
	respBlocks, _ := http.Get(url + "/api/line/Red/blocks")
	respSim, _ := http.Get(url + "/api/simulation")

	s.ctcout, _ = io.ReadAll(respBlocks.Body)
	s.simulation, _ = io.ReadAll(respSim.Body)
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
	c.IndentedJSON(http.StatusOK, s.ctcout)
}

func (s *WaysideHttp) getCtcSimulation(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, s.simulation)
}

func (s *WaysideHttp) getBlocks(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, s.blocks)
}

func (s *WaysideHttp) putBlocks(c *gin.Context) {
	body, _ := io.ReadAll(c.Request.Body)
	s.blocks = body
}

func (s *WaysideHttp) getSwitches(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, s.switches)
}

func (s *WaysideHttp) putSwitches(c *gin.Context) {
	body, _ := io.ReadAll(c.Request.Body)
	s.switches = body
}
