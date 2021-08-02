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
            'Twitter', 'esthermutheu99@gmail.com', '_dylandaxy', 'p@$$w0rD', 'dylan')
        self.account2 = Credentials(
            'Gmail', 'esthermutheu99@gmail.com', 'rass', 'l0v3_L33', 'haddasah')

        def tearDown(self):
            """tearDown method that does clean up after each test case has run.
        """
        Credentials.accounts_list = []

        def test_init(self):
            """test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.account1.account_name, 'Twitter')
        self.assertEqual(self.account1.email, 'esthermutheu99@gmail.com')
        self.assertEqual(self.account1.username, '_dylandaxy')
        self.assertEqual(self.account1.password, 'p@$$w0rD')
        self.assertEqual(self.account1.user, 'dylan')

        def test_save_account(self):
            """test_save_account test case to test if the credential object is saved into the credentials list
        """
        self.account1.save_account()
        self.account2.save_account()

        self.assertEqual(len(Credentials.accounts_list), 2)
        self.assertEqual(Credentials.accounts_list[0].account_name, 'Twitter')
