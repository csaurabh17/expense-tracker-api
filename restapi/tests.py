# from django.test import TestCase
from unittest import TestCase

# Create your tests here.


def sum(a, b):
    return a + b


class TestClass(TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
