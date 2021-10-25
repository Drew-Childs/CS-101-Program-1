#Drew Childs, CS101 0002, Created: 9/5/2019, Due: 9/13/2019

print("Welcome to jetairways, please check our menu:")
print("1-Coffee        $5.00")
print("2-Soft drink    $7.00")
print("3-Chips         $3.45")
print("4-Cookies       $4.50")

menu = {"Coffee": 5, "coffee": 5,
        "Soft drink": 7, "soft drink": 7,
        "Chips": 3.45, "chips": 3.45,
        "Cookies": 4.50, "cookies": 4.50
        }

drink = str(input("What do you want to drink today? "))
snack = str(input("And what about a snack? "))

print("Your total today is $%0.2f" % (menu[drink] + menu[snack]))
print("Have a great day")
