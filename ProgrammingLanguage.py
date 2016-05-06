class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        is_dynamic = False
        if self.typing == "Dynamic":
            is_dynamic = True
            return is_dynamic
        return is_dynamic
    def __str__(self):
        return self.name
