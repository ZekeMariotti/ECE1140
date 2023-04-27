import { Component } from '@angular/core';
import { interval, repeat, Subscription } from 'rxjs';
import { BackendService } from '../services/backend.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  currentTime: Date = new Date();

  constructor(
    private backendService: BackendService
  ) {}

  ngOnInit(): void {
    this.backendService.getTime()
    this.getTime();

    interval(100).subscribe(() => {this.getTime()});
  }

  getTime(): void {
    this.backendService.getTime().subscribe(time => this.currentTime = time);
  }
}
