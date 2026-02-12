while True:
    pass_foundation = input("Enter your password: ")

    length = len(pass_foundation)> 5
    upper = any(char.isupper() for char in pass_foundation)
    lower = any(char.islower() for char in pass_foundation)

    if length and upper and lower:
        print(f"Password succsesfully created:\n new password {pass_foundation}")
    elif not length:
        print("Password must be at least 5 characters long: ")
    elif not upper:
        print("Password must have at least 1 uppercase letter: ")
    elif lower:
        print("Password must have at least 1 lowercase letter: ")
    else:
        break

   # pass_rule_1 = input("Your password must include an uppercase letter: ")
   # if any(char.isupper() for char in pass_rule_1):
      #  break
    #else:
        #print("Your password must include an uppercase letter: ")
    #def count_letters(word):
       # count_lower = 0
        #count_upper = 0
       # for char in pass_rule_1:
           # if char.isalpha():
           #     if char.isupper():
            #        count_upper += 1
             #   elif char.islower():
             #       count_lower +=1
            
        #if count_upper >= 1 and len(pass_foundation)< 5:
        #    print("Password must have an uppercase letter")
       # else:
         #   print("pe")



