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
11. Implemented <code>LBYL and EAFP</code> in my code.<br>
    - <code>Look Before You Leap - LBYL</code><br>
        - My code checks if files and directories exist before accessing them (e.g., checking os.path.exists() before opening a file).Implemented [here](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/app/plugins/history/__init__.py)<br>
        - Example: In <code>history/__init__.py</code>, before opening <code>history.csv</code>, we check if it exists to avoid an error.<br>
    - <code>Easier to Ask for Forgiveness than Permission - EAFP</code><br>
        - Instead of checking conditions, my code tries to execute actions and catches exceptions if they fail (e.g., <code>try/except</code>).Implemented [here](https://github.com/JaswanthKSnjit/IS601-Mid-Term/blob/main/app/commands/__init__.py)<br>
        - Example: In <code>execute_command()<code>, the program assumes the command exists and catches KeyError if it doesn’t.<br>
