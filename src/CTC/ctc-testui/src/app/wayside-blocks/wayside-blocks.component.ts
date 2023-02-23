import { JsonPipe } from '@angular/common';
import { Component } from '@angular/core';
import { BlockInfo } from '../models/blockinfo';
import { CtcService } from '../services/ctc.service';

@Component({
  selector: 'app-wayside-blocks',
  templateUrl: './wayside-blocks.component.html',
  styleUrls: ['./wayside-blocks.component.css']
})
export class WaysideBlocksComponent {
  waysideBlocks: BlockInfo[] = JSON.parse('[{"block":1,"occupied":false,"signal":"Green"},{"block":2,"occupied":false,"signal":"Green"},{"block":3,"occupied":false,"signal":"Green"},{"block":4,"occupied":false,"signal":"Green"},{"block":5,"occupied":false,"signal":"Green"},{"block":6,"occupied":false,"signal":"Green"},{"block":7,"occupied":false,"signal":"Green"},{"block":8,"occupied":false,"signal":"Green"},{"block":9,"occupied":false,"signal":"Green"},{"block":10,"occupied":false,"signal":"Green"},{"block":11,"occupied":false,"signal":"Green"},{"block":12,"occupied":false,"signal":"Green"},{"block":13,"occupied":false,"signal":"Green"},{"block":14,"occupied":false,"signal":"Green"},{"block":15,"occupied":false,"signal":"Green"},{"block":16,"occupied":false,"signal":"Green"}]');

  constructor(
    private backend: CtcService
  ) {}

  ngOnInit() {
  }

  setData() {
    this.backend.setBlocks(this.waysideBlocks).subscribe();
  }
}
