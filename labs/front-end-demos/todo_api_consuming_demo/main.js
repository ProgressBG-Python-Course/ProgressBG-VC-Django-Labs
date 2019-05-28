function AJAX_request(url, callback){
  // create an XMLHttpRequest object
  var xhr = window.XMLHttpRequest ? new XMLHttpRequest() :
          new ActiveXObject("Microsoft.XMLHTTP");

  // initializes the request:
  xhr.open("GET", url, true);

  // EventHandler, that will be fired each time when the xhr state changes
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      callback(this.responseText);
    };
  };

  // sends the request:
  xhr.send();
}
function clickHandler(){
  var data = AJAX_request(todoListURL, processData)  
}
function processData(data){
  outputNode.innerHTML = data;
}

var todoListURL = 'http://127.0.0.1:8000/todos_rest/api/todos/'

// get btn node
var btnNode = document.getElementById('btn');
// get ouput node:
var outputNode = document.getElementById('output');

// atach click event
btnNode.addEventListener('click', clickHandler)










// python syntax:
// def clickHandler():
//   print('clickHandler')

// clickHandler()

// JS syntax:
// function clickHandler(){
//   outputNode.innerHTML = "todo list"
// }
// clickHandler();
