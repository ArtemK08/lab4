import unittest
import sys
import os

# шлях до папки src, щоб можна було імпортувати lab4
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab4 import (
    find_substring,
    replace_substring,
    split_text,
    format_string_f,
    format_string_method,
    extract_emails,
    validate_phone_number,
    extract_hashtags,
    extract_mentions,
    count_words,
    count_sentences,
    word_frequency,
    extract_variant_data
)

class TestTextAnalyzer(unittest.TestCase):

    def test_find_substring(self):
        #Тест для функції find_substring.
        self.assertEqual(find_substring("Hello, world!", "world"), 7)
        self.assertEqual(find_substring("Hello, world!", "python"), -1)

    def test_replace_substring(self):
        #Тест для функції replace_substring.
        self.assertEqual(replace_substring("Hello, world!", "world", "Python"), "Hello, Python!")

    def test_split_text(self):
        #Тест для функції split_text.
        self.assertEqual(split_text("Hello, world!", ", "), ["Hello", "world!"])

    def test_format_string_f(self):
        #для функції format_string_f.
        self.assertEqual(format_string_f("Alice", 30), "Мене звати Alice і мені 30 років.")

    def test_format_string_method(self):
        # для функції format_string_method.
        self.assertEqual(format_string_method("Bob", 25), "Мене звати Bob і мені 25 років.")

    def test_extract_emails(self):
        #для функції extract_emails.
        text = "Contact us at info@example.com or support@tests.com"
        expected = ["info@example.com", "support@tests.com"]
        self.assertEqual(extract_emails(text), expected)

    def test_validate_phone_number(self):
        # для функції validate_phone_number.
        self.assertTrue(validate_phone_number("+380123456789"))
        self.assertFalse(validate_phone_number("12345"))

    def test_extract_hashtags(self):
        #для функції extract_hashtags.
        text = "I love #Python and #Programming"
        expected = ["#Python", "#Programming"]
        self.assertEqual(extract_hashtags(text), expected)

    def test_extract_mentions(self):
        #для функції extract_mentions.
        text = "Hello @admin and @user123"
        expected = ["@admin", "@user123"]
        self.assertEqual(extract_mentions(text), expected)

    def test_count_words(self):
        #для функції count_words.
        text = "Це тестовий рядок із п'яти слів."
        self.assertEqual(count_words(text), 7)

    def test_count_sentences(self):
        #для функції count_sentences.
        text = "Перше речення. Друге речення! Третє речення?"
        self.assertEqual(count_sentences(text), 3)

    def test_extract_variant_data(self):
        #для вилучення моделей реакторів за допомогою регулярних виразів.
        text = "Реактор моделі FR-1000 працює стабільно."
        pattern = r'\b[A-Z]{2}-\d{3,4}\b'
        self.assertEqual(extract_variant_data(text, pattern), ["FR-1000"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
