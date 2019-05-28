import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map, catchError } from 'rxjs/operators';

import { Todo } from './todo';

@Injectable({
  providedIn: 'root'
})
export class TodosApiService {

  private baseUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) { }

  // API: GET http://127.0.0.1:8000/api/tasks/
  public getAllTodos(): Observable<any> {
    return this.http
      .get(this.baseUrl + '/tasks/').pipe(
        map(response => {
          const todos = response;
          // console.dir(todos);
          // return todos.map((todo) => new Todo(todo));
          return todos;
        }),
        catchError(this.handleError),
      )
  }

  // API: POST http://127.0.0.1:8000/api/tasks/
  createTodo(todo: Todo): Observable<any> {
    console.dir(todo);

    return this.http
    .post(`${this.baseUrl}/tasks/`, todo)
    .pipe(map(response => {
      console.dir(response);
      return response;
    }))
  }

  // getTodo(id: number): Observable<object> {
  //   return this.http.get(`${this.baseUrl}/${id}`);
  // }

  // updateTodo(id: number, value: any): Observable<object> {
  //   return this.http.put(`${this.baseUrl}/${id}`, value);
  // }

  deleteTodo(id: number): Observable<any> {
    return this.http.delete(`${this.baseUrl}/task/${id}/`);
  }

  // getTodosByCompleted(age: number): Observable<any> {
  //   return this.http.get(`${this.baseUrl}/age/${age}/`);
  // }

  deleteAll(): Observable<any> {
    return this.http.delete(`${this.baseUrl}/`);
  }

  private handleError (error: Response | any) {
    console.error('ApiService::handleError', error);
    return Observable.throw(error);
  }
}