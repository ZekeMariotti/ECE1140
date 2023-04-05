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
	app.ImportLine("E:/Professional/ECE1140/src/CTC/redLineBlocks.csv", "E:/Professional/ECE1140/src/CTC/redLineSwitches.csv")
	app.ImportLine("E:/Professional/ECE1140/src/CTC/greenLineBlocks.csv", "E:/Professional/ECE1140/src/CTC/greenLineSwitches.csv")

	app.Start()

	// Hold open
	for {

	}
}
