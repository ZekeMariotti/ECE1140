package app

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/frontendAPI"
)

type App struct {
	TimeKeeper  *common.TimeKeeper
	FrontendAPI *frontendAPI.FrontendAPI
	DataStore   *datastore.DataStore
}

func NewApp() *App {
	app := App{
		TimeKeeper: common.NewTimeKeeper(),
		DataStore:  datastore.NewDataStore(),
	}
	app.FrontendAPI = frontendAPI.NewFrontendAPI(app.DataStore)
	return &app
}

func (a *App) Start() {
	a.TimeKeeper.StartSimulation()
}
