"""This module contains exceptions used in malconstrict """


class UserNotFoundException(Exception):
    """Exception thrown when no user exists in MAL database."""
    pass


class EntryNotFoundException(Exception):
    """Exception thrown when an entry is not found in MAL database."""
    pass


class NotInListException(Exception):
    """Exception thrown when an entry is not found in a user's list."""
    pass


class BadAuthenticationException(Exception):
    """Exception thrown when authentication token is bad or missing."""
    pass


class NotYetImplementedException(Exception):
    """Exception thrown when an unimplemented function is called."""
    pass
