import { Component } from '@angular/core';
import { interval } from 'rxjs';
import { BackendService } from '../services/backend.service';

@Component({
  selector: 'app-simulation-controls',
  templateUrl: './simulation-controls.component.html',
  styleUrls: ['./simulation-controls.component.css']
})
export class SimulationControlsComponent {
  speed: number = 1

  constructor(
    private backend: BackendService
  ) {}

  ngOnInit() {
    this.getSpeed();

    interval(500).subscribe(() => this.getSpeed());
  }

  speedChanged(e: any) {
    console.warn(this.speed);
    this.setSpeed();
  }

  getSpeed() {
    this.backend.getSimulationSpeed().subscribe(speed => this.speed = speed);
  }

  setSpeed() {
    this.backend.putSimulationSpeed(this.speed).subscribe();
  }
}
