package common

import (
	"time"
)

type TimeKeeper struct {
	simulationTime  time.Time
	simulationSpeed int
	lastUpdateTime  time.Time
	stopSignal      chan bool
}

// Returns a new TimeKeeper object
func NewTimeKeeper() *TimeKeeper {
	return &TimeKeeper{}
}

// Starts the simulation time
// WARNING: Do not stop after starting unless ending the entire simulation
func (t *TimeKeeper) StartSimulation() {
	// Initialize variables
	t.simulationSpeed = 1
	t.simulationTime = time.Now()
	t.lastUpdateTime = time.Now()

	// Start service to update simulation time
	go t.simulationUpdateService()
}

// Stops the simulation time updating service
// WARNING: Do not call until wanting to close the entire simulation
func (t *TimeKeeper) StopSimulation() {
	t.stopSignal <- true
}

// Gets the current time of the simulation
func (t *TimeKeeper) GetSimulationTime() time.Time {
	return time.Now()
}

// Gets the current speed of the simulation
func (t *TimeKeeper) SetSimulationSpeed(simSpeed int) {
	t.simulationSpeed = simSpeed
}

// Service to continuously update the simulation time
// Call TimeKeeper.StartSimulation() to start, and TimeKeeper.StopSimulation() to stop
func (t *TimeKeeper) simulationUpdateService() {
	for {
		// Handle stop
		select {
		case <-t.stopSignal:
			return
		default:
			t.updateSimulationTime()
		}
	}
}

// Function to handle updating the simulation time
func (t *TimeKeeper) updateSimulationTime() {
	// Handle real time calculations
	realDelta := time.Since(t.lastUpdateTime)
	t.lastUpdateTime = time.Now()
	// Update simulation speed from delta
	simDelta := realDelta * time.Duration(t.simulationSpeed)
	t.simulationTime = t.simulationTime.Add(simDelta)
}
