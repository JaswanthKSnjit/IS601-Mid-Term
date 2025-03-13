"""
Pytest configuration file.

This file defines shared fixtures and command-line options for pytest.
It includes:
- A `--num_records` argument to control the number of test records.
- Fixtures for dynamically generating test data using Faker.
"""

import pytest
from faker import Faker

def pytest_addoption(parser):
    """Add custom command-line arguments for pytest."""
    parser.addoption("--num_records", action="store", default="100", help="Number of records to generate")

@pytest.fixture
def num_records(request):
    """Provide num_records as a fixture to tests."""
    return int(request.config.getoption("--num_records"))  # Convert to int

@pytest.fixture
def fake_data(num_records):
    """Generate fake data using Faker based on num_records."""
    fake = Faker()
    return [{"name": fake.name(), "email": fake.email()} for _ in range(num_records)]
