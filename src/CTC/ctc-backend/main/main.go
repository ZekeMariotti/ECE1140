package main

import (
	"fmt"
	"os"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/app"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/test"
	"github.com/gin-gonic/gin"
)

func main() {
	// Get arguments
	args := os.Args[1:]

	// Set HTTP server mode to release
	gin.SetMode(gin.ReleaseMode)

	// Check if we are running test cases
	if args[0] == "test" {
		fmt.Println("Running tests")
		test.RunTests()
		return
	}

	// Create a new application instance
	app := app.NewApp()

	// Import lines
	app.ImportLine("./redLineBlocks.csv", "./redLineSwitches.csv")
	app.ImportLine("./greenLineBlocks.csv", "./greenLineSwitches.csv")

	app.Start()

	// Hold open
	for {

	}
}
