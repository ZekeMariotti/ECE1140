package route

import (
	"fmt"

	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
)

type RouteCalculator struct {
	data *datastore.DataStore
}

func NewRouteCalculator(data *datastore.DataStore) *RouteCalculator {
	calc := RouteCalculator{
		data: data,
	}

	return &calc
}

func (r *RouteCalculator) CalculateRoute(train common.Train, destination common.Block) []int {
	// Fix issue?
	if len(train.Location.Blocks) < 1 {
		return make([]int, 0)
	}

	// Ensure they are not the same block
	if train.Location.Blocks[len(train.Location.Blocks)-1] == destination.Number {
		return make([]int, 0)
	}

	// Advance search in the direction the train can go
	stop := false
	line := r.data.Lines.Get(train.Line)
	startBlock := r.data.Lines.Get(train.Line).Blocks.Get(train.Location.Blocks[len(train.Location.Blocks)-1])
	searchRoutes := make([][]int, 0)
	searchRoutes = append(searchRoutes, make([]int, 1))
	searchRoutes[0][0] = startBlock.Number
	successfulPathIndexes := make([]int, 0)
	for !stop {
		// Do search for each path we are currently searching
		//fmt.Println(searchRoutes)
		for i := 0; i < len(searchRoutes); i++ {
			currentBlock := searchRoutes[i][len(searchRoutes[i])-1]
			rawBlocks := r.getNextBlocks(line.Blocks.Get(currentBlock), train.Direction, line)
			nextBlocks := make([]common.Block, 0)
			for j := range rawBlocks {
				good := true
				for k := range searchRoutes[i] {
					if searchRoutes[i][k] == rawBlocks[j].Number {
						good = false
					}
				}
				if good {
					nextBlocks = append(nextBlocks, rawBlocks[j])
				}
			}
			fmt.Print(i, ": ", currentBlock, ": ")
			for i := range nextBlocks {
				fmt.Print(nextBlocks[i].Number, ",")
			}
			fmt.Println()
			if len(nextBlocks) > 1 {
				for j := 1; j < len(nextBlocks); j++ {
					// Make a branch from the current path
					newRoute := make([]int, len(searchRoutes[i]))
					copy(newRoute, searchRoutes[i])
					newRoute = append(newRoute, nextBlocks[j].Number)
					searchRoutes = append(searchRoutes, newRoute)
				}
			}
			searchRoutes[i] = append(searchRoutes[i], nextBlocks[0].Number)

			// Check if done
			if searchRoutes[i][len(searchRoutes[i])-1] == destination.Number {
				stop = true
				successfulPathIndexes = append(successfulPathIndexes, i)
			}
		}
	}

	// Find shortest path
	lengths := make([]int, len(searchRoutes))
	minLength := 1
	minIndex := -1
	for _, v := range successfulPathIndexes {
		lengths[v] = len(searchRoutes[v])

		// Do first time min setup
		if minIndex == -1 {
			minIndex = v
			minLength = lengths[v]
		}

		// Check for new min
		if lengths[v] < minLength {
			minIndex = v
			minLength = lengths[v]
		}
	}

	// Return minimized route
	return searchRoutes[minIndex]
}

func (r *RouteCalculator) getNextBlocks(block common.Block, trainDir common.TrainDirection, line common.Line) []common.Block {
	hasSwitch, trackSwitch := r.IsSwitchBlock(block.Number, line)
	nextBlocksIDs := make([]int, 0)

	switch block.Direction {
	case common.BLOCKDIRECTION_BIDIRECTIONAL:
		if trainDir == common.TRAINDIRECTION_ASCENDING {
			if hasSwitch && (trackSwitch.Side == common.BLOCKSIDE_ASCEND) {
				nextBlocksIDs = append(nextBlocksIDs, trackSwitch.GetNextBlocks(block.Number)...)
			} else {
				nextBlocksIDs = append(nextBlocksIDs, block.Number+1)
			}
		} else if trainDir == common.TRAINDIRECTION_DESCENDING {
			if hasSwitch && (trackSwitch.Side == common.BLOCKSIDE_DESCEND) {
				nextBlocksIDs = append(nextBlocksIDs, trackSwitch.GetNextBlocks(block.Number)...)
			} else {
				nextBlocksIDs = append(nextBlocksIDs, block.Number-1)
			}
		}
	case common.BLOCKDIRECTION_ASCENDING:
		if hasSwitch && (trackSwitch.Side == common.BLOCKSIDE_ASCEND) {
			nextBlocksIDs = append(nextBlocksIDs, trackSwitch.GetNextBlocks(block.Number)...)
		} else {
			nextBlocksIDs = append(nextBlocksIDs, block.Number+1)
		}
	case common.BLOCKDIRECTION_DESCENDING:
		if hasSwitch && (trackSwitch.Side == common.BLOCKSIDE_DESCEND) {
			nextBlocksIDs = append(nextBlocksIDs, trackSwitch.GetNextBlocks(block.Number)...)
		} else {
			nextBlocksIDs = append(nextBlocksIDs, block.Number-1)
		}
	}

	nextBlocks := make([]common.Block, len(nextBlocksIDs))
	for i, v := range nextBlocksIDs {
		nextBlocks[i] = line.Blocks.Get(v)
	}

	return nextBlocks
}

func (r *RouteCalculator) IsSwitchBlock(block int, line common.Line) (bool, *common.Switch) {
	for i := range line.Switches {
		if line.Switches[i].Destination1 == block {
			return true, &line.Switches[i]
		}
		if line.Switches[i].Destination2 == block {
			return true, &line.Switches[i]
		}
		if line.Switches[i].Source == block {
			return true, &line.Switches[i]
		}
	}
	return false, &common.Switch{}
}
