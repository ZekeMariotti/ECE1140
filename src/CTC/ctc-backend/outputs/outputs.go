package outputs

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

type OutputAPI struct {
	port   int
	data   *datastore.DataStore
	router *gin.Engine
}

func NewOutputAPI(port int, data *datastore.DataStore) *OutputAPI {
	api := OutputAPI{
		port:   port,
		data:   data,
		router: gin.Default(),
	}

	api.router.Use(cors.Default())

	return &api
}
