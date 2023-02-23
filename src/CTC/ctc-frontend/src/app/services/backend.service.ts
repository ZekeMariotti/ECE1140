import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, Observable } from 'rxjs';
import { Train } from '../models/train';
import { Block } from '../models/block';
import { environment } from '../../environments/environment';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
  })
};

@Injectable({
  providedIn: 'root'
})
export class BackendService {
  readonly headers = new HttpHeaders().set('Content-Type', 'application/json');



  constructor(
    private http: HttpClient
  ) { }

  getTrains(): Observable<Train[]> {
    return this.http.get<Train[]>(`${environment.api_be}/api/frontend/trains`, {responseType: 'json'});
  }

  getTime(): Observable<Date> {
    return this.http.get<Date>(`${environment.api_be}/api/frontend/time`, {responseType: 'json'});
  }

  getLines(): Observable<string[]> {
    return this.http.get<string[]>(`${environment.api_be}/api/frontend/lines`, {responseType: 'json'});
  }

  getBlocks(line: string): Observable<Block[]> {
    return this.http.get<Block[]>(`${environment.api_be}/api/frontend/lines/${line}/blocks`);  }

  getStations(line: string): Observable<string[]> {
    return this.http.get<string[]>(`${environment.api_be}/api/frontend/lines/${line}/stations`, {responseType: 'json'});
  }

  getSimulationSpeed(): Observable<number> {
    return this.http.get<number>(`${environment.api_be}/api/frontend/simulationspeed`, {responseType: 'json'});
  }

  putSimulationSpeed(speed: number): Observable<number> {
    return this.http.put<number>(`${environment.api_be}/api/frontend/simulationspeed`, speed, httpOptions);
  }

  postTrain(train: Train): Observable<Train> {
    return this.http.post<Train>(`${environment.api_be}/api/frontend/trains`, train, httpOptions)
  }
}
