# Even-Odd Guessing Game

## Objective
Implement a Python program where a player competes against the computer in an even-odd guessing game.

## Rules
1. The player enters a number (integer).
2. The computer randomly generates a number.
3. The player guesses whether the sum of both numbers will be **even** or **odd**.
4. The program calculates the sum and determines if the player's guess was correct.
5. The program outputs whether the player **wins** or **loses** based on their guess.

## Constraints
- The player's input should be a valid integer.
- The program should handle invalid inputs gracefully.
- The computer-generated number should be random within a reasonable range (e.g., 1 to 10).
- The game should allow the player to continue playing until they choose to exit.

## Example Interaction
1. **Player Input:** Enter your number: `4`  
2. **Player Guess:** Guess 'even' or 'odd': `even`  
3. **Computer Choice:** Computer chose: `7`  
4. **Sum Calculation:** `4 + 7 = 11` (odd)  
5. **Result:** You lose!  

## Follow-up Enhancements
- Modify the game to track and display the player's win count.
- Allow the player to set a custom range for the computer’s number.
- Implement a best-of-5 mode where the first to 3 wins is the overall winner.
