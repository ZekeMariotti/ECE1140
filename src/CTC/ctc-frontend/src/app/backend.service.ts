import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Train } from './train';


@Injectable({
  providedIn: 'root'
})
export class BackendService {
  baseUrl: string = '/api';
  readonly headers = new HttpHeaders().set('Content-Type', 'application/json');

  constructor(
    private http: HttpClient
  ) { }

  getTrains(): Observable<Train[]> {
    return this.http.get<Train[]>(this.baseUrl+"/trains")
  }
}
