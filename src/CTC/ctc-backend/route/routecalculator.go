package route

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
)

type RouteCalculator struct {
	data *datastore.DataStore
}

func (r *RouteCalculator) CalculateRoute(train common.Train, destination common.Block) []common.Block {
	// Ensure they are not the same block
	if train.Location.Blocks[len(train.Location.Blocks)-1] == destination.Number {
		return []common.Block{}
	}

	// Advance search in the direction the train can go
	stop := false
	startBlock := r.data.Lines.Get(train.Line).Blocks.Get(train.Location.Blocks[len(train.Location.Blocks)-1])
	searchRoutes := make([][]common.Block, 0)
	searchRoutes = append(searchRoutes, make([]common.Block, 0))
	searchRoutes[0][0] = startBlock
	successfulPathIndexes := make([]int, 0)
	for !stop {
		// Do search for each path we are currently searching
		for i := 0; i < len(searchRoutes); i++ {
			currentBlock := searchRoutes[i][len(searchRoutes[i])-1]
			nextBlocks := r.getNextBlocks(currentBlock, train.Direction, r.data.Lines.Get(train.Line))
			if len(nextBlocks) > 1 {
				for j := 1; j < len(nextBlocks); j++ {
					// Make a branch from the current path
					newRoute := make([]common.Block, 0)
					newRoute = append(newRoute, searchRoutes[i]...)
					newRoute = append(newRoute, nextBlocks[j])
					searchRoutes = append(searchRoutes, newRoute)
				}
			}

			// Check if done
			if searchRoutes[i][len(searchRoutes)-1].Number == destination.Number {
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
	hasSwitch, trackSwitch := r.isSwitchBlock(block.Number, line)
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

func (r *RouteCalculator) isSwitchBlock(block int, line common.Line) (bool, *common.Switch) {
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
