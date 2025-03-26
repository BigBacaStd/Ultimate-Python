#Python script
#Counting euro cents

v50=50
v20=20
v10=10

M_50=int(input('The number of 50 cent coins in my wallet is:'))
M_20=int(input('of 20 cents I have:'))
M_10=int(input('and 10 cents I have:'))
money = M_50*v50 + M_20*v20 + M_10*v10
print('So I have', money,'cents.')