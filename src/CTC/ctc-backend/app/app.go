package app

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/frontendAPI"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/outputs"
)

type App struct {
	TimeKeeper  *common.TimeKeeper
	FrontendAPI *frontendAPI.FrontendAPI
	OutputAPI   *outputs.OutputAPI
	DataStore   *datastore.DataStore
}

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

func (a *App) ImportLine(pathBlock string, pathSwitch string) {
	line := common.ParseLine(pathBlock, pathSwitch)
	a.DataStore.Lines.Set(line.Name, *line)
}

func (a *App) Start() {
	a.TimeKeeper.StartSimulation()
	a.OutputAPI.Serve()
	a.FrontendAPI.Serve()
}
