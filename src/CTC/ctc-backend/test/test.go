package test

import (
	"fmt"
	"time"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/app"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/route"
)

func RunTests() {
	// Test case
	correctRoute := []int{63, 64, 65}

	// Make a new app
	a := app.NewApp()

	// Import lines
	a.ImportLine("./redLineBlocks.csv", "./redLineSwitches.csv")
	a.ImportLine("./greenLineBlocks.csv", "./greenLineSwitches.csv")

	// Start app
	go a.Start()

	// Add a new train to green line
	testTrainFrontend := common.TrainFrontend{
		ID:     1,
		Line:   "Green",
		Driver: "Frank",
		Location: common.TrainLocation{
			Blocks: []int{0, 63},
		},
		Stops: []common.TrainStopFrontend{
			{
				Station: "GLENBURY",
				Time: common.StopTime{
					Time: time.Now().Add(time.Minute * 7),
				},
			},
		},
	}
	testTrain := a.DataStore.TrainFrontendToBackend(testTrainFrontend)
	a.DataStore.Trains.Set(testTrain.ID, testTrain)

	// Test routing function for train
	routeGen := route.NewRouteCalculator(a.DataStore)
	result := routeGen.CalculateRoute(testTrain, a.DataStore.Lines.Get("Green").Blocks.Get(62))
	correct := true
	for i := range result {
		if len(correctRoute) <= i {
			correct = false
			break
		}
		if result[i] != correctRoute[i] {
			correct = false
			break
		}
	}

	// Report
	if correct {
		fmt.Println("Test Case passed!")
	} else {
		fmt.Println("Test Case failed!")
		fmt.Println("Result:", result)
	}
}
