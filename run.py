#!/usr/bin/env python3.8

from user import Credentials, User


def create_account(name, emil, uname, pw, user):
    def create_account(name, email, uname, pw, user):
        """Function to create a new contact.
    """
    new_credential = Credentials(name, email, uname, pw, user)
    return new_credential


def save_account(account):
    """Function to save a credential.
    """
    account.save_account()


def generate_pw(length):
    """Function to generate a new random password.
    """
    return Credentials.generate_pw(length)
