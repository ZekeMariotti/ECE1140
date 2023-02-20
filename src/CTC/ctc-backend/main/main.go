package main

import "github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/app"

func main() {
	app := app.NewApp()
	app.Start()

	// Hold open
	for {

	}
}
