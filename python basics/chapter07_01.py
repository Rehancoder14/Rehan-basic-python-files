# write a program to print a multiplication table of given a number
table = int (input("Enter your number:\n "))
for i in range (1,11):
    # print(str(table)+ "x" + str (i) + "="+ str(i* table))
    print(f"{table}x{i}= {i* table }")