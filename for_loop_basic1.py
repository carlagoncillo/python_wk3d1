#1
for x in range (151):
    print(x)

x=0
while x<=150:
    print(x)
    x += 1

#2
for x in range (5,1001):
    if x % 5 == 0:
        print(x)

x=5
while x<=150:
    print(x)
    x += 5

#3
for x in range (1,101):
    if x % 10 == 0:
        x = "Coding Dojo"
    elif x % 5 == 0:
        x = "Coding"
    print(x)

#4
sum = 0
for x in range (0,500001):
    if x % 2 != 0:
        sum += x
print(sum)


#5
for x in range (2018,0,-4):
    print(x)

#6
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum + 1):
    if x % mult == 0:
        print(x)