while True:
    pass_foundation = input("Enter your password: ")

    length = len(pass_foundation)>= 10
    upper = any(char.isupper() for char in pass_foundation)
    lower = any(char.islower() for char in pass_foundation)
    number = any(char.isnumeric() for char in pass_foundation)
    special = any(not char.isalnum() for char in pass_foundation)

    if length and upper and lower and number and special:
        print(f"\n*Password succsesfully created*\n\n-Your password: {pass_foundation}")
        break
    elif not length:
        print("\n-Password must be at least 10 characters long: \n")
    elif not upper:
        print("\n-Password must have at least 1 uppercase letter: \n")
    elif not lower:
        print("\n-Password must have at least 1 lowercase letter: \n")
    elif not number:
        print("\n-Password must have at least 1 number: \n")
    elif not special:
        print("\n-Password must have at least 1 special character: \n")
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



