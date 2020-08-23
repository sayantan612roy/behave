import pytest
import os

def test_logo():
    os.system('cd .. & behave features/test_logo.feature')
    print(os.getcwd())
