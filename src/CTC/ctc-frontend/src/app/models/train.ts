import { TrainLocation } from "./trainLocation";
import { TrainStop } from "./trainStop";

export class Train {
  constructor(
    public id: number,
    public line: string,
    public driver: string,
    public location: TrainLocation,
    public stops: TrainStop[]
  ) {  }

}
