import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Train } from '../train';
import { environment } from '../../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class BackendService {
  readonly headers = new HttpHeaders().set('Content-Type', 'application/json');

  constructor(
    private http: HttpClient
  ) { }

  getTrains(): Observable<Train[]> {
    return this.http.get<Train[]>(`${environment.api_be}/api/trains`, {responseType: 'json'});
  }
}
