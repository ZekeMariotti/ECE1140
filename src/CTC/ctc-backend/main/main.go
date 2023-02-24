package main

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/app"
)

func main() {
	app := app.NewApp()

	// Import lines
	app.ImportLine("../../redLineBlocks.csv", "../../redLineSwitches.csv")
	app.ImportLine("../../greenLineBlocks.csv", "../../greenLineSwitches.csv")

	// Import wayside controllers
	app.AddWayside("http://localhost:9080")

	app.Start()

	// Hold open
	for {

	}
}
