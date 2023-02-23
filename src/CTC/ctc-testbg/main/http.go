package main

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

type WaysideHttp struct {
	port   int
	router *gin.Engine
	data   *Data
}

func NewWaysideHttp(port int, data *Data) *WaysideHttp {
	s := WaysideHttp{
		port:   port,
		router: gin.Default(),
		data:   data,
	}
	s.setupRoutes()
	return &s
}

func (s *WaysideHttp) Serve() {
	url := fmt.Sprintf("0.0.0.0:%d", s.port)
	s.router.Run(url)
}

func (s *WaysideHttp) setupRoutes() {
	s.router.GET("/blocks", s.getBlocks)
	s.router.GET("/switches", s.getSwitches)
}

func (s *WaysideHttp) getBlocks(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, s.data.Blocks)
}

func (s *WaysideHttp) getSwitches(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, s.data.Switches)
}
