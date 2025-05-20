

class IdentityUser:
    def __init__(self, id: str, email: str, name: str, password: str):
        self.id = id
        self.email = email
        self.name = name
        self.password = password

    def __repr__(self):
        return f"IdentityUser(id={self.id}, email={self.email}, name={self.name})"