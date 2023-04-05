import random
import string

def password_generate(min_length, numbers=True, speccial_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if speccial_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if speccial_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Minimum karakter uzunluğunu yazığ enter tıklayınız: "))
has_number = input("Şifre içerisinde rakam olsun mu (y/n)? ").lower() == "y"
has_special = input("Şifre içerisinde özel karakter olsun mu (y/n)? ").lower() == "y"
pwd = password_generate(min_length, has_number, has_special)

print("Şifreniz : ", pwd)