import logging
import csv
import os
from app.commands import Command

HISTORY_FILE = "data/history.csv"  # Ensure this path is correct

class MultiplyCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        """Perform the multiplication of two numbers."""
        return a * b

    def execute(self, *args, **kwargs):
        """Execute the multiplication command and save to history."""
        a, b = map(float, args)  # Convert inputs to float
        result = self.evaluate(a, b)  # Get the result of the multiplication
        logging.info(f'{a} x {b} = {result}')  # Log the operation
        print(f'{a} x {b} = {result}')  # Print the result

        # Automatically save to history
        self.save_to_history("multiply", a, b, result)

        return result  # Return the result for command history

    def save_to_history(self, operation, num1, num2, result):
        """Append calculation result to history.csv."""
        file_exists = os.path.exists(HISTORY_FILE)
        
        with open(HISTORY_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Operation", "Operand1", "Operand2", "Result"])  # pragma: no cover
            writer.writerow([operation, num1, num2, result])
