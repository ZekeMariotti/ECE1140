package common

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strconv"

	"github.com/shopspring/decimal"
)

// Parses the csv files
func ParseLine(pathBlocks string, pathSwitches string) *Line {
	// Define line
	l := Line{
		Name:     "",
		Blocks:   NewSafeBlockMap(),
		Switches: make([]*Switch, 0),
		Stations: make([]*Station, 0),
	}

	// Import blocks
	fBlocks, _ := os.Open(pathBlocks)
	rBlocks := csv.NewReader(fBlocks)
	blocksCSV, _ := rBlocks.ReadAll()
	defer fBlocks.Close()

	for i, v := range blocksCSV {
		// Skip header
		if i == 0 {
			continue
		}

		// Import block data
		num, _ := strconv.Atoi(v[0])
		section := v[1]
		line := v[2]
		length, _ := decimal.NewFromString(v[3])
		grade, _ := decimal.NewFromString(v[4])
		speed, _ := decimal.NewFromString(v[5])
		dir := BLOCKDIRECTION_BIDIRECTIONAL
		switch v[6] {
		case "ASC":
			dir = BLOCKDIRECTION_ASCENDING
		case "DESC":
			dir = BLOCKDIRECTION_DESCENDING
		}
		stationName := v[7]
		platformL, _ := strconv.ParseBool(v[8])
		platformR, _ := strconv.ParseBool(v[9])
		crossing, _ := strconv.ParseBool(v[10])
		underground, _ := strconv.ParseBool(v[11])
		elevation, _ := decimal.NewFromString(v[12])
		cumElevation, _ := decimal.NewFromString(v[13])

		b := Block{
			Number:              num,
			Section:             section,
			Line:                line,
			Length:              length,
			Grade:               grade,
			SpeedLimit:          speed,
			Direction:           dir,
			Elevation:           elevation,
			CumulativeElevation: cumElevation,
			Underground:         underground,
			Crossing:            crossing,
		}

		// Handle Station
		if stationName != "" {
			side := STATIONSIDE_BOTH
			if platformL && !platformR {
				side = STATIONSIDE_LEFT
			} else if !platformL && platformR {
				side = STATIONSIDE_RIGHT
			}

			b.Station = &Station{
				Name: stationName,
				Side: side,
			}
			l.Stations = append(l.Stations, b.Station)
		}

		l.Blocks.Set(b.Number, b)

		// Ensure line name is set
		if l.Name == "" {
			l.Name = line
		}
	}

	// Import switches
	fSwitch, _ := os.Open(pathSwitches)
	rSwitch := csv.NewReader(fSwitch)
	switchCSV, err := rSwitch.ReadAll()
	if err != nil {
		fmt.Println(err)
		log.Fatalln(err)
	}
	defer fSwitch.Close()

	for i, v := range switchCSV {
		// Skip header
		if i == 0 {
			continue
		}

		// Get data
		source, _ := strconv.Atoi(v[0])
		dest1, _ := strconv.Atoi(v[1])
		dest2, _ := strconv.Atoi(v[2])

		s := Switch{
			Source:       source,
			Destination1: dest1,
			Destination2: dest2,
		}
		l.Switches = append(l.Switches, &s)

		// Append switch reference to blocks switch affects
		for key, val := range l.Blocks.GetCopy() {
			if key == source || key == dest1 || key == dest2 {
				val.Switch = &s
				l.Blocks.Set(key, val)
			}
		}
	}

	return &l
}
