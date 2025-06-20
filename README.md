# Python--project-higher_lower
The Higher Lower game challenges players to guess which of two social media accounts has more followers. Players earn points for correct guesses and continue until they guess wrong. The game features engaging visuals and a simple interface for endless fun!
### Step 1: Setting the Stage: Imports and Game Initialization

- **Imports**:
  - `import random`: Used for random selection of accounts.
  - `import higherLowerlogo`, `import higherlowerdata8`: Custom files containing game data and logo.
  - `import os`: Clears the console screen for a clean user experience.

- **Initial Game State**:
  - The game logo is printed, the score is initialized to zero, and the first account is randomly selected.

### Step 2: Modular Design: The Helper Functions

- **display_accountinfo(account)**:
  - Formats account data into a readable string.

- **check_answer(guess, follower_1, follower_2)**:
  - Determines if the player's guess is correct based on follower counts.

### Step 3: The Game's Engine: The Main while Loop

- Each iteration represents a round where the player makes a guess.
- The game continuously cycles through accounts, ensuring no duplicates for comparison.

### Step 4: The Aftermath: Scoring and Continuation

- After each guess, the screen is refreshed, and the score is updated based on the player's answer.
- The game ends when the player makes an incorrect guess.

### Step 5: Post-Loop Code

- Displays the final accounts after the game ends, though this may be leftover debugging code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
