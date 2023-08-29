print('Welcome to EL Quiz Game Version 1.0')
playing = input("Do you want to play the game? ").lower()
if playing != "yes":
    print("Game ended")
    quit()

print("Let's play El Game")   
score = 0


answer = input("What does PC stand for? ").lower()
if answer == "personal computer":
    print('Correct!')
    score += 1
else: 
    print('incorrect!')

answer = input('What does LP stand for> ').lower()
if answer == "labour party":
    print('correct!')
    score += 1
else:
    print('incorrect!')

answer = input('who won 2023 presidential election in Nigeria? ').lower()
if answer == "peter obi":
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input('How many states do we have in Nigeria? ').lower()
if answer == '36':
    print('correct!')
    score += 1
else:
    print('incorrect!')

print(" You got " + str(score) + " questions correct")
print(" That is " + str((score/4) * 100) + "%")