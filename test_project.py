from project import validate_menu_choice,is_valid_int,error
import pytest
from utils import format_duration,average

#Apparently I did all the functional part in the different modules, and project.py is just a integration and menu layer.
#These were just some helper functions i made for menu hope it works.
#I doubt that i even have 3 testable functions. But if you accept test for functions in other files i have some which i'll include at bottom of this file(only some not all).

def test_is_valid_int():
    #is_valid_int function is exclusive to my functions, It only accepts positive integers.
    #On entering Negative integer or Zero it raises ValueError(We can change the specific error message by using custom_error argument.)
    assert is_valid_int(5) == 5
    assert is_valid_int(9) == 9
    assert is_valid_int(5.0) == 5
    assert is_valid_int("10") == 10
    with pytest.raises(ValueError):
        is_valid_int(0)
    with pytest.raises(ValueError):
        is_valid_int(-1)
    with pytest.raises(ValueError,match = "The number cannot be negative or zero."):
        is_valid_int(-7)
    with pytest.raises(ValueError,match="This function does not accept zero."):
        is_valid_int(0,"This function does not accept zero.")
    with pytest.raises(ValueError,match="\'custom_error\' cannot be empty."):
        is_valid_int(-29,"")
    
def test_validate_menu_choice(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda _: "3")
    assert validate_menu_choice(5) == 3
    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert validate_menu_choice(5) == 1
    monkeypatch.setattr("builtins.input", lambda _: "5")
    assert validate_menu_choice(5) == 5
    monkeypatch.setattr("builtins.input", lambda _: "10")
    assert validate_menu_choice(5) is None
    monkeypatch.setattr("builtins.input", lambda _: "hello")
    assert validate_menu_choice(5) is None
    
def test_error():
    assert error("Hello world") is None
    assert error(ValueError("Invalid Value")) is None
    with pytest.raises(ValueError, match="\'message\' is a required argument."):
        error("")
        
#This were the 3 functions.
#Now some other  helper functions from other file.

def test_average():
    assert average([10, 20, 30]) == 20
    assert average([5, 5, 5]) == 5
    assert average([1, 2, 3, 4]) == 2.5
    with pytest.raises(ZeroDivisionError):
        average([])
        
def test_format_duration():
    assert format_duration(60) == "1m "
    assert format_duration(3600) == "1h "
    assert format_duration(3661) == "1h 1m 1s "
    assert format_duration(7325) == "2h 2m 5s "
    assert format_duration(59) == "59s "
    with pytest.raises(ValueError, match="Duration must be a numeric value in seconds."):
        format_duration("hello")
        
#Hope it works.!