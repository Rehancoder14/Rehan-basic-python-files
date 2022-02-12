#write a python programs scored in subjects(fds), by n number of students and then compute 
# following 
marks = []
N = int(input("Enter no of students (for absent students enter -1) : \n "))
for i in range(N):
    n = int(input("Enter Your marks: "))
    marks.append(n)
    

print(marks)
def abs_students():
    count = 0
    for i in range(N):
        if marks[i]== -1:
            count +=1
    return count


def avg_marks():
    total = 0 
    for j in range(N):
        total = total + marks[j]
    return total/(N-abs_students)
   


def highlow():
    max = 0
    min = 100
    for k in range(N):
        if max<marks[k]:
            max = marks[k]
            
        if min> marks[k] and marks[k]!= -1:
            min = marks[k]
        print(min, marks)    
        # print("Highest marks in the list is : ",max)
        # print("Lowest marks in the list is : ", min)


def highfreq():
    

print("The average of marks of student is ",avg_marks())
print("The high and low scores respectively are ",highlow())

