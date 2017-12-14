  //Version 5 of app for Watch and Code
  var todoList = {
    todos: [],
    displayTodos: function() {
      //if there are no todoList
      //if this.todos.length is equal to 0, or === 0
        //console.log('Your todo list is empty!')
      //else
        //print todos as normal
      if (this.todos.length === 0) {
        console.log('Your todo list is empty!');
      } else {
        console.log('My todos: ');
        for (var i = 0; i < this.todos.length; i++) {
          //removed this line here b/c it also appears in the else
            //directly below, console.log(this.todos[i].todoText);
          //check if .completed is true
            //print with (x)
            //else print with ( )
          if (this.todos[i].completed === true) {
            console.log('(x)', this.todos[i].todoText);
          } else {
            console.log('( )', this.todos[i].todoText);
          }
        }
      }
    },
    addTodo: function (todoText) {
      this.todos.push({
        todoText: todoText,
        //note, first todoText is the objects property, second is the parameter
        completed: false
      });
      this.displayTodos();
    },
    changeTodo: function (position, todoText) {
      //this.todos[position] = newValue; --from previous version
      this.todos[position].todoText = todoText;
      this.displayTodos();
    },
    deleteTodo: function (position) {
      this.todos.splice(position, 1);
      this.displayTodos();
    },
    toggleCompleted: function(position) {
      var todo = this.todos[position];
      todo.completed = !todo.completed;
      this.displayTodos();
    },
    toggleAll: function() {
      var totalTodos = this.todos.length;
      var completedTodos = 0;

      //get number of completed todoList
      for (var i=0; i<totalTodos; i++) {
        if (this.todos[i].completed===true) {
          completedTodos++;
        }
      }

      //if everything's true, make everything false
      if (completedTodos === totalTodos) {
        //make everything false
        for (var i=0; i<totalTodos; i++) {
          this.todos[i].completed = false;
        }
        //otherwise, make everything true
      } else {
        for(var i=0; i<totalTodos; i++) {
          this.todos[i].completed = true;
        }
      }

      this.displayTodos();
    }
  };
