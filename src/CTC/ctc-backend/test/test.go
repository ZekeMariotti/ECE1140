package test

import (
	"encoding/json"
	"fmt"
	"time"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/app"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/route"
)

func RunTests() {
	// ----- Test Route Generation -----
	// Case 01
	fmt.Print("CASE 01: ")
	case01_expected := []int{63, 64, 65}
	case01_pass, case01_result := testRoute(63, "GLENBURY", 65, "Green", case01_expected)
	if case01_pass {
		fmt.Print("PASS")
	} else {
		fmt.Println("FAILURE")
		fmt.Println("Expected Route:", case01_expected)
		fmt.Println("Received Route:", case01_result)
	}
	fmt.Println()

	// Case 02
	fmt.Print("CASE 02: ")
	case02_expected := []int{63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 85, 84, 83, 82, 81, 80, 79, 78, 77, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57}
	case02_pass, case02_result := testRoute(63, "OVERBROOK", 57, "Green", case02_expected)
	if case02_pass {
		fmt.Print("PASS")
	} else {
		fmt.Println("FAILURE")
		fmt.Println("Expected Route:", case02_expected)
		rst, _ := json.Marshal(case02_result)
		fmt.Println("Received Route:", string(rst))
	}
	fmt.Println()

	// Case 03
	fmt.Print("CASE 03: ")
	case03_expected := []int{0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16}
	case03_pass, case03_result := testRoute(0, "HERRON AVE", 16, "Red", case03_expected)
	if case03_pass {
		fmt.Print("PASS")
	} else {
		fmt.Println("FAILURE")
		fmt.Println("Expected Route:", case03_expected)
		rst, _ := json.Marshal(case03_result)
		fmt.Println("Received Route:", string(rst))
	}
	fmt.Println()

	// Case 04
	fmt.Print("CASE 04: ")
	case04_expected := []int{0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60}
	case04_pass, case04_result := testRoute(0, "SOUTH HILLS JUNCTION", 60, "Red", case04_expected)
	if case04_pass {
		fmt.Print("PASS")
	} else {
		fmt.Println("FAILURE")
		fmt.Println("Expected Route:", case04_expected)
		rst, _ := json.Marshal(case04_result)
		fmt.Println("Received Route:", string(rst))
	}
	fmt.Println()
}

func testRoute(src int, station string, dst int, line string, expected []int) (bool, []int) {
	// Start new app instance
	a := app.NewApp()
	a.ImportLine("./redLineBlocks.csv", "./redLineSwitches.csv")
	a.ImportLine("./greenLineBlocks.csv", "./greenLineSwitches.csv")
	go a.Start()

	// Toss train into instance
	trainFrontend := common.TrainFrontend{
		ID:     1,
		Line:   line,
		Driver: "Test Driver",
		Location: common.TrainLocation{
			Blocks: []int{src},
		},
		Stops: []common.TrainStopFrontend{
			{
				Station: station,
				Time: common.StopTime{
					Time: time.Now().Add(time.Minute * 7),
				},
			},
		},
	}
	testTrain := a.DataStore.TrainFrontendToBackend(trainFrontend)
	a.DataStore.Trains.Set(testTrain.ID, testTrain)

	// Test routing function for train
	routeGen := route.NewRouteCalculator(a.DataStore)
	result := routeGen.CalculateRoute(testTrain, a.DataStore.Lines.Get(line).Blocks.Get(dst))
	correct := true
	for i := range result {
		if len(expected) <= i {
			correct = false
			break
		}
		if result[i] != expected[i] {
			correct = false
			break
		}
	}
	return correct, result
}
