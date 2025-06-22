count = 0
money = 50
while True:
    if money <= 0:
        print("You have no money. Game over.")
        break
    elif count > 0:
        continue_game = input(f"You have ${money}. Do you want to play again? (yes/no): ").strip().lower()
        if continue_game == "no" or "n":
            print(f"Thank you for playing! You've played the game {count} times.")
            break
        elif continue_game == "yes" or "y" or "ye":
            count = 0
            print("Starting a new game...")
            continue
    else:
        lower_range = int(input("Enter the minimum NUMBER for the guessing range: "))
        upper_range = int(input("Enter the maximum NUMBER for the guessing range: "))
        if lower_range >= upper_range:
            print("Invalid range. The minimum number must be less than the maximum number." )
        else: 
            import random
            number_to_guess = random.randint(lower_range, upper_range)
            attempts = 0
            print(f"Welcome to the Number Guessing Game! You have ${money} to start with. Each guess costs $5. If you lose all your money, the game ends.")

            while True:
                guess = int(input(f"Guess a number between {lower_range} and {upper_range}: "))
                count = 0
                attempts += 1
                if money <= 0:
                        print("You have run out of money! Game over.")
                        count += 1
                        break
                
                elif guess < lower_range or guess > upper_range:
                    money -= 5
                    print(f"Please guess a number within the range of {lower_range} to {upper_range}. You have ${money}")
                    
                elif guess < number_to_guess:
                    money -= 5
                    print(f"Go higher! You have ${money}")
                    
                elif guess > number_to_guess:
                    money -= 5
                    print(f"Go lower! You have ${money}")
                    
                else:
                    count += 1
                    if attempts == 1:
                        money += 100
                        print(f"Congratulations! YOU WIN THE JACKPOT OF $100!!! YOU HAVE ${money}!! You've guessed the number {number_to_guess} in {attempts} attempt.")
                        break
                    else:
                        money += 50
                        print(f"Congratulations! YOU WIN $50!!! YOU HAVE ${money}!! You've guessed the number {number_to_guess} in {attempts} attempts.")
                        break
