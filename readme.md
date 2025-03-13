<h1 align="center"> IS601 Mid Term - Advance Calculator</h1>

## Setup Instructions

1. Clone Repo: <code> git clone git@github.com:JaswanthKSnjit/IS601-Mid-Term </code>
2. Navigate to project directory <code> cd IS601-Mid-Term</code>
3. Create a Python Virtual Environments <code> python -m venv venv </code>
4. Activate Python Virtual Environments <code> source venv/bin/activate </code>
5. Install dependencies <code> pip install -r requirements.txt </code>
6. Install faker <code> pip install faker </code>
7. Install faker requirements <code> pip freeze > requirements.txt </code>
8. To run the program <code> python main.py </code>
9. Running basic tests <code> pytest tests</code>
10. Faker generated random tests <code> pytest tests --num_records=100 </code>
11. For full debug output <code> pytest tests --num_records=10 -v -s </code>
