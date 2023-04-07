package main

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/app"
	"github.com/gin-gonic/gin"
)

func main() {
	// Set HTTP server mode to release
	gin.SetMode(gin.ReleaseMode)

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
