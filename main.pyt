import random

print("""🕹️ Number Guessing Game - Instructions
        Welcome to the Number Guessing Game!

        🔢 The computer has selected a random number between 1 and 234190.

        🎯 Your goal is to guess the correct number.

        💡 After each guess:

        You'll be told if the number is too high or too low.

        Keep trying until you guess the correct number.

        🛑 To exit the game at any time, simply type: exit

        🧠 Only positive integer inputs are accepted.

        Good luck and have fun! 🎉
      """)

while(True):

    mode = (input("""Enter the mode of the game:
                 •1 for User will guess the number
                 •2 for Computer will guess the number \n => """))
    if(int(mode) < 1 or int(mode) > 2):
        print("Please enter the correct input : ")
        continue
    elif not (mode.isdigit()):
        print("Please enter the correct input : ")
        continue

    elif(int(mode) == 1):
        ran_num = random.randint(1,234190)
        num_of_attempts = 1
        hasExited = False

        user_input = input(f"Enter your choice : ")


        if(user_input.lower() == "exit"):
            print("👋 Thanks for playing!")
            break

        while ran_num != int(user_input):
            if(user_input.lower() == 'exit'):
                hasExited = True
                break

            if(user_input.lower() != "exit" and not user_input.isdigit()):

                user_input = input("🚫Please enter a number\n => ")
            
            if(int(user_input) > ran_num):
                user_input = input("🧠 Too High! Try entering a lower number\n => ")
                num_of_attempts += 1

            elif(int(user_input) < ran_num):

                user_input = input("🧠 Too Low! Try entering a higher number\n => ")
                num_of_attempts += 1
            

            

        if(hasExited):
            print("You have exited the game!")
            print(f"The number was : {ran_num} ")
            print("🔁 Wanna try again ? Type (Y) for Yes or (N) for No\n ")

        print("🎯")
        print("🎉 Congratulations! you guessed it right!")
        print(f"📈Number of attempts you took => {num_of_attempts}")
        print("🔁 Wanna play again ? Type (Y) for Yes or (N) for No\n ")
        
        isPlay = True;

        

    elif(int(mode) == 2):
        user_num = int(input("First enter a number for the computer to guess \n • Print 'h' if the entered number is higher than your number \n else, enter l \n =>"))
        comp_num = random.randint(1,234190)
        num_of_attempts_comp = 1
        while(comp_num != user_num):
            print(comp_num)
            user_feedback = input("=>")

                
            if(user_feedback == 'h'):
                difference = comp_num - random.randint(user_num, comp_num)
                comp_num -= difference
                num_of_attempts_comp += 1

            elif(user_feedback == 'l'):
                difference =  random.randint(comp_num ,user_num) - comp_num 
                comp_num += difference
                num_of_attempts_comp += 1

            if(user_feedback == 'h' and num_of_attempts_comp % 10 == 0):
                difference = random.randint(1, 3500)
                comp_num -= difference
                num_of_attempts_comp += 1

            if(user_feedback == 'l' and num_of_attempts_comp % 10 == 0):
                difference = random.randint(1, 3500) 
                comp_num += difference
                num_of_attempts_comp += 1
                
        print(comp_num)
        print("Oops! Computer guessed the number right!")
        print("🔁 Wanna play again ? Type (Y) for Yes or (N) for No\n ")
        isPlay = True

    while(True):
        plagain = input("=> ")
        if(plagain.lower() == "y"):
            isPlay = True
            break

        elif(plagain.lower() == "n"):

            isPlay = False
            break
        else:
            print("🚫Please enter a correct value!")
            continue
    
    if(isPlay):
        continue
    else:
        print("You have exited the game!")
        
        print("👋 Thanks for playing!")
        break
        


    
                