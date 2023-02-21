package frontendAPI

import (
	"fmt"
	"net/http"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

type FrontendAPI struct {
	router    *gin.Engine
	datastore *datastore.DataStore
}

// Creates a new front end API
func NewFrontendAPI(ds *datastore.DataStore) *FrontendAPI {
	api := FrontendAPI{
		datastore: ds,
	}
	api.initialize()
	return &api
}

// Begins serving frontend API
func (a *FrontendAPI) Serve(address string) {
	a.router.Run(address)
}

// Intializes variables for the API
func (a *FrontendAPI) initialize() {
	a.router = gin.Default()
	a.router.Use(cors.Default())
	a.setupPaths()
}

// Registers paths to the API
func (a *FrontendAPI) setupPaths() {
	prefix := "/api/frontend/"
	// GET Commands
	a.router.GET(prefix+"lines", a.getLines)
	a.router.GET(prefix+"lines/:name", a.getLineByName)
	a.router.GET(prefix+"trains", a.getTrains)
	a.router.GET(prefix+"time", a.getTime)
}

// Handler for GET /lines
func (a *FrontendAPI) getLines(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, a.datastore.Lines.GetSlice())
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

// Handler for GET /trains
func (a *FrontendAPI) getTrains(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, a.datastore.Trains.GetSlice())
}

// Handler for GET /time
func (a *FrontendAPI) getTime(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, a.datastore.TimeKeeper.GetSimulationTime())
}
