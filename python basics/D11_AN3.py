# Name : Rehan Sameer Mahat
# Div: D
# roll no : D11
# Assignment no 3




# To accept N numbers from user. Compute and display maximum in list, minimum in list,
# sum and average of numbers using built-in function.

numlist=[]

N=int(input("How many no. you want in list: "))

for j in range(N):
    numlist.append(int(input("Enter no: ")))

print(numlist)

max=0       #whenever taking max, take it as least value in the given list, we r assuming that all the e3lemetns in the list are greater than 0

for k in range(N):
    if numlist[k] > max:
        max=numlist[k]

print("The MAXIMUM  element in list is= "+str(max))


min=999999      #whenever taking min, take it as greater than the given list, we r assuming that all the values in the list are less that 999999

for k in range(N):
    if numlist[k] < min:
        min=numlist[k]

print("The MINIMUM  element in list is= "+str(min))

sum=0

for i in range(N):        #
    sum= sum + numlist[i]

print("Addition is = "+str(sum))
print("Average is  = "+str(sum/N))
