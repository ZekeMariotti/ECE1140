package frontendAPI

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"strconv"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

type FrontendAPI struct {
	port      int
	router    *gin.Engine
	datastore *datastore.DataStore
}

// Creates a new front end API
func NewFrontendAPI(port int, ds *datastore.DataStore) *FrontendAPI {
	api := FrontendAPI{
		port:      port,
		datastore: ds,
	}
	api.initialize()
	return &api
}

// Begins serving frontend API
func (a *FrontendAPI) Serve() {
	url := fmt.Sprintf("0.0.0.0:%d", a.port)
	a.router.Run(url)
}

// Intializes variables for the API
func (a *FrontendAPI) initialize() {
	a.router = gin.Default()
	a.router.Use(cors.Default())
	a.setupPaths()
}

// Registers paths to the API
func (a *FrontendAPI) setupPaths() {
	// GET (Read) Commands
	a.router.GET("/api/frontend/lines", a.getLines)
	a.router.GET("/api/frontend/lines/:name", a.getLineByName)
	a.router.GET("/api/frontend/lines/:name/blocks", a.getBlocks)
	a.router.GET("/api/frontend/lines/:name/stations", a.getStations)
	a.router.GET("/api/frontend/trains", a.getTrains)
	a.router.GET("/api/frontend/time", a.getTime)
	a.router.GET("/api/frontend/simulationspeed", a.getSimulationSpeed)
	// POST (Create) Commands
	a.router.POST("/api/frontend/trains", a.postTrains)
	a.router.PUT("/api/frontend/simulationspeed", a.putSimulationSpeed)
	a.router.PUT("/api/frontend/lines/:name/blocks/:block/open", a.putBlockOpen)
}

// Handler for GET /lines
func (a *FrontendAPI) getLines(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, a.datastore.Lines.GetLineNames())
}

// Handler for GET /lines/{name}
func (a *FrontendAPI) getLineByName(c *gin.Context) {
	name := c.Param("name")
	if a.datastore.Lines.HasKey(name) {
		c.IndentedJSON(http.StatusOK, a.datastore.Lines.Get(name))
		return
	}
	c.IndentedJSON(http.StatusNotFound, gin.H{"message": fmt.Sprintf("Line %s not found", name)})
}

// Handler for GET /lines/{name}/blocks
func (a *FrontendAPI) getBlocks(c *gin.Context) {
	name := c.Param("name")
	if a.datastore.Lines.HasKey(name) {
		c.IndentedJSON(http.StatusOK, a.datastore.Lines.GetBlocksUI(name))
		return
	}
	c.IndentedJSON(http.StatusNotFound, gin.H{"message": fmt.Sprintf("Line %s stations not found", name)})
}

// Handler for GET /lines/{name}/stations
func (a *FrontendAPI) getStations(c *gin.Context) {
	name := c.Param("name")
	if a.datastore.Lines.HasKey(name) {
		c.IndentedJSON(http.StatusOK, a.datastore.Lines.GetStations(name))
		return
	}
	c.IndentedJSON(http.StatusNotFound, gin.H{"message": fmt.Sprintf("Line %s stations not found", name)})
}

// Handler for GET /trains
func (a *FrontendAPI) getTrains(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, a.datastore.Trains.GetSlice())
}

// Handler for GET /time
func (a *FrontendAPI) getTime(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, a.datastore.TimeKeeper.GetSimulationTime())
}

// Handler for GET /simulationSpeed
func (a *FrontendAPI) getSimulationSpeed(c *gin.Context) {
	speed := a.datastore.TimeKeeper.GetSimulationSpeed()
	c.IndentedJSON(http.StatusOK, speed)
}

// Handler for POST /trains
func (a *FrontendAPI) postTrains(c *gin.Context) {
	result := common.Train{}
	body, _ := io.ReadAll(c.Request.Body)
	json.Unmarshal(body, &result)
	a.datastore.Trains.Set(result.ID, result)
}

// Handler for PUT /simulationSpeed
func (a *FrontendAPI) putSimulationSpeed(c *gin.Context) {
	result := int(1)
	body, _ := io.ReadAll(c.Request.Body)
	json.Unmarshal(body, &result)
	a.datastore.TimeKeeper.SetSimulationSpeed(result)
}

// Handler for PUT /lines/:name/blocks/:block/open
func (a *FrontendAPI) putBlockOpen(c *gin.Context) {
	result := bool(true)
	line := c.Param("name")
	blockStr := c.Param("block")
	block, _ := strconv.Atoi(blockStr)
	body, _ := io.ReadAll(c.Request.Body)
	json.Unmarshal(body, &result)
	a.datastore.Lines.SetBlockOpen(line, block, result)
}
