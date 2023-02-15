import { TrainStop } from "./trainStop";

export interface Train {
  id: number;
  line: string;
  driver: string;
  stops: TrainStop[]
}
