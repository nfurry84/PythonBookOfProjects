"""this module contains pytest functions"""
import main

def test_mytest():
    """initial test"""
    assert 2+2 == 4

def test_main_values():
    """Test main values output"""
    assert main.CONF != ''
    assert main.KEY != ''