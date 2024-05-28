number=34
Number_of_guess = 1
print("You have to 9 Times to guess the number: ")
while(Number_of_guess<=9):
   guess = int(input("enter number to guess \n"))
   if(guess > number):
      print("You guess higher number, Please Guess less number");
   elif(guess < number):
      print("you guess the less number, plese guess the higher number")
   else:
      print("You guess the correct number!")
      print("in",Number_of_guess,"time You guess the number.")
      break;
   print(9 - Number_of_guess,"No. of chance is leave to guess");
   Number_of_guess = Number_of_guess + 1
if(Number_of_guess > 9):
   print("Game Over !")