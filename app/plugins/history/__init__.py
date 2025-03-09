import os
import csv
import logging
import pandas as pd
from tabulate import tabulate
from app.commands import Command

# Define history file path inside 'data' folder
HISTORY_DIR = "data"
CSV_FILE = os.path.join(HISTORY_DIR, "history.csv")

# Ensure the 'data' directory exists
os.makedirs(HISTORY_DIR, exist_ok=True)

class HistoryCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler
        self.csv_file = CSV_FILE  # Use CSV file inside 'data'

    def execute(self, *args):
        """Handles history commands like show, clear, delete."""
        if len(args) == 0:
            print("Usage: history [show|clear|delete <index>]")
            return
        
        command = args[0]
        
        if command == "show":
            self.show_history()  # ✅ Ensure this method exists
        elif command == "clear":
            self.clear_history()
        elif command == "delete" and len(args) > 1:
            try:
                index = int(args[1])  # Use 1-based index
                self.delete_history_entry(index)  # Ensure this method is defined
            except ValueError:
                print("Invalid index. Usage: history delete <index>")
        else:
            print("Unknown history command.")

    def show_history(self):
        """Show the complete command history from history.csv."""
        if not os.path.exists(self.csv_file):
            print("No command history found.")
            return

        try:
            # Read history from CSV file
            df = pd.read_csv(self.csv_file)

            if df.empty:
                print("No command history found.")
            else:
                # Remove duplicate rows (if any)
                df.drop_duplicates(inplace=True)

                # Display the table with proper indexing (start from 1)
                print(tabulate(df, headers='keys', tablefmt='pretty', showindex=[i+1 for i in range(len(df))], numalign="center"))

        except Exception as e:
            print(f"Error reading history: {e}")

    def clear_history(self):
        """Clear history from memory and CSV."""
        # Clear history from memory (command_handler history list)
        self.command_handler.history = []

        # Clear the CSV file
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Operation", "Operand 1", "Operand 2", "Result"])  # Write the header row only

        logging.info("History cleared.")
        print("History cleared.")

    def delete_history_entry(self, index):
        """Delete a specific entry from history by index."""
        if not os.path.exists(self.csv_file):
            print("No command history found.")
            return

        try:
            df = pd.read_csv(self.csv_file)

            # Convert 1-based index (from user input) to 0-based index
            index = index - 1  # Subtract 1 to make the index 0-based

            # Ensure the index is within bounds
            if index < 0 or index >= len(df):
                print("Invalid index. Use 'history show' to see available entries.")
                return

            df.drop(index, inplace=True)  # Delete the row
            df.reset_index(drop=True, inplace=True)  # Reset index after deletion

            df.to_csv(self.csv_file, index=False)  # Save back to CSV
            print(f"Deleted history entry at index {index + 1}.")  # Display 1-based index

        except Exception as e:
            print(f"Error deleting history entry: {e}")
