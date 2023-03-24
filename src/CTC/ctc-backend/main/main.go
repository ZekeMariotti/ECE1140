package main

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/app"
)

func main() {
	app := app.NewApp()

	// Import lines
	app.ImportLine("E:/Professional/ECE1140/src/CTC/redLineBlocks.csv", "E:/Professional/ECE1140/src/CTC/redLineSwitches.csv")
	app.ImportLine("E:/Professional/ECE1140/src/CTC/greenLineBlocks.csv", "E:/Professional/ECE1140/src/CTC/greenLineSwitches.csv")

	// Import wayside controllers
	app.AddWayside("http://localhost:9080")

	app.Start()

	// Hold open
	for {

	}
}
