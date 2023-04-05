package common

import (
	"strings"
	"time"
)

type StopTime struct {
	time.Time
}

func (t *StopTime) UnmarshalJSON(b []byte) error {
	layout := "2006-01-02T15:04:05-0700"

	var err error = nil
	str := strings.Trim(string(b), "\"")
	if str == "null" {
		t.Time = time.Time{}
		return nil
	}

	t.Time, err = time.Parse(layout, str)
	if err != nil {
		return err
	}

	return nil
}
