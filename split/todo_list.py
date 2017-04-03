from datetime  import datetime, timedelta
from todo      import Todo

class TodoList:

    def __init__(self, todos):
        self.todos = todos

    def get_todos(self):
        return self.todos

    def add_todo(self, todo):
        self.todos.append(todo)

    def split_todo(self, todo):
        pass

    def remove_todo(self, todo):
        if todo in self.todos:
            self.todos.remove(todo)
        else:
            pass

    def __str__(self):
        todos = "\n".join([str(x) for x in self.todos])
        return "\n\n" + todos + "\n\n"

    def __repr__(self):
        return __str__(self)
