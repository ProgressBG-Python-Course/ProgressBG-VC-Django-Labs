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
  todoArray=[];

  addItem(value){
    this.todoArray.push(value)
    console.log(this.todoArray)
  }
  // to submit item with enter, not only  with add btn click
  todoSubmit(form:any){
    let value = form.value;
    if(value!==""){
      this.todoArray.push(value.todo);  
      form.resetForm();   
    }else{
      alert('Field required **')
    }    
  }

  deleteItem(todo){
    this.todoArray.forEach( (item, i) => {
      if(item === todo){
       this.todoArray.splice(i,1)
      }
    })
  }

  constructor() { }

  ngOnInit() {
  }

}
