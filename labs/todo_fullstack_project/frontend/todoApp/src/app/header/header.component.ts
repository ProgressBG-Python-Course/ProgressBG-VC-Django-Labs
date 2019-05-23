import { Component, OnInit } from '@angular/core';

@Component({
  selector: '.app-header',
  template: '<p>Header WORKS</p>',
  styles: ['p{color: "red"}']
})
export class HeaderComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  keyPresshandler(data){
    console.log(data)
  }

}
