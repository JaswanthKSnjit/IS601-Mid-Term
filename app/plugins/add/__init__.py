from app.commands import Command
import logging
import csv
import os

HISTORY_FILE = "data/history.csv"  # Ensure this path is correct

class AddCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        """Perform the addition of two numbers."""
        return a + b

    def execute(self, *args, **kwargs): # pragma: no cover
        """Execute the addition command and save to history."""
        # Ensure args are converted to floats
        a, b = map(float, args)
        result = self.evaluate(a, b)  # Get the result of the addition
        logging.info(f'{a} + {b} = {result}')  # Log the operation
        print(f'{a} + {b} = {result}')  # Print the result
        
        # Automatically save to history
        self.save_to_history("add", a, b, result)

        return result  # Return the result for command history
    
    def save_to_history(self, operation, num1, num2, result): # pragma: no cover
        """Append calculation result to history.csv."""
        file_exists = os.path.exists(HISTORY_FILE)
        
        with open(HISTORY_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Operation", "Operand1", "Operand2", "Result"])  
            writer.writerow([operation, num1, num2, result])
