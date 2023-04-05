import { DecimalPipe } from "@angular/common";

export class Block {
  constructor(
    public number: number,
    public line: string,
    public section: string,
    public length: string,
    public signal: string,
    public occupied: boolean,
    public suggestedspeed: number,
    public authority: number,
    public open: boolean,
  ) {  }

}
