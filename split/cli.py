import yaml
from todo      import Todo
from todo_list import TodoList

class CLI:

    def __init__(self, options_file, todo_list):
        self.todo_list = todo_list

        with open(options_file, 'r') as options:
            self.options = yaml.load(options)

    def execute(self, key):
        # command = self.options.get(key, "h")['command']
        if key == "a":
            print "Description: "
            description = raw_input()
            todo        = Todo(description)
            self.todo_list.add_todo(todo)
        elif key == "v":
            print self.todo_list
        elif key == "h":
            print self.menu()
        elif key == "q":
            quit()

    def is_valid(self, entry):
        return entry in self.options.keys()

    def menu(self):
        menu = []
        for i, option in enumerate(self.options.items()):
            key         = option[0]
            description = option[1]["description"]
            row         = key + ": " + description + "\n"

            menu.append(row)

        return "".join(menu)
