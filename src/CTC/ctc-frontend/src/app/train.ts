import { TrainStop } from "./trainStop";

export class Train {
  constructor(
    public id: number,
    public line: string,
    public driver: string,
    public stops: TrainStop[]
  ) {  }

}
