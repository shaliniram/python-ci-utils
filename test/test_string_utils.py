from app.string_utils import reverse_string, is_palindrome

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_is_palindrome_true():
    assert is_palindrome("Madam") is True

def test_is_palindrome_false():
    assert is_palindrome("OpenAI") is False
