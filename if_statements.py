# is_hot = False
# is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

# house_price = 1000000
# has_good_credit = True

# if has_good_credit:
#     down_payment = 0.1 * house_price
# else:
#     down_payment = 0.2 * house_price
# print(f"Down payment: ${down_payment}")


# Conditions
# has_high_income = True
# # has_good_credit = True
# has_criminal_record = False

# if has_high_income and not has_criminal_record:
#     print("Eligible for loan!")

# temperature = 35

# if temperature == 30:
#     print("it's a hot day")
# else:
#     print("It's not a hot day")

# name = "J"

# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50:
#     print("name must be a maximum of 50 characters")
# else:
#     print("name looks good!")

# building a guessing game
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('you won!')
#         break
# else:
#     print("The guess didn't work!")
    
# building a car game
command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car started")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    else:
        print("sorry, i don't understand that")