import { Component, OnInit } from '@angular/core';

import { Observable } from 'rxjs';
import { TodosApiService } from '../todos-api.service';
import { Todo } from '../todo';

@Component({
  selector: 'app-todo-api',
  templateUrl: './todo-api.component.html',
  styleUrls: ['./todo-api.component.css']
})
export class TodoApiComponent implements OnInit {
  todos: Observable<Todo[]>;

  constructor(private todosApiService: TodosApiService) { }

  ngOnInit() {
    this.reloadData();
  }
 
  deleteAllTodos() {
    this.todosApiService.deleteAll()
      .subscribe(
        data => {
          console.log(data);
          this.reloadData();
        },
        error => console.log('ERROR: ' + error));
  }
 
  // list todos
  reloadData() {    
    this.todos = this.todosApiService.getTodosList();    
  }
}
