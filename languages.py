from ProgrammingLanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print("{}, {} Typing, Reflection={}, First appeared in {}.".format(python.name, python.typing, python.reflection, python.year))

print("The dynamically typed languages are:")
for language in ruby, python, vb:
    if language.is_dynamic():
        print(language.name)


