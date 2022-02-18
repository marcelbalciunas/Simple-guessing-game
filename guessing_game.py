import random

print("\nI just generated a random number between 1 and 100.")

#generating a random number
def random_num():
    random_number = list(range(1,101))
    x = random.choice(random_number)
    return x
random_number = random_num()

#checking the random number (default OFF)
# print(f"Random number is {random_number}")

#function to get a score point
def score(score_attempt, score_count):
   gold = 1000
   silver = 850
   bronze = 600
   wood = 400
   paper = 100

   finalscore = 0

   if(score_attempt <= 4):
      finalscore = (gold / score_attempt) * score_count
   elif(score_attempt > 4 and score_attempt <= 8):
      finalscore = (silver / score_attempt) * score_count
   elif(score_attempt > 8 and score_attempt <= 11):
      finalscore = (bronze / score_attempt) * score_count
   elif(score_attempt > 11 and score_attempt <= 15):
      finalscore = (wood / score_attempt) * score_count
   elif(score_attempt > 15):
      finalscore = (paper / score_attempt) * score_count

   return int(finalscore)

#validating user input
def validation(user_input):
      if user_input.isdigit():
         user_input = int(user_input)
         if user_input > 100:
            return False
         elif user_input > -1:
            return user_input
      else:
         return False

#take the attempts input and validate
while True:
   user_attempt_input = input("How many attempts to guess the number? (up to 100): ")   

   validated_attempt = validation(user_attempt_input)

   if validated_attempt == False:
         print("\nNot valid, enter only numbers from 1 to 100:")
   elif not validated_attempt == False:
      break

#checking validated attempt (default OFF)
# print(f"Number after validated attempt: {validated_attempt}")

#loop to repeat the attempts number times
for x in range(validated_attempt):
      x -= 1
      counter = validated_attempt - ( x + 1)
      #print(f"The x inside the loop is {x}")
      #print(f"The counter inside the loop is {counter}")

   #take the guesses input and validate
      while True:
         user_guess_input = input(f"\nAttempt {counter}: Guess a number between 1 - 100: ")   

         validated_guess = validation(user_guess_input)

         if validated_guess == False:
               print("\nNot valid, enter only numbers from 1 to 100:")
         elif not validated_guess == False:
            break

      #checking validated guesses (default OFF)
      #print(f"Number after validated guess: {validated_guess}")

      #find the positive difference between random number and validated guess
      diff = 0
      if random_number < validated_guess:
         diff = validated_guess - random_number
      else:
         diff = random_number - validated_guess

      #checking positive diff (default OFF)
      #print(f"the diff is {diff}")

      #tips1
      divisible_by_three = validated_guess % 3
      divisible_by_four = validated_guess % 4
      divisible_by_five = validated_guess % 5

      #tips2
      if counter < 2:
         if diff != 0:
            print("\nNo more attempts for you. Game Over.")
            print(f"The random number was {random_number}\n")
            break

      if diff == 0:
         my_score = score(validated_attempt, counter)
         print(f"\nYou win! You've got {my_score} points\n")
         break

      if diff > 95:
         if validated_guess > random_number:
            print("Seriously, you're faaaaaaaaaar away. Take out some dozens and see what happens.")
         else:
            print("There's a huge ocean of numbers between your number and the number you want to find out. Go ahead!")

      elif diff > 89 and diff <= 95:
         if validated_guess > random_number:
            print("There's quite a journey ahead, indeed a lot of numbers between your pick and the number you wanna catch.")
         else:
            print("Your number and the number you want to find out are very distant. Try again, little by little...")

      elif diff == 89:
         print("You've lost this attempt. Sorry")

      elif diff > 76 and diff < 89:
         if validated_guess > random_number:
            print("You're well ahead of the number you want to discover.")
         else:
            print("Your number needs to grow substantially to reach the one you're searching for.")

      elif diff == 76:
         if divisible_by_four == 0:
            print("The number is divisible by four")
         else:
            print("The number is not divisible by four")

      elif diff > 71 and diff < 76:
         if validated_guess > random_number:
            print("You're starting to not be sooo far from the number you want to find,\nbut remove a lot of numbers to be closer.")
         else:
            print("You're starting to not be sooo far from the number you want to find,\nbut add a lot of numbers to be closer.")

      elif diff > 60 and diff <= 71:
         if validated_guess > random_number:
            print("The number is ahead for more than the half of the range.")
         else:
            print("The number is behind for more than the half of the range.")

      elif diff == 60:
         print("you've lost this attempt. Sorry")

      elif diff > 51 and diff <= 59:
         if validated_guess > random_number:
            print("You're not far, but not close as well. But you're ahead!")
         else:
            print("You're not far, but not close as well. But you're behind!")

      elif diff > 41 and diff <= 51:
         if validated_guess > random_number:
            print("Little by little you're on the way. Remove several numbers to reach the goal.")
         else:
            print("Little by little you're on the way. Add in several numbers to reach the goal.")

      elif diff == 41:
         print("you've lost this attempt. Sorry")

      elif diff > 33 and diff <= 40:
         if validated_guess > random_number:
            print("You're really starting to get close, but there's a bunch ahead.")
         else:
            print("You're really starting to get close, but there's a bunch behind.")

      elif diff == 33:
         if divisible_by_five == 0:
            print("The number is divisible by five")
         else:
            print("The number is not divisible by five")      

      elif diff > 20 and diff <= 32:
         if validated_guess > random_number:
            print("You're near, but not too much. Take out some dozens and see for yourself.")
         else:
            print("You're near, but not too much. Put in some dozens and see for yourself.")  

      elif diff == 20:
         if divisible_by_three == 0:
            print("The number is divisible by three")
         else:
            print("The number is not divisible by three")  

      elif diff > 10 and diff <= 19:
         if validated_guess > random_number:
            print("In a piece of the range, there are several numbers to remove in order to discover the number.")
         else:
            print("In a piece of the range, there are several numbers to add in order to discover the number.")  

      elif diff > 5 and diff <= 10:
         if validated_guess > random_number:
            print("You're really getting there, by the way you're some numbers ahead though.")
         else:
            print("You're really getting there, by the way you're some numbers behind though.")

      elif diff > 1 and diff <= 5:
         if validated_guess > random_number:
            print("You're really really close, relax a bit to succeed.")
         else:
            print("You're really really close, add up some more numbers and see what happens.")

      elif diff == 1:
         if validated_guess > random_number:
            print("Wow almost there! the less you let it go is enough for you.")
         else:
            print("Wow almost there! one last push is enough!")
