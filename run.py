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


def create_user(fname, lname, uname, pw):
    """Function for creating new user.
    """
    new_user = User(fname, lname, uname, pw)
    return new_user


def save_user(user):
    """Save user.
    """
    user.save_user()


def user_login(uname, pw):
    """Function to handle user login.
    """
    return User.user_login(uname, pw)


def delete_user(user):
    """Function to remove user.
    """
    user.delete_user()
