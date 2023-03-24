import { DecimalPipe } from "@angular/common";

export class Block {
  constructor(
    public number: number,
    public line: string,
    public section: string,
    public length: DecimalPipe,
    public signal: string,
    public occupied: boolean,
    public suggestedspeed: DecimalPipe,
    public authority: number,
    public open: boolean,
  ) {  }

}
