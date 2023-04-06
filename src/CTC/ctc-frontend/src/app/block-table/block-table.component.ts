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
  automode: boolean = false;

  constructor(
    private backend: BackendService
  ) {}

  ngOnInit() {
    this.getBlocks();
    this.getAutoMode();

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

  getAutoMode() {
    this.backend.getAutoMode().subscribe(enabled => this.automode = enabled);
  }

  putBlockAuthority(block: number, authority: number) {
    this.backend.putBlockAuthority(this.line, block, authority).subscribe();

    this.getBlocks();
  }

  putBlockSpeed(block: number, speed: number) {
    this.backend.putBlockSpeed(this.line, block, speed).subscribe();

    this.getBlocks();
  }

  putAutoMode() {
    this.backend.putAutoMode(!this.automode).subscribe();

    this.getAutoMode();
  }
}
