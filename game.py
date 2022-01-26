import random
random.seed()
print("Welcome to game \"Guess the number\"")
maxVal=int(input("Give max value:"))
print(maxVal)
number= random.randrange(1,maxVal)
print(number)
answer = int(0)
print("Guess the number,")
answer=int(input(" input some number:"))
while answer != number:
  if answer < number:
    print("Too small")
  else:
    print ("Too large")
  answer = int(input("Try again, input some number:"))
print("You\'ve made it!!!\nBye!!!")

