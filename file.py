num1 = 42   # variable declaration
num2 = 2.3  # variable declaration
boolean = True  # variable declaration
string = 'Hello World'  # variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, data types, strings, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, dictionary
fruit = ('blueberry', 'strawberry', 'banana') # list

print(type(fruit)) # log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') # add value, string
print(person['name']) # log statement, data type, string

person['name'] = 'George' # change value
person['eye_color'] = 'blue' # change value string
print(fruit[2]) # log statement, date type

if num1 > 45: # length check, access value
    print("It's greater") # log statement
else:   # else function
    print("It's lower") #log statement, data type string

if len(string) < 5: #length check, access value
    print("It's a short word!") #log statement
elif len(string) > 15: # else length check access value 
    print("It's a long word!") # log statement, string 
else: # else
    print("Just right!") # log statement

for x in range(5): # for loop, function argument parameter
    print(x) #log statement
for x in range(2,5): # for loop function argument parameter
    print(x) # log statement 
for x in range(2,10,3): # for loop function argunent parameter
    print(x) # log statement
x = 0 #variable declaration
while(x < 5): #start while loop
    print(x)    # log statement, data type number
    x += 1 #while loop increments by 1

pizza_toppings.pop() #function delete value
pizza_toppings.pop(1) #function delete value

print(person) # log statement
person.pop('eye_color') #function, delete value
print(person) #log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': #if conditional
        continue # continue for loop
    print('After 1st if statement') #log statement, data type string
    if topping == 'Olives': #if condtional
        break #stop for loop

def print_hello_ten_times(): # funtion arguement
    for num in range(10): #function parameter
        print('Hello') # log statement, data type string

print_hello_ten_times() #log statement,  function, data type strings

def print_hello_x_times(x): # function argument
    for num in range(x): # function parameter
        print('Hello')  # log statement , data type string

print_hello_x_times(4) #log statement, function argument, data type string

def print_hello_x_or_ten_times(x = 10):#function argument
    for num in range(x): #function parameter
        print('Hello') #log statement, data type string

print_hello_x_or_ten_times() #log statement, function argument
print_hello_x_or_ten_times(4) #log statement, function argument



"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)