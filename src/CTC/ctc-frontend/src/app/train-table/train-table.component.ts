import { Component, Directive, EventEmitter, Input, Output, QueryList, ViewChildren } from '@angular/core';
import { DecimalPipe, NgFor } from '@angular/common';
import { Train } from '../models/train';
import { BackendService } from '../services/backend.service';
import { interval } from 'rxjs';

@Component({
  selector: 'app-train-table',
  templateUrl: './train-table.component.html',
  styleUrls: ['./train-table.component.css']
})
export class TrainTableComponent {
  trains: Train[] = [];

  constructor(
    private backendService: BackendService
  ) {}

  ngOnInit(): void {
    this.getData();

    interval(500).subscribe(() => {this.getData()});
  }

  getData(): void {
    this.backendService.getTrains().subscribe(trains => this.trains = trains);
  }
}
