import { Component } from '@angular/core';
import { interval } from 'rxjs';
import { CtcService } from '../services/ctc.service';

@Component({
  selector: 'app-ctc-lines',
  templateUrl: './ctc-lines.component.html',
  styleUrls: ['./ctc-lines.component.css']
})
export class CTCLinesComponent {
  lines: string = "";

  constructor(
    private backend: CtcService
  ) {}

  ngOnInit() {
    this.getData();

    interval(250).subscribe(() => this.getData());
  }

  getData() {
    this.backend.getLines().subscribe(lines => this.lines = lines);
  }

}
