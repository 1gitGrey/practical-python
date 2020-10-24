# bounce.py
#
# Exercise 1.5


# declares step variable for loop
n = 0 # the # of drops
h = 100 # m | initial height

# loop
while n < 10:
    h = h * (3/5)
    print(n + 1, round(h, 4))
    n += 1
