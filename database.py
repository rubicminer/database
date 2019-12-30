#Made by rubicminer
from os import getcwd, remove as osremove


class database(object):
    database = None

    @classmethod
    def declare(cls, file):
        with open(file, "a+"):
            cls.database = file

    @classmethod
    def read(cls):
        if cls.database is not None:
            with open(cls.database, "r") as database:
                file = database.readline()
                while file:
                    print(file)
                    file = database.readline()

    @classmethod
    def write(cls, text):
        if cls.database is not None:
            with open(cls.database, "a+") as database:
                database.write(f"\n{text}")

    @classmethod
    def overwrite(cls, text):
        if cls.database is not None:
            with open(cls.database, "w") as database:
                database.write(f"\n{text}")

    @classmethod
    def clear(cls):
        if cls.database is not None:
            with open(cls.database, "w") as database:
                database.write("")

    @classmethod
    def remove(cls):
        if cls.database is not None:
            osremove(cls.database)
            cls.database = None


database.