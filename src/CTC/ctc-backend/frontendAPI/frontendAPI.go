package frontendAPI

import (
	"net/http"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

type FrontendAPI struct {
	router    *gin.Engine
	datastore *datastore.DataStore
}

func NewFrontendAPI(ds *datastore.DataStore) *FrontendAPI {
	api := FrontendAPI{
		datastore: ds,
	}
	api.initialize()
	return &api
}

func (a *FrontendAPI) initialize() {
	a.router = gin.Default()
	a.router.Use(cors.Default())
	a.setupPaths()

	a.router.Run("localhost:8080")
}

func (a *FrontendAPI) setupPaths() {
	prefix := "/api/frontend/"
	// GET Commands
	a.router.GET(prefix+"trains", a.getTrains)
	a.router.GET(prefix+"time", a.getTime)
}

func (a *FrontendAPI) getTrains(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, a.datastore.Trains)
}

func (a *FrontendAPI) getTime(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, a.datastore.TimeKeeper.GetSimulationTime())
}
