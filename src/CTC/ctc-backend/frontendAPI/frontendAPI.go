package frontendAPI

import (
	"net/http"
	"time"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

var trains = []common.Train{}

func Start() {
	startTime := time.Now()
	delays := make([]time.Duration, 100)

	delays[0], _ = time.ParseDuration("164s")

	trains = []common.Train{
		{
			ID:     0,
			Line:   "Red",
			Driver: "Bob Builder",
			Stops: []common.TrainStop{
				{
					Station: "Shadyside",
					Time:    startTime.Add(delays[0]),
				},
			},
		},
	}

	r := gin.Default()
	r.Use(cors.Default())

	r.GET("/api/trains", getTrains)

	r.Run("localhost:8080")
}

func getTrains(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, trains)
}
