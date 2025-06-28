#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <windows.h>

int main() {
    char playagain[2];  

    do {
        int user_input;
        srand(time(0));
        int random = rand() % 1000000 + 1;

        printf("Guess the number between 1 and 1000000:\n");

        do {
            printf("Enter your guess: ");
            scanf("%d", &user_input);

            if (user_input > random) {
                printf("Your guessed number is HIGHER!! \n");
            } else if (user_input < random) {
                printf("Your guessed number is LOWER \n");
            }
        } while (user_input != random);

        printf("🎉 Congratulations! You guessed it right!!\n");

        printf("Wanna play again? Type (Y) for Yes and (N) for No: ");
        scanf(" %s", playagain); 

        if (tolower(playagain[0]) == 'y') {
            system("cls"); 
        }

    } while (tolower(playagain[0]) == 'y');
    printf("Thanks for playing!!\n");

    return 0;
}
