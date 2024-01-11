import re
import uuid

from custom_exceptions import alt_raise, WrongNameABaseQLException


class ParentALTBase(object):
    DATABASE_NAME_PATTERN = r"[a-zA-D0-9-_\.]"

    def __init__(self):
        self.db_id = self.generate_db_id()

    def generate_db_id(self):
        # The logic of generating Database id may change,
        # so the function should stay
        return uuid.uuid4()


class ALTBase(ParentALTBase):
    def __init__(self):
        super().__init__()
        self._name: str | None = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, user_input: str):
        if not re.match(self.DATABASE_NAME_PATTERN,
                        user_input):
            alt_raise(exception=WrongNameABaseQLException)
        else:
            self._name = user_input
            print(
                f"Database {self._name} was created with assigned id of {self.db_id}")


alt_base = ALTBase()
alt_base.name = "my-alt_base"
