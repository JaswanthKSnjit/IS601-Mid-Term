from app.commands import Command

class MenuCommand(Command):
    def execute(self, *args, **kwargs):
        """Execute the menu command, displaying available commands."""
        self.display_menu()

    def display_menu(self):
        """Prints the available commands in the application."""
        print("Available Commands:")
        print("-------------------")
        print("add                : add <num1> <num2> (e.g., add 5 5)")
        print("subtract           : subtract <num1> <num2> (e.g., subtract 5 5)")
        print("multiply           : multiply <num1> <num2> (e.g., multiply 5 5)")
        print("divide             : divide <num1> <num2> (e.g., divide 5 5)")
        print("history show       : Display command history")
        print("history delete <n> : Delete the n-th entry from history")
        print("history clear      : Clear the command history")
        print("exit               : Exit the application")
        print("-------------------")

# Register the MenuCommand when the application is initialized
menu_command = MenuCommand()
