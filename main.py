import time
import datetime
def game_intro():
    print("===THE PASSWORD GAME===")
    time.sleep(2)
    print("-Your password must meet all requirments-")
    time.sleep(2)
    print("-Work through each step wisely-")
    time.sleep(2)
    print("-steps will be skiped over if already completed-")
    time.sleep(2)
    print("-so start simple, and work with the game-")
    time.sleep(2)
    print("-have fun-")
    time.sleep(2)

game_intro()

while True:
    pass_foundation = input("Enter your password: ")
    length_0 = len(pass_foundation) >= 8
    length_1 = len(pass_foundation) <= 14
    upper = any(char.isupper() for char in pass_foundation)
    lower = any(char.islower() for char in pass_foundation)
    number = any(char.isnumeric() for char in pass_foundation)
    special = any(not char.isalnum() for char in pass_foundation)
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    month_is = any(month in pass_foundation.lower() for month in months)
    day_is = any(day in pass_foundation.lower() for day in days)
    roman_numeral = ["M","X","I","V","M","C","L","D"]
    roman_numeral_is = any(roman_num in pass_foundation for roman_num in roman_numeral)
    if length_0 and length_1 and upper and lower and number and special and month_is and day_is and roman_numeral_is:
        print(f"\n*Password successfully created*\n\n-Your password: {pass_foundation}")
        break
    elif not length_0:
        print("\n-Password must contain at least 8 characters: \n")
    elif not length_1:
        print("\n-Password must contain below 14 characters: \n")
    elif not upper:
        print("\n-Password must contain at least 1 uppercase letter: \n")
    elif not lower:
        print("\n-Password must contain at least 1 lowercase letter: \n")
    elif not number:
        print("\n-Password must contain at least 1 number: \n")
    elif not special:
        print("\n-Password must contain at least 1 special character: \n")
    elif not month_is:
        print("\n-Password must contain a month of the year: \n")
    elif not day_is:
        print("\n-Password must contain a week day: \n")
    elif not roman_numeral_is:
        print("\n-Password must contain a roman numeral: \n ")
    else:
        break



