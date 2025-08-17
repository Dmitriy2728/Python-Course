import pytest
from string_utils import StringUtils

@pytest.mark.parametrize (
"input_text, expected_output",
    [
        ("hello", "Hello"),
        ("Hello", "Hello"),
        ("1hello world", "1hello world"),
    ],
)
def test_string_positive(input_text, expected_output):
    Utils = StringUtils()
    assert Utils.capitalize(input_text) == expected_output

@pytest.mark.parametrize (
"input_text, expected_output",
    [
        ("   hello", "hello"),
        ("  Hello world", "Hello world"),
        ("Hello world  ", "Hello world  "),
    ],
)
def test_string_positive2(input_text, expected_output):
    Utils2 = StringUtils()
    assert Utils2.trim(input_text) == expected_output

# Позитивные проверки Функции 3.
@pytest.mark.parametrize (
"Input_string, Symbol",
    [
        ("Hello!", "H"),
        ("1234_56", "_"),
    ],
)
def test_contains(Input_string, Symbol):
    Utils3=StringUtils()
    assert Utils3.contains(Input_string, Symbol) is True
    
# Негативные проверки Функции 3.
@pytest.mark.parametrize (
"Input_string, Symbol",
    [
        ("Hello!", "R"),
        ("1234_56", "!"),
        ("Hello!", " ")
    ],
)
def test_contains2(Input_string, Symbol):
    Utils4=StringUtils()
    assert not Utils4.contains(Input_string, Symbol)


@pytest.mark.parametrize (
"Input_string, Symbol, expected_result",
    [
        ("Hello!", "H", "ello!"),
        ("1234_56", "_", "123456"),
        ("Hello!", None, "Hello!"),
        ("Hello", "R", "Hello")
    ],
)
def test_delete(Input_string, Symbol, expected_result):
    Utils5=StringUtils()
    assert Utils5.delete_symbol(Input_string, Symbol) == expected_result


