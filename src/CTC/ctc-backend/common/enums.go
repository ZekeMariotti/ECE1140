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

type TrainDirection uint8

const (
	TRAINDIRECTION_ASCENDING  TrainDirection = 0
	TRAINDIRECTION_DESCENDING TrainDirection = 1
)

type BlockSide uint8

const (
	BLOCKSIDE_ASCEND  BlockSide = 0
	BLOCKSIDE_DESCEND BlockSide = 1
)

type BlockSignal string

const (
	BLOCKSIGNAL_GREEN  BlockSignal = "Green"
	BLOCKSIGNAL_YELLOW BlockSignal = "Yellow"
	BLOCKSIGNAL_RED    BlockSignal = "Red"
)

// Units
const (
	METERS_TO_FEET_STR string = "3.280839895"
	KMPH_TO_MPH_STR    string = "0.6213711922"
	MS_TO_MPH_STR      string = "2.23694"
	MPH_TO_MS_STR      string = "0.44704"
)
