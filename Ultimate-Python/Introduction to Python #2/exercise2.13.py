# Python Script

# Repeat the exercise 2.11, including a qualitative mark together with the quantitative one.
# Matching quantitative-qualitative marks is as seen in exercise 2.10.

# Example: If the partial test mark is 9.5, the work mark 10 and the final test mark 9, the result
# on-screen should be 'You have passed the subject, your final mark is Honors'

test = float(input('Please enter Test mark: '))
lab = float(input('Please enter Lab mark: '))
exam = float(input('Please enter Exam mark: '))

final = 0.3*test + 0.2*lab + 0.5*exam

if test >= 9.5 and lab >= 10 and final >= 9:
    print(f'You have passed the subject, your final mark is Honors.')
else:
    print(f'You have not passed the subject')