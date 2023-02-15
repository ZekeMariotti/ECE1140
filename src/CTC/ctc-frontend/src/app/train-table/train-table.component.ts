import { Component, Directive, EventEmitter, Input, Output, QueryList, ViewChildren } from '@angular/core';
import { DecimalPipe, NgFor } from '@angular/common';
import { Train } from '../train';
import { BackendService } from '../backend.service';

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
  }

  private getData(): void {
    this.backendService.getTrains().subscribe(trains => this.trains = trains);
  }
}
