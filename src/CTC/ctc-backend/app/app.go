package app

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/frontendAPI"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/outputs"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/wayside"
)

type App struct {
	TimeKeeper  *common.TimeKeeper
	FrontendAPI *frontendAPI.FrontendAPI
	OutputAPI   *outputs.OutputAPI
	DataStore   *datastore.DataStore
	Waysides    []*wayside.WaysideController
}

// Returns a new instance of the application
func NewApp() *App {
	app := App{
		TimeKeeper: common.NewTimeKeeper(),
		DataStore:  datastore.NewDataStore(),
	}
	app.FrontendAPI = frontendAPI.NewFrontendAPI(8080, app.DataStore)
	app.OutputAPI = outputs.NewOutputAPI(8090, app.DataStore)
	app.DataStore.TimeKeeper = app.TimeKeeper
	return &app
}

// Imports a line from a pair of csv files to the system
func (a *App) ImportLine(pathBlock string, pathSwitch string) {
	line := common.ParseLine(pathBlock, pathSwitch)
	a.DataStore.Lines.Set(line.Name, *line)
}

func (a *App) AddWayside(address string) {
	ws := wayside.NewWaysideController(address, "Red", a.DataStore)
	ws.StartServices()
	a.Waysides = append(a.Waysides, ws)
}

// Starts running the app
func (a *App) Start() {
	a.TimeKeeper.StartSimulation()
	go a.OutputAPI.Serve()
	go a.FrontendAPI.Serve()
}
