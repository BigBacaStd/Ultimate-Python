#Python script
# 4.8 Cubes: Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
# TODO: Add your code here

cubes = []

for number in range (1, 11):
    cube = number ** 3
    cubes.append(cube)
    print(cube)