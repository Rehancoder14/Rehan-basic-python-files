l1 = [1,7,15,34,3,6]
l1.sort() #sorts the list in ascending form 
print(l1)  

l1.reverse() #reverse function rewrites in reverse form 
print(l1)

l1.append(100) #prints 100 at the end of the list.
print(l1) 


l1.insert(0,10)# insert funtion add the number wherever we want 
print(l1)


l1.pop(2) # pop function deletes the number according to the index
print(l1) 


l1.remove(34) #remove function remove the number which want
print(l1) 

print(l1.index(100))
# prints the position of the elements of the tuple
print(sum(l1))

