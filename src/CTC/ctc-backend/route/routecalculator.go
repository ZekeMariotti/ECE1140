package route

import (
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/common"
	"github.com/ZekeMariotti/ECE1140/tree/master/src/CTC/ctc-backend/datastore"
)

type RouteCalculator struct {
	data *datastore.DataStore
}

type newBlock struct {
	block     common.Block
	searchDir common.TrainDirection
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
	searchRoutes := make([][]newBlock, 0)
	searchRoutes = append(searchRoutes, make([]newBlock, 1))
	searchRoutes[0][0] = newBlock{block: startBlock, searchDir: train.Direction}
	successfulPathIndexes := make([]int, 0)
	for !stop {
		// Do search for each path we are currently searching
		for i := 0; i < len(searchRoutes); i++ {
			currentBlock := searchRoutes[i][len(searchRoutes[i])-1].block
			lastBlock := searchRoutes[i][len(searchRoutes[i])-1].block
			if len(searchRoutes[i]) > 1 {
				lastBlock = searchRoutes[i][len(searchRoutes[i])-2].block
			}
			currentDir := searchRoutes[i][len(searchRoutes[i])-1].searchDir
			rawBlocks := r.getNextBlocks(lastBlock, currentBlock, currentDir, line)
			nextBlocks := make([]newBlock, 0)
			for j := range rawBlocks {
				good := true
				// Add any filtering here as needed
				if good {
					nextBlocks = append(nextBlocks, rawBlocks[j])
				}
			}

			if len(nextBlocks) > 1 {
				for j := 1; j < len(nextBlocks); j++ {
					// Make a branch from the current path
					newRoute := make([]newBlock, len(searchRoutes[i]))
					copy(newRoute, searchRoutes[i])
					newRoute = append(newRoute, nextBlocks[j])
					searchRoutes = append(searchRoutes, newRoute)
				}
			}
			if len(nextBlocks) > 0 {
				searchRoutes[i] = append(searchRoutes[i], nextBlocks[0])
			}

			// Check if done
			if searchRoutes[i][len(searchRoutes[i])-1].block.Number == destination.Number {
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

	result := make([]int, len(searchRoutes[minIndex]))
	for i := range searchRoutes[minIndex] {
		result[i] = searchRoutes[minIndex][i].block.Number
	}

	// Return minimized route
	return result
}

func (r *RouteCalculator) getNextBlocks(last common.Block, block common.Block, trainDir common.TrainDirection, line common.Line) []newBlock {
	hasSwitch, trackSwitch := r.IsSwitchBlock(block.Number, line)
	nextBlocksIDs := make([]int, 0)
	nextBlockDirs := make([]common.TrainDirection, 0)

	switch block.Direction {
	case common.BLOCKDIRECTION_BIDIRECTIONAL:
		if trainDir == common.TRAINDIRECTION_ASCENDING {
			if hasSwitch && (trackSwitch.Side == common.BLOCKSIDE_ASCEND) {
				nextSwitchBlocks := trackSwitch.GetNextBlocks(block.Number)
				for i := range nextSwitchBlocks {
					if nextSwitchBlocks[i] == last.Number {
						nextBlocksIDs = append(nextBlocksIDs, block.Number+1)
						nextBlockDirs = append(nextBlockDirs, trainDir)
					} else if nextSwitchBlocks[i] < block.Number || block.Number == 0 {
						nextBlockDirs = append(nextBlockDirs, common.TRAINDIRECTION_DESCENDING)
						nextBlocksIDs = append(nextBlocksIDs, nextSwitchBlocks[i])
					} else {
						nextBlockDirs = append(nextBlockDirs, trainDir)
						nextBlocksIDs = append(nextBlocksIDs, nextSwitchBlocks[i])
					}
				}
			} else {
				nextBlocksIDs = append(nextBlocksIDs, block.Number+1)
				nextBlockDirs = append(nextBlockDirs, trainDir)
			}
		} else if trainDir == common.TRAINDIRECTION_DESCENDING {
			if hasSwitch && (trackSwitch.Side == common.BLOCKSIDE_DESCEND) {
				nextSwitchBlocks := trackSwitch.GetNextBlocks(block.Number)
				for i := range nextSwitchBlocks {
					if nextSwitchBlocks[i] == last.Number {
						nextBlocksIDs = append(nextBlocksIDs, block.Number-1)
						nextBlockDirs = append(nextBlockDirs, trainDir)
					} else if nextSwitchBlocks[i] > block.Number {
						nextBlockDirs = append(nextBlockDirs, common.TRAINDIRECTION_ASCENDING)
						nextBlocksIDs = append(nextBlocksIDs, nextSwitchBlocks[i])
					} else {
						nextBlockDirs = append(nextBlockDirs, trainDir)
						nextBlocksIDs = append(nextBlocksIDs, nextSwitchBlocks[i])
					}
				}
			} else {
				nextBlocksIDs = append(nextBlocksIDs, block.Number-1)
				nextBlockDirs = append(nextBlockDirs, trainDir)
			}
		}
	case common.BLOCKDIRECTION_ASCENDING:
		if hasSwitch && (trackSwitch.Side == common.BLOCKSIDE_ASCEND) {
			nextSwitchBlocks := trackSwitch.GetNextBlocks(block.Number)
			for i := range nextSwitchBlocks {
				if nextSwitchBlocks[i] == last.Number {
					nextBlocksIDs = append(nextBlocksIDs, block.Number+1)
					nextBlockDirs = append(nextBlockDirs, trainDir)
				} else if nextSwitchBlocks[i] < block.Number {
					nextBlockDirs = append(nextBlockDirs, common.TRAINDIRECTION_DESCENDING)
					nextBlocksIDs = append(nextBlocksIDs, nextSwitchBlocks[i])
				} else {
					nextBlockDirs = append(nextBlockDirs, trainDir)
					nextBlocksIDs = append(nextBlocksIDs, nextSwitchBlocks[i])
				}
			}
		} else {
			nextBlocksIDs = append(nextBlocksIDs, block.Number+1)
			nextBlockDirs = append(nextBlockDirs, trainDir)
		}
	case common.BLOCKDIRECTION_DESCENDING:
		if hasSwitch && (trackSwitch.Side == common.BLOCKSIDE_DESCEND) {
			nextSwitchBlocks := trackSwitch.GetNextBlocks(block.Number)
			if trackSwitch.Source == last.Number {
				nextBlocksIDs = append(nextBlocksIDs, block.Number-1)
				nextBlockDirs = append(nextBlockDirs, trainDir)
			} else {
				for i := range nextSwitchBlocks {
					if nextSwitchBlocks[i] > block.Number {
						nextBlockDirs = append(nextBlockDirs, common.TRAINDIRECTION_ASCENDING)
						nextBlocksIDs = append(nextBlocksIDs, nextSwitchBlocks[i])
					} else {
						nextBlockDirs = append(nextBlockDirs, trainDir)
						nextBlocksIDs = append(nextBlocksIDs, nextSwitchBlocks[i])
					}
				}
			}
		} else {
			nextBlocksIDs = append(nextBlocksIDs, block.Number-1)
			nextBlockDirs = append(nextBlockDirs, trainDir)
		}
	}

	nextBlocks := make([]newBlock, len(nextBlocksIDs))
	for i := range nextBlocksIDs {
		nextBlocks[i] = newBlock{
			block:     line.Blocks.Get(nextBlocksIDs[i]),
			searchDir: nextBlockDirs[i],
		}
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
