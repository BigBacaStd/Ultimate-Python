# Python Script

# Write and execute a script which request the user to input a real
# number in the interval [0,10]. Then, it must assign to the mark the corresponding
# qualitative mark according to the following rules:
# - 'Fail': Marks in the range [0,5].
# - 'Pass´: Marks in the range [5,8].
# - 'Honors': Marks in the range [8, 9.5].
# - 'Full honors': Mark in the range [9.5, 10].

# Example; If the mark is 4 or 8 the result on-screen should be 'Fail' or 'Honors', respectively.

Mark_Value=float(input('Please enter mark: '))

if Mark_Value <=5:
    print('Fail')

elif (Mark_Value >5) and (Mark_Value <=8):
    print('Pass')

elif (Mark_Value > 8) and (Mark_Value < 9.5):
    print('Honors')


else:
    print('Full Honors')

