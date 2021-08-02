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


def set_pw(pw):
    """Function to set credential password.
    """
    return Credentials.set_pw(pw)


def display_accounts(user):
    """Function that returns all credentials of logged in user.
    """
    accounts = Credentials.display_accounts(user)
    return accounts


def delete_account(account):
    """Function to delete a credential.
    """
    account.delete_account()
