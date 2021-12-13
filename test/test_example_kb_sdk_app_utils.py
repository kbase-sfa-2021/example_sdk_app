import pytest
from unittest.mock import create_autospec, call
from lib.example_kb_sdk_app.utils import ExampleReadsApp



def test_era():
    era = create_autospec(ExampleReadsApp)
    era.do_analysis()
    pass