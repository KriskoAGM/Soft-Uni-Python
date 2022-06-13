def length(password):
    if 6 <= len(password) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def letters_and_digits(password):
    if password.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def digits(password):
    digit_counter = 0
    for x in password:
        if x.isdigit():
            digit_counter += 1
    if digit_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


some_password = input()
is_valid = [length(some_password), letters_and_digits(some_password), digits(some_password)]

if all(is_valid):
    print('Password is valid')