import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.css']
})
export class TodosComponent implements OnInit {
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
