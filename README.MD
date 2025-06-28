🎯 Number Guessing Game (C Version)
A simple console-based number guessing game written in C. The program generates a random number between 1 and 10,000, and the player must guess it. After each guess, the program provides feedback whether the guessed number is too high or too low.

📦 Features
Generates a random number on each play.

Informs the user if their guess is higher or lower than the target.

Looped gameplay — user can keep playing as many times as they want.

Console screen clears when restarting (on Windows).

🛠 Technologies Used
C Programming Language

Standard Libraries:

stdio.h

stdlib.h

time.h

ctype.h

windows.h (for system("cls"))

🚀 How to Run
Copy the source code into a file, e.g., guessing_game.c.

Compile the program using any C compiler:

bash
Copy
Edit
gcc guessing_game.c -o guessing_game
Run the executable:

bash
Copy
Edit
./guessing_game
(On Windows, just double-click or run guessing_game.exe)

🎮 Gameplay
Enter your guess.

Receive hints: “HIGHER” or “LOWER”.

Continue until you guess the correct number.

Choose to play again by entering Y/y, or exit with N/n.

