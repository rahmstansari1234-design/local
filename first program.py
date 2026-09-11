print("        LOVE CALCULATOR")
print("=" * 32)

first_name = input("Enter your name: ").strip()
second_name = input("Enter her name: ").strip()
were = input("Do you know each other or is it just a crush? ").strip().casefold()

if not first_name or not second_name:
    print("Please enter both names.")
else:
    scores = {
        "yes": 99.99,
        "no": 49.99,
        "maybe": 50.00,
        
    }
    score = scores.get(were, 51.00)

    print(f"\n{first_name} + {second_name} = {score}% love")

    if score >= 80:
        message = "Amazing match!"
    elif score >= 50:
        message = "There is a lovely connection."
    else:
        message = "You have to take a chance and make your own paradox of love."

    print(f"\n{message}")
    print("Only time will tell, so get to know each other or take a chance!")





    