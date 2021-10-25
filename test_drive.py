import pytest
from drive import fdrive
import re

def test_fdrive():
    vtext = fdrive('leandro',25,21)
    assert (vtext  == 'leandro is allowed to drive')

def test_no_fdrive():
   assert fdrive('leandro',15,21) == 'leandro not allowed to drive'
