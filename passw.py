MIN_LENGTH = 2
MAX_LENGTH = 6
MIN_LOWER = 1
MIX_UPPER = 1
MIN_NUMBERS = 1
SPECIAL_CHAR = "!#"
# 0431628611 - NOTON
password_length = False
password_valid = False
password_special = False

while not password_valid:
    password = input("Please enter a valid password")
    if MAX_LENGTH >= len(password) >= MIN_LENGTH:
        password_length = True
    if SPECIAL_CHAR in password:
        password_special = True
    if password_special:
        password_valid = True

print("Password Valid.")

