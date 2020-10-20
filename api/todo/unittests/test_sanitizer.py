from unittest import TestCase
from todo.sanitizer import sanitize


class TestBadWordValidation(TestCase):

    def test_safe_words(self):
        bad_title = "Buy a present for fudge judy"
        expected_title = "Buy a present for f*dge judy"

        sanitized = sanitize(bad_title)
        self.assertEqual(sanitized, expected_title)
