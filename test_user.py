import unittest
from unittest.case import TestCase

from user import Credential, User


class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the credentials class behaviours.


Args:
      unittest(TestCase):TestCase class that helps in creating test cases.
      """

    def setUp(self):
        """
        setUp method to run before each test cases
        """
