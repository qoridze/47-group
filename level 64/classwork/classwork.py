class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name}, ასაკი: {self.age}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        return self.age
