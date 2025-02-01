import random
import os


def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:
        os.system('clear')


# Card deck: numbers (or 11 for Ace if not handled later) and face cards as strings.
cards = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J", "a"]

# Message lists
welcomeMessage = [
    "Welcome to BlackJack! 🎲 Ready to test your luck and skill? Let’s play!",
    "Step right up to the table! 🃏 Let’s see if today’s your lucky day!",
    "Shuffling the deck... 🔄 Get ready for an exciting game of BlackJack!",
    "Welcome, challenger! ⚔️ Can you outsmart the dealer and take the win?",
    "Cards are dealt, the stakes are high! 🔥 Let’s play some BlackJack!"
]
drawBjMessage = [
    "Oh, look at that—21 for both of you. What are the odds?",
    "Wow, 21 for everyone. Guess the cards are just feeling generous today!",
    "Well, isn’t this special? 21 for both players. Must be nice!"
]
winBjMessage = [
    "BAM! You hit BlackJack! 🎉 You’re the real card master!",
    "You got 21! A BlackJack worthy of applause! 👏",
    "BlackJack! 🎲 You’re the master of the deck!"
]
loseBjMessage = [
    "Oh no! The computer got BlackJack! 😱 Better luck next time!",
    "The computer has BlackJack... Looks like it outsmarted you this time! 🤖",
    "Oops! The opponent pulled a BlackJack! Don’t worry, you'll get them next time! 😬"
]
bustedMessage = [
    "Oops, you busted! 💥 Looks like luck wasn’t on your side today!",
    "You busted! The final card wasn’t your friend... 😬",
    "Busted! You went over 21, but you’ll get it next time! 😅"
]
compBustedMessage = [
    "YAY! The computer busted! 🎉 VICTORY, you win this one!",
    "The computer went over 21! Looks like you just won! 🏆",
    "The computer busted! Victory is yours! 🎉"
]
highPointMessage = [
    "You won! 🎉 You’ve got the skills, my friend!",
    "Victory is yours! 🏆 You played your cards right!",
    "Congratulations, you’re the card champion! 👏"
]
compHighPointsMessage = [
    "You lost this round, but don’t worry, it’s just a game! 😅",
    "The computer takes this one! 🥲 But you’ll get 'em next time!",
    "The computer won this round, but you played great! On to the next! 😎"
]
drawMessage = [
    "It’s a tie! 🎲 No winner today, but great game!",
    "Well, that was close! It’s a draw! Better luck next round! 🤝",
    "A draw! No one won, but both played brilliantly! ✨"
]
goodbyeMessage = [
    "Alright, you’re done for today. Take care, and come back soon! ✌️",
    "Game over for now! Hope to see you again soon! 👋",
    "That’s a wrap! You played well today. Catch you later! 🎮",
    "Goodbye! May the cards be ever in your favor next time! 🍀",
    "It’s time to call it a day. Until next time, card master! 😎",
    "Sad to see you go! But hey, you can always come back for more fun! 👋"
]


# Single function to calculate the total value of a hand
def calculate_value(cards_list):
    total_value = 0
    ace_count = 0
    for card in cards_list:
        if isinstance(card, int):  # If the card is an integer (e.g., 2, 3, 10)
            total_value += card
        elif card == 'a':  # Ace, add 11 initially
            total_value += 11
            ace_count += 1
        else:  # For other face cards (J, Q, K), consider them as 10
            total_value += 10

    # Adjust Ace value from 11 to 1 if total is greater than 21
    while total_value > 21 and ace_count:
        total_value -= 10
        ace_count -= 1

    return total_value


# Function to check the victory conditions and display final hands
def check_victory(current_score, comp_current_score, player_cards, comp_cards):
    total_cards_player = calculate_value(player_cards)
    total_value_comp = calculate_value(comp_cards)


    print(f"\nYour final cards: {player_cards}, final score: {total_cards_player}")
    print(f"Dealer final cards: {comp_cards}, Dealer final score: {total_value_comp}")

    if current_score == 21 and comp_current_score == 21:
        print(random.choice(drawBjMessage))
    elif current_score == 21:
        print(random.choice(winBjMessage))
        return True
    elif comp_current_score == 21:
        print(random.choice(loseBjMessage))
        return True
    elif current_score > 21:
        print(random.choice(bustedMessage))
        return True
    elif comp_current_score > 21:
        print(random.choice(compBustedMessage))
        return True
    elif current_score > comp_current_score:
        print(random.choice(highPointMessage))
        return True
    elif comp_current_score > current_score:
        print(random.choice(compHighPointsMessage))
        return True
    elif comp_current_score == current_score:
        print(random.choice(drawMessage))
        return True
    return False  # Game not over yet


def ask_to_play_again():
    while True:
        play = input("\nDo you want to play again? (y/n): ").lower()
        if play == "y":
            clear_console()
            return True
        elif play == "n":
            print(random.choice(goodbyeMessage))
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def play_game():
    play = input("Do you want to play a game of BlackJack? (y/n): ").lower()
    while True:  # Main loop to keep the game running
        if play == "y":
            clear_console()
            print(random.choice(welcomeMessage))
            # Deal initial cards
            player_cards = [random.choice(cards), random.choice(cards)]
            comp_cards = [random.choice(cards), random.choice(cards)]
            player_score = calculate_value(player_cards)
            comp_score = calculate_value(comp_cards)


            print(f"\nYour cards: {player_cards}, current score: {player_score}")
            print(f"Dealer's first card: {comp_cards[0]}")

            # Player decision loop
            while player_score < 22:
                choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if choice == "y":
                    new_card = random.choice(cards)
                    player_cards.append(new_card)
                    player_score = calculate_value(player_cards)

                    print(f"\nYour cards: {player_cards}, current score: {player_score}")
                    print(f"Dealer's first card: {comp_cards[0]}")
                elif choice == "n":
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
                    continue


            if player_score <= 21:
                while comp_score < 17:
                    comp_cards.append(random.choice(cards))
                    comp_score = calculate_value(comp_cards)



            if check_victory(player_score, comp_score, player_cards, comp_cards):
                if not ask_to_play_again():  # Ask to play again
                    break

        elif play == "n":
            print(random.choice(goodbyeMessage))
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

            play = input("Do you want to play a game of BlackJack? (y/n): ").lower()


play_game()
