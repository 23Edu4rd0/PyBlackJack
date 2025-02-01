# BlackJack Game in Python

Welcome to the BlackJack Game! This project is a fun, interactive simulation of a BlackJack game where you can challenge the dealer and test your luck and skill.

## Features

- **Interactive Gameplay:** Play a game of BlackJack against the computer with simple `y/n` inputs.
- **Dynamic Messaging:** Enjoy a variety of messages for wins, losses, ties, BlackJack, busts, and more. Each game round displays random messages to keep the experience fresh.
- **Console Clearing:** The console is automatically cleared between rounds to provide a clean interface.
- **Easy-to-Understand Code:** The project is written in Python and is structured for easy customization and learning.

## How It Works

1. **Starting the Game:** When the game starts, a random welcome message is displayed.
2. **Game Flow:**
   - The player and the computer are both dealt two cards.
   - The player's score and one of the computer's cards are shown.
   - The player can choose to draw more cards or pass.
   - If the player passes, the computer draws cards until reaching a score of at least 17.
   - The game then evaluates the outcome (win, loss, tie, bust, or BlackJack) and displays a corresponding message.
3. **Replay Option:** After each game, the player is asked if they want to play again. If yes, the console is cleared, and a new game starts.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/blackjack-game.git
   ```
2. Navigate to the project directory:
   ```sh
   cd blackjack-game
   ```
3. (Optional) Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

## Running the Game

Run the following command:

```sh
python blackjack.py
```

## Customization

- **Messages**: The game uses lists to store various messages for different situations (e.g., wins, losses, ties, BlackJack, busts, etc.). Feel free to modify or add new messages.
- **Gameplay**: You can adjust the gameplay logic, card deck, or scoring system as needed. The code is well-commented for easy modifications.

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, please create an issue or submit a pull request.

## License

This project is open source and available under the MIT License.


