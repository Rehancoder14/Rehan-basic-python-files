# list1 =[21,4.3 , 54,2, "rehan", True]
# for index, item in enumerate (list1):
#     print(item, index)


list2 = [12,42,23,43,45,43,743,38,90]
# b = []
# for i in list2:
#     if i%2==0:
#         b.append(list2)

b = [ i for i in list2 if i %2 == 0]
print(b)
   