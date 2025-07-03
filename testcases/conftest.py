# conftest.py
import pytest
from pyjavaproperties import Properties
import os
from page_object_model.testresources import constants

# Corrected path for environment.properties
# Go up one level from 'testcases' to 'page_object_model', then into 'testresources'
current_dir = os.path.dirname(os.path.abspath(__file__)) # This is ...\testcases
parent_dir = os.path.dirname(current_dir) # This is ...\page_object_model

properties_file_path = os.path.join(parent_dir, 'testresources', 'environment.properties')

@pytest.fixture(scope='session')
def base_fixture():
    prod = Properties()
    try:
        with open(properties_file_path, 'r', encoding='utf-8') as fp:
            prod.load(fp)
    except FileNotFoundError:
        pytest.fail(f"Properties file not found at: {properties_file_path}")
    except Exception as e:
        pytest.fail(f"Error loading properties: {e}")

    yield prod