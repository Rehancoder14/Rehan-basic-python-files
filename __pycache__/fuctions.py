def percentage(marks):
    P = (marks[0]+marks[1]+ marks[2]+ marks[3]+marks[4]+marks[5]+marks[6])/650 *100
    return P
# def and return are  the key word or funtion
score = [62,79,78,78,69,56,54]
mypercentage = percentage(score)
print(mypercentage)



def temperature(fahrenheit):
    C =  ((fahrenheit - 32) * (5/9))
    return C

temp= int(input("Enter temperature:\n"))
currenttemp = temperature(temp)
print(currenttemp)
