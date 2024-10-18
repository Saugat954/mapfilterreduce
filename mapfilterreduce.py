
def cube(x):
    return x*x*x

print(cube(3))


#map functions in python

list1 = [1,2,4,6,8]
newlist = []
#normal ethod
for item in list1:
    newlist.append(cube(item))

print(newlist)

#using map method and using lambda function

 

list2 = [2, 3, 4, 5, 6]
list3 = [3,1,2,4,5]
my_list = list(map(lambda x,y: x + y, list2,list3))
print(my_list)


#filter function in python


def filter_function(x):
    return x>4

filtered_list = list(filter(filter_function,list2))
print(filtered_list)

#reduce function in python

from functools import reduce

number = [1,2,3,4,5,6]

reducednumber = reduce(lambda x,y:x+y, number)
print(reducednumber)