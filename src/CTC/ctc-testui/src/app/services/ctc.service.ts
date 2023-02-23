import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, Observable } from 'rxjs';
import { environment } from '../../environments/environment.development';
import { BlockInfo } from '../models/blockinfo';
import { SwitchInfo } from '../models/switchinfo';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
  })
};

@Injectable({
  providedIn: 'root'
})
export class CtcService {

  constructor(
    private http: HttpClient
  ) { }

  getLines(): Observable<string> {
    return this.http.get<string>(`${environment.api_ctc}/ctc/lines`, httpOptions);
  }

  getSimulation(): Observable<string> {
    return this.http.get<string>(`${environment.api_ctc}/ctc/simulation`, httpOptions);
  }

  setBlocks(blocks: BlockInfo[]): Observable<BlockInfo[]> {
    return this.http.put<BlockInfo[]>(`${environment.api_ctc}/blocks`, blocks, httpOptions);
  }

  setSwitches(switches: SwitchInfo[]): Observable<SwitchInfo[]> {
    return this.http.put<SwitchInfo[]>(`${environment.api_ctc}/switches`, switches, httpOptions);
  }
}
