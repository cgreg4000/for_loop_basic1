for x in range(0, 151):
    print(x)

for x in range(5, 5001, 5):
    print(x)

for x in range(1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)


odd_sum = 0
for x in range(0, 500001):
    if x % 2 == 0:
        continue
    else:
        odd_sum = odd_sum + x

print(odd_sum)


x = 2018
while x >= 0:
    print(x)
    x -= 4


lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum + 1):
    if x % mult == 0:
        print(x)
