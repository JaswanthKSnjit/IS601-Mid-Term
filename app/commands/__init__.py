import csv
import os
from abc import ABC, abstractmethod

HISTORY_FILE = "data/history.csv"  # Ensure the correct path

# Define Command (Abstract Base Class)
class Command(ABC): #pragma: no cover
    @abstractmethod
    def execute(self, *args, **kwargs):
        """Abstract method to execute the command with given arguments."""
        pass

# Define CommandHandler
class CommandHandler:
    def __init__(self):
        self.commands = {}  # Dictionary to store command classes
        self.history = self.load_history()  # Load existing history to prevent duplicates

        # Ensure 'data' directory exists
        os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

    def register_command(self, command_name: str, command):
        """Registers a command with its corresponding name."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args):
        """ 
        Execute the command by its name and store results properly.
        
        Args:
            command_name (str): The name of the command (e.g., 'add', 'subtract').
            *args: The extra arguments for the command (e.g., numbers a and b).
        """
        try:
            # Handle special commands like 'menu' and 'history'
            if command_name in ["history", "menu"]:
                if command_name in self.commands:
                    self.commands[command_name].execute(*args)
                else:
                    print(f"No such command: {command_name}")
                return

            # Convert all arguments to floats for consistency
            args = [float(arg) for arg in args]

            # Execute the command and store the result
            result = float(self.commands[command_name].execute(*args))

            # Create a formatted command entry
            command_entry = [command_name, *args, result]

            # Prevent duplicate storage in memory (history)
            if command_entry not in self.history:
                self.history.append(command_entry)  # Append only if unique
                self.save_history()  # Save updated history to CSV

        except KeyError:
            print(f"No such command: {command_name}")
        except ValueError:
            print("Enter valid numbers for the operation.")
        except Exception as e:
            print(f"Error executing command '{command_name}': {e}")

    def load_history(self):
        """Load history from CSV file into memory to prevent duplicate storage."""
        history_data = []
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, mode="r", newline="") as file:
                    reader = csv.reader(file)
                    next(reader, None)  # Skip header
                    for row in reader:
                        # Convert numerical values back to float for proper comparison
                        history_data.append([row[0], float(row[1]), float(row[2]), float(row[3])])
            except Exception as e:
                print(f"Error loading history: {e}")
        return history_data

    def save_history(self): # pragma: no cover
        """Save the complete history list to CSV, ensuring no duplicate entries."""
        with open(HISTORY_FILE, mode="w", newline="") as file:  # Overwrite to prevent duplicates
            writer = csv.writer(file)
            writer.writerow(["Operation", "Operand 1", "Operand 2", "Result"])  # Write header
            for entry in self.history:
                writer.writerow(entry)  # Store only unique values
