<h1 align="center"> IS601 Mid Term - Advance Calculator</h1>

## Setup Instructions

1. Clone Repo: <code> git clone git@github.com:JaswanthKSnjit/IS601-Mid-Term </code>
2. Navigate to project directory <code> cd IS601-Mid-Term</code>
3. Create a Python Virtual Environments <code> python -m venv venv </code>
4. Activate Python Virtual Environments <code> source venv/bin/activate </code>
5. Install dependencies <code> pip install -r requirements.txt </code>
6. Install faker requirements <code> pip freeze > requirements.txt </code>
7. To run the program <code> python main.py </code>
8. Running basic tests <code> pytest tests</code>
9. Faker generated random tests <code> pytest tests --num_records=100 </code>
10. For full debug output <code> pytest tests --num_records=10 -v -s </code>

---

## GitHub Actions

![GitHub Workflow Status](https://github.com/JaswanthKSnjit/IS601-Mid-Term/actions/workflows/test.yml/badge.svg)

Check the workflow runs [here](https://github.com/JaswanthKSnjit/IS601-Mid-Term/actions).

The workflow file is located [here](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/.github/workflows/test.yml).

---

## Demonstration Video

Watch the video demonstration [here](https://www.youtube.com/watch?v=your-video-id).

---

## Project Requirements

1. The program does basic Arithmeic operations such as <code>add, subtract, multiply, divide</code>.
2. Throws an exception when user divide a number with zero. <code>Error Message: Cannot Divide by 0!</code>.
3. Uses atleat one class, one static method and one class method.
4. All the claculation is stored in [data/history.csv](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/data/history.csv).
5. Passes [pytest](screenshots/pytest.png)
6. Passes [pylint](screenshots/pylint test.png)
7. 100% test coverage [pytestcov](screenshots/pytest cov.png)
8. Test pass with fake data generated with [faker](screenshots/faker.png). command: <code> pytest tests --num_records=100 </code> for full report we can this command: <code> pytest tests --num_records=10 -v -s </code>.
9. <code>main.py</code> is the entry point of this project, offering a command-line interface (CLI) for executing commands and interacting with the application.
10. You can access log files [here](https://github.com/JaswanthKSnjit/IS601-Mid-Term/tree/main/logs).
## Implemented LBYL and EAFP in My Code

### 🔹 Look Before You Leap (LBYL)
- My code checks if files and directories exist before accessing them (e.g., checking `os.path.exists()` before opening a file).
- **Example:** In [`history/__init__.py`](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/app/plugins/history/__init__.py), before opening `history.csv`, we check if it exists to avoid an error.

### 🔹 Easier to Ask for Forgiveness than Permission (EAFP)
- Instead of checking conditions, my code **tries to execute actions and catches exceptions** if they fail *(e.g., `try/except`)*.
- **Example:** In [`commands/__init__.py`](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/app/commands/__init__.py), the function `execute_command()` assumes that the command exists and catches `KeyError` if it doesn’t.

### ✅ Other Features
- Uses multiprocessing to enable commands to run on separate cores.
- `.env` is used to set environment variables.
- Passes GitHub Action Workflow to run [Pytests](https://github.com/JaswanthKSnjit/IS601-Mid-Term/actions).
- Design pattern is implemented all over the code.
- Documentation is available [here]().



---

## Core Functionalities

1. **Command-Line Interface (REPL)**
   - [Add](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/app/plugins/add/__init__.py): Add two numbers.
   - [Subtract](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/app/plugins/subtract/__init__.py): Subtract two numbers.
   - [Multiply](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/app/plugins/multiply/__init__.py): Multiply two numbers.
   - [Divide](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/app/plugins/divide/__init__.py): Divide two numbers
   - [History](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/data/history.csv): Calculation  history is stored in <code.history.csv</code> file.
   - [Plugins](https://github.com/JaswanthKSnjit/IS601-Mid-Term/tree/main/app/plugins): Dynamically loaded plugins.

2. **Plugin System**
   - My code has a flexible plugin system that allows seamless intergration of new commands without modifying whole code.
   - Plugins are stored [here](https://github.com/JaswanthKSnjit/IS601-Mid-Term/tree/main/app/plugins).
   - Each of these plugins are automatically detected and registered when we run the program.
   - When the user run the program with command <code>python main.py</code>, The programs asks to enter <code>menu</code> to view avaliable operations. Output screenshot can be viewed [here](/home/jasu/IS601-Mid-Term/screenshots/output.png).

3. **Calculation History Management with Pandas**
   - We use <code>pandas</code> to enable user to load, save, clear, delete history through REPL interface.
   *Command used in history*
   1. <code>history show</code> Loads all the saved calculation history on to terminal.
   2. <code>history clear</code> Clears who saved calculations.
   3. <code>history delete<n></code> Deletes particular line in history.
4. **Professional Logging Practices**
   - Logging is implemented  for operations, data manipluations, errors and information messages.
   - Log messages are also implemented based on severity <code>INFO, WARNINGS, ERROR.</code>
   - Dynamically logs configuration through environment variables for levels and output destinations.
   - Logs can be viewed [here](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/logs/app.log).

5. **Advanced Data Handling with Pandas**
   - We use pandas for data reading and writing into a CSV file.
   - The CSV file manages the history.
   - CSV file can be viewed [here](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/data/history.csv).

6. **Design Patterns for Scalable Architecture**
   *Facade Pattern*
     - Simplifies complex data operations using Pandas.
     - `HistoryCommand` class abstracts the process of **reading, saving, and clearing history** in a **single interface**, shielding users from low-level CSV operations.
     - Example in `history/__init__.py` [here](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/app/plugins/history/__init__.py).
        ```python
        class HistoryCommand(Command):
            def show_history(self):
                """Show the complete command history from CSV."""
                if not os.path.exists(self.csv_file):
                    print("No command history found.")
                    return
                df = pd.read_csv(self.csv_file)
                print(tabulate(df, headers='keys', tablefmt='pretty'))
     - The reason to use facade pattern as it provides (show_history()) to interact with CSV and Pandas operations.
    *Facade Pattern*
     - 
