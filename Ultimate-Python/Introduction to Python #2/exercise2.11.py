# Python Script

# Write and execute a script which request the user to input three real numbers in the interval [0,10].
# The three numbers marks corresponding to a test, a lab report and the exam of a subject, respectively.
# Given the marks, the script should find out the final mark and display a message whether the student has passed the subject or not
# The final mark is computed considering the following percentages:

#   - The test is 30% of the final mark.
#   - The lab report is a 20% of the final mark.
#   - The exam is the remainder of the final mark.

# The rule for passing the subject is that both (a) the exam mark and (b) the final mark must be higher than or equal to 5.

# Example: If the marks are 4.2 (test), 7 (lab report) and 5.8 (exam), the message on screen
# should be 'You have passed the subject and your final mark is 5.56'.
# Similarly, if the marks are 7.7 and 4.8, the message on-screen should be 'You have not passed the subject'.

test = float(input('Please enter Test mark: '))
lab = float(input('Please enter Lab mark: '))
exam = float(input('Please enter Exam mark: '))

final = 0.3*test + 0.2*lab + 0.5*exam

if final >= 5 and exam >=5:
    print(f'You have passed the subject and your final mark is {final:.2f}.')
else:
    print(f'You have not passed the subject your final mark is {final:.2f}.')