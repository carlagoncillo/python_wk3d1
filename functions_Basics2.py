#1
def countdown(num):
    y = []
    for x in range(num, -1, -1):
        y.append(x)
    print(y)
countdown(5)

#2
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

#3
def first_plus_length(list):
    sum = list[0] + (len(list))
    return sum
print(first_plus_length([1,2,3,4,5]))

#4
def value_greater_than_second(list):
    newlist = []
    for i in list:
        if len(list) < 2:
            return False
        elif i > list[i]:
            newlist.append(i)
    print(len(newlist))
    return newlist
print(value_greater_than_second([5,2,3,2,1,4]))
print(value_greater_than_second([3]))

#5
def length_and_Value(size, value):
    newList = []
    for i in range(0, size):
        newList.append(value)
    return newList
list_Same_Values =  length_and_Value( 6, 2)
list_Same_Values_two =  length_and_Value( 4, 7)
print(list_Same_Values)
print(list_Same_Values_two)