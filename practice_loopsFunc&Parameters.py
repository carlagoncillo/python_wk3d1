# Loops practice
# for Loops
for x in range (5):
    print(x)

for x in "Hello": # "Hello" is a string index of H = 0 and so on...
    print(x)

for val in "string":
    if val == "i":
        break   # break will stop the if statement its either exit or go back to the for loop
    print(val)
# output: s, t, r

for val in "string":
    if val == "i": 
        continue # The continue statement is very useful when you want to skip specific iteration(s), but still keep looping to the end.
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

# for loops end

# while loops
x=0
while x<5:
    print(x)
    x += 1

# while loop ends
# Loops practice ends here

# functions practice
def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

print(sum1)
print(sum2)
print(sum3)

def name(pop):
    return "Favorite Fruit: " + pop
fruit = name("Orange")
print(fruit)
# functions practice ends here

# Default parameters and & named arguments practice starts here
def name_it(name="Benji", repeat=2):
    print(f"Good Evening {name}!\n" * repeat) # this is how the format of a f string should look like

name_it()
name_it("Dodong")
name_it(name="Roberto")
name_it(repeat=3)
name_it(name="Botong", repeat=2) # it dont matter which format you want to use
name_it(repeat=4,name="Botong") # it dont matter which format you want to use
# Default parameters and & named arguments practice ends here