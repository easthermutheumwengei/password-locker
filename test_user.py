import unittest
from unittest.case import TestCase

from user import Credential, Credentials, User


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

        self.account1 = Credentials(
            'Twitter', 'esthermutheu99@gmail.com', '_esther', 'p@$$w0rD', 'haddasah')
        self.account2 = Credentials(
            'Gmail', 'esthermutheu99@gmail.com', 'rass', 'l0v3_L33', 'haddasah')

        def tearDown(self):
            """tearDown method that does clean up after each test case has run.
        """
        Credentials.accounts_list = []
