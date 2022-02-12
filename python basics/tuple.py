t = (1, 2, 3, 4) # this is tuple coz t is define by () .
print(t[1]) #prints the element of the tuple

#tuples cannot be altered or manipulated 
print(t.count(1))
# here it will count that how many times the number exist in tuple

print(t.index(2))
# prints the position of the elements of the tuple

a= set()  # set contains non repetitive element 
print(type(a))
a.add(4) # add function add the numbers into the set
print(a)
print(a.pop()) # pop function will remove element from set and return it again 
b = {1,2,3}
print(type(b))
