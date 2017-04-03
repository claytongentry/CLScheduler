from cli       import CLI
from todo_list import TodoList

OPTIONS_FILE = './options.yml'

def run(cli):
    selection = raw_input()
    if cli.is_valid(selection):
        cli.execute(selection)
    else:
        print selection + " is not a valid option.\n"

    run(cli)

if __name__ == "__main__":
    todo_list = TodoList([])
    cli       = CLI(OPTIONS_FILE, todo_list)

    print "Welcome to Split!\n--------------"
    print cli.menu()

    run(cli)
