import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
 
@Injectable({
  providedIn: 'root'
})
export class TodosApiService {
 
  private baseUrl = 'http://127.0.0.1:8000/api/tasks';
 
  constructor(private http: HttpClient) { }

  getTodosList(): Observable<any> {
    return this.http.get(`${this.baseUrl}/`);
  }
 
  // getTodo(id: number): Observable<object> {
  //   return this.http.get(`${this.baseUrl}/${id}`);
  // }
 
  // createTodo(todo: Object): Observable<object> {
  //   return this.http.post(`${this.baseUrl}/`, todo);
  // }
 
  // updateTodo(id: number, value: any): Observable<object> {
  //   return this.http.put(`${this.baseUrl}/${id}`, value);
  // }
 
  // deleteTodo(id: number): Observable<any> {
  //   return this.http.delete(`${this.baseUrl}/${id}`);
  // }  
 
  // getTodosByCompleted(age: number): Observable<any> {
  //   return this.http.get(`${this.baseUrl}/age/${age}/`);
  // }
 
  deleteAll(): Observable<any> {
    return this.http.delete(`${this.baseUrl}/`);
  }
}