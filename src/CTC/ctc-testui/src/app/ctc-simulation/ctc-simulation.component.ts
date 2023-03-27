import { Component } from '@angular/core';
import { interval } from 'rxjs';
import { CtcService } from '../services/ctc.service';

@Component({
  selector: 'app-ctc-simulation',
  templateUrl: './ctc-simulation.component.html',
  styleUrls: ['./ctc-simulation.component.css']
})
export class CTCSimulationComponent {
  simulation: string = "";

  constructor(
    private backend: CtcService
  ) {}

  ngOnInit() {
    this.getData();

    interval(250).subscribe(() => this.getData());
  }

  getData() {
    this.backend.getSimulation().subscribe(sim => this.simulation = sim);
  }

}
