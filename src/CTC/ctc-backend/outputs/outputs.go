package outputs

import (
	"fmt"
	"net/http"
	"strconv"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

type OutputAPI struct {
	port   int
	data   *datastore.DataStore
	router *gin.Engine
}

// Create a new output API and initialize it
func NewOutputAPI(port int, data *datastore.DataStore) *OutputAPI {
	api := OutputAPI{
		port:   port,
		data:   data,
		router: gin.Default(),
	}

	api.router.Use(cors.Default())

	return &api
}

// Starts serving the API
func (a *OutputAPI) Serve() {
	url := fmt.Sprintf("0.0.0.0:%d", a.port)
	a.registerPaths()

	a.router.Run(url)
}

// Initialize API endpoints
func (a *OutputAPI) registerPaths() {
	a.router.GET("/api/line", a.getLines)
	a.router.GET("/api/line/:line", a.getLineByName)
	a.router.GET("/api/line/:line/blocks", a.getBlocks)
	a.router.GET("/api/line/:line/blocks/:block", a.getBlockByID)
	a.router.GET("/api/simulation", a.getSimulation)
	a.router.GET("/api/simulation/time", a.getSimulationTime)
	a.router.GET("/api/simulation/speed", a.getSimulationSpeed)
}

// HTTP GET handler for lines
func (a *OutputAPI) getLines(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, a.data.Lines.GetOutput())
}

// HTTP GET handler for lines
func (a *OutputAPI) getLineByName(c *gin.Context) {
	name := c.Param("line")
	line := a.data.Lines.Get(name)
	c.IndentedJSON(http.StatusOK, line.GetLineOutput())
}

// HTTP GET handler for block information
func (a *OutputAPI) getBlocks(c *gin.Context) {
	line := c.Param("line")
	c.IndentedJSON(http.StatusOK, a.data.Lines.GetOutputs(line))
}

// HTTP GET handler for block information
func (a *OutputAPI) getBlockByID(c *gin.Context) {
	line := c.Param("line")
	ID, _ := strconv.Atoi(c.Param("block"))
	l := a.data.Lines.Get(line)
	c.IndentedJSON(http.StatusOK, l.GetBlockOutput(ID))
}

// HTTP GET handler for simulation information
func (a *OutputAPI) getSimulation(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, a.data.TimeKeeper.GetSimulation())
}

// HTTP GET handler for simulation time information
func (a *OutputAPI) getSimulationTime(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, a.data.TimeKeeper.GetSimulationTime())
}

// HTTP GET handler for simulation speed information
func (a *OutputAPI) getSimulationSpeed(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, a.data.TimeKeeper.GetSimulationSpeed())
}
