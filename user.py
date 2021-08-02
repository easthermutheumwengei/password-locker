import random
import string


class Credentials:
    '''
    Class to generate credentials for different accounts.
    '''
    accounts_list = []
    user_accounts = []


def __init__(self, account_name, email, username, password, user):
    """__init__ method to help use define the properties of our credentials objects.

        Args:
            account_name (string): New name of the credential account.
            email (string): New email address associated with that credential.
            username (string): New username for that credential.
            password (string): New password.
            user ([string]): Current logged in user.
        """
    self.account_name = account_name
    self.email = email
    self.username = username
    self.password = password
    self.user = user

    def save_account(self):
        """save_account method saves credential objects into accounts_list
    """
    Credentials.accounts_list.append(self)


@classmethod
def generate_pw(cls, pw_length):
    """generate_pw method that generates a random password.

    Args:
        pw_length (number): Length of generated password.

    Returns:
        string: Return the generated password.
    """
    pw = ''.join(random.choice(string.ascii_letters) for i in range(pw_length))
    return pw
