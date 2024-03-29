import { DatePipe, formatDate, Time } from '@angular/common';
import { Component, LOCALE_ID, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AbstractControl, FormGroup, FormBuilder, FormControl, Validators, FormArray} from '@angular/forms';
import { Train } from '../models/train';
import { TrainStop } from '../models/trainStop';
import { BackendService } from '../services/backend.service';
import { TrainLocation } from '../models/trainLocation';

@Component({
  selector: 'app-train-dispatch',
  templateUrl: './train-dispatch.component.html',
  styleUrls: ['./train-dispatch.component.css']
})
export class TrainDispatchComponent implements OnInit {
  stations: string[] = [];
  lines: string[] = ["Red", "Green"];

  id: number = 0;
  line: string = this.lines[0];
  driver: string = '';
  stops: TrainStop[] = new Array<TrainStop>();
  stationSelect: boolean[] = [];
  stationTimes: Date[] = [];


  constructor(
    private backend: BackendService,
    private router: Router
  ) {}

  ngOnInit() {
    this.getData()

    for (let i = 0; i < this.stations.length; i++) {
      this.stationTimes[i] = new Date()
    }
  }

  setLine(line: string): void {
    this.line = line;
    this.getData();
  }

  getData(): void {
    this.backend.getStations(this.line).subscribe(stations => this.stations = stations);
    this.backend.getNextTrainID().subscribe(id => this.id = id);
  }

  getStops(): void {
    for (let index = 0; index < this.stations.length; index++) {
      if (this.stationSelect[index] == true) {
        this.stops.push(new TrainStop(this.stations[index], formatDate(this.stationTimes[index], 'yyyy-MM-ddTHH:mm:ssZ', 'en-US')));
      }
    }
  }

  onSubmit() {
    this.getStops()
    let location = new TrainLocation([0]);
    let train = new Train(this.id, this.line, this.driver, location, this.stops);
    console.warn(train)
    this.backend.postTrain(train).subscribe();
    this.router.navigateByUrl('/trains')
  }
}
