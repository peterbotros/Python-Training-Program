# This program gets three test scores and displays
# their average. It congratulates the user if the
# average is a high score

# The high score variable holds the value that is
# considerd a hight score.

hight_score = 95

# Get the thhree test scores
test1 = int(input('Enter the score for test 1:' ))
test2 = int(input('Enter the score for test 2:' ))
test3 = int(input('Enter the score for test 3:' ))

# Calculate the average test score.
average = (test1 + test2 + test3) / 3

#Print the average.
print('The average score is', average)

# If the average is a high score,
# congratulate the user.
if average >= hight_score:
    print ('Congrats!')
else
    print('That is a great average!')
