import pytest
import convertor_roman_int
import list_wrong_input_1
import list_wrong_input_2
import dict_right_input


def test_right_input_of_roman_number_is_valid():
    for key, value in dict_right_input.right_input.items():
        print(value)
        assert convertor_roman_int.convert_roman_to_int(value) == key


def test_wrong_input_1_of_roman_number_is_valid():
    for wrong in list_wrong_input_1.wrong_input:
        print(wrong)
        with pytest.raises(ValueError):
            convertor_roman_int.convert_roman_to_int(wrong)


def test_wrong_input_2_of_roman_number_is_valid():
    for wrong in list_wrong_input_2.wrong_input:
        print(wrong)
        with pytest.raises(ValueError):
            convertor_roman_int.convert_roman_to_int(wrong)
