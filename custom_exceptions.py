
# Not Standard Python Exceptions, as ALTBase is going
# to have its own ala Language, so it
# needs its own Exceptions


class BaseALTBaseQLException:
    ...


class SyntaxABaseQLException(BaseALTBaseQLException):
    ...


class WrongNameABaseQLException(BaseALTBaseQLException):
    ...


def alt_raise(exception: BaseALTBaseQLException):
    print("Some Exception of ALTBaseQL was raised")
