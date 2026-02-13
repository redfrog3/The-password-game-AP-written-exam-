import requests   #allows to pull info from websites
from bs4 import BeautifulSoup  #converts the html info into nice simple form

def get_wordle_solution():
    url = "https://www.tomsguide.com/news/what-is-todays-wordle-answer" #website with wordle answer
    response = requests.get(url) #gets html info containing answer
    soup = BeautifulSoup(response.text, 'html.parser') #makes html info easy to understand
    word = soup.find("p", id="b772eb30-a3e1-4c4e-a514-78aa43892bb2")\
        .find("strong")\
        .text.strip()#         line 8 and 9 finds the answer, line 10 strips surounding down just to the answer
    return word #returns the function

wordle_solution = get_wordle_solution()

while True:
    pass_foundation = input("Enter your password: ")

    length = len(pass_foundation) >= 8
    upper = any(char.isupper() for char in pass_foundation)
    lower = any(char.islower() for char in pass_foundation)
    number = any(char.isnumeric() for char in pass_foundation)
    special = any(not char.isalnum() for char in pass_foundation)
    wordle_is = wordle_solution.lower() in pass_foundation.lower()
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    month_is = any(month in pass_foundation.lower() for month in months)

    if length and upper and lower and number and special and month_is and wordle_is:
        print(f"\n*Password succsesfully created*\n\n-Your password: {pass_foundation}")
        break
    elif not length:
        print("\n-Password must contain at least 8 characters: \n")
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
    elif not wordle_is:
        print("\nPassword must contain today's wordle solution: \n")
    else:
        break



