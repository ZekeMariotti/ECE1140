package common

import (
	"time"

	"github.com/shopspring/decimal"
)

type TimeKeeper struct {
	simulationTime  time.Time
	simulationSpeed decimal.Decimal
	lastUpdateTime  time.Time
	stopSignal      chan bool
}

// Starts the simulation time
// WARNING: Do not stop after starting unless ending the entire simulation
func (t *TimeKeeper) StartSimulation() {
	// Initialize variables
	t.simulationSpeed = decimal.NewFromInt(1)
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
func (t *TimeKeeper) SetSimulationSpeed(simSpeed decimal.Decimal) {
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
	delta := time.Since(t.lastUpdateTime)
	t.lastUpdateTime = time.Now()
	// Update simulation speed from delta
	deltaDecimal := decimal.New(delta.Milliseconds(), 0)
	simDeltaDecimal := deltaDecimal.Mul(t.simulationSpeed)
	simDeltaString := simDeltaDecimal.String()
	simDelta, _ := time.ParseDuration(simDeltaString + "ms")
	t.simulationTime = t.simulationTime.Add(simDelta)
}
