while True:
    pass_foundation = input("Enter your password: ")
    if len(pass_foundation)< 5:
        print("Password must have at least 5 characters")
    else:
        break

while True:
    pass_rule_1 = input("Your password must include an uppercase letter: ")
    def count_letters(word):
        count_lower = 0
        count_upper = 0
        for char in pass_rule_1:
            if char.isalpha():
                if char.isupper():
                    count_upper += 1
                elif char.islower():
                    count_lower +=1
            
        if count_upper >= 1:
            print("Password must have an uppercase letter")
        else:
            print("hi")



