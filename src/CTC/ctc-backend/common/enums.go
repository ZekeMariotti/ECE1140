package common

// enums.go stores various enumerable values

type StationSide uint8

const (
	STATIONSIDE_LEFT  StationSide = 0
	STATIONSIDE_RIGHT StationSide = 1
	STATIONSIDE_BOTH  StationSide = 2
)

type BlockDirection uint8

const (
	BLOCKDIRECTION_ASCENDING     BlockDirection = 0
	BLOCKDIRECTION_DESCENDING    BlockDirection = 1
	BLOCKDIRECTION_BIDIRECTIONAL BlockDirection = 2
)

type BlockSignal string

const (
	BLOCKSIGNAL_GREEN  BlockSignal = "Green"
	BLOCKSIGNAL_YELLOW BlockSignal = "Yellow"
	BLOCKSIGNAL_RED    BlockSignal = "Red"
)
