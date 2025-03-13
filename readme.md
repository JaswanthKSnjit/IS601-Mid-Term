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

