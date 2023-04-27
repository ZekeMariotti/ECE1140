import { Component } from '@angular/core';
import { BackendService } from '../services/backend.service';
import { interval } from 'rxjs';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  lines: string[] = ["Red", "Green"];
  throughput: number[] = [];

  constructor(
    private backend: BackendService
  ) {}

  ngOnInit() {
    this.getData()

    interval(300).subscribe(() => this.getData());
  }

  getData() {
    for (let index = 0; index < this.lines.length; index++) {
       this.backend.getThroughput(this.lines[index]).subscribe((throughput: number) => this.throughput[index] = throughput);
    }
  }
}
