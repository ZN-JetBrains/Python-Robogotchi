class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def from_string(cls, data):  # data => Test-test.user@email.com
        name, email = data.split("-")
        return cls(name, email)
