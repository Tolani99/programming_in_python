import additions
import pytest

def test_add():
    assert additions.add(4, 5) == 9

def test_sub():
    assert additions.sub(4, 5) == -1