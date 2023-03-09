import { Component } from '@angular/core';
import { interval } from 'rxjs';
import { Block } from '../models/block';
import { BackendService } from '../services/backend.service';

@Component({
  selector: 'app-block-table',
  templateUrl: './block-table.component.html',
  styleUrls: ['./block-table.component.css']
})
export class BlockTableComponent {
  lines: string[] = ["Red", "Green"];
  line: string = this.lines[0];
  blocks: Block[] = [];

  constructor(
    private backend: BackendService
  ) {}

  ngOnInit() {
    this.getBlocks();

    interval(30*1000).subscribe(() => this.getBlocks())
  }

  setLine(line: string) {
    this.line = line;

    this.getBlocks();
  }

  putBlockOpen(block: number, open: boolean) {
    this.backend.putBlockOpen(this.line, block, open).subscribe();

    this.getBlocks();
  }

  getBlocks() {
    this.backend.getBlocks(this.line).subscribe(blocks => this.blocks = blocks);
  }
}
