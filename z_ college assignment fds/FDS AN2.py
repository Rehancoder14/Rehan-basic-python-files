#Write a Python program to store marks scored in subject “Fundamental of Data
#Structure” by N students in the class. Write functions to compute following:
#a) The average score of class
#b) Highest score and lowest score of class
#c) Count of students who were absent for the test
#d) Display mark with highest frequency


marks=[]              #list for storing the students marks
#print(marks)
N=int(input("Enter no. of student: "))  

for i in range(N):
    m=int(input("Enter your marks (for absent enter -1): "))
    marks.append(m)

print(marks)



def highlow():              #Highest score and lowest score of class
    max=0 
    min=100
    for k in range(N):         
        if(max < marks[k]):
            max=marks[k]

        if(min>marks[k] and marks[k]!=-1):
            min=marks[k]
    
    return max, min
    
def absentstudent():        #Count of students who were absent for the test
    count=0 
    for i in range(N):
        if marks[i]==-1:
            count+=1
    
    return count  
    
def avgmarks():                 #The average score of class 
    total=0
    for j in range(N):
        if(marks[j]!=-1):
            total=total+marks[j]

    return total/(N-absentstudent())
    
def highfreq():      #Display mark with highest frequency
    fcount=0
    fmax=0
    for i in range(N):
        fcount=0
        for j in range(N):
            if(marks[i]!=-1 and marks[j]!=-1 and marks[i]==marks[j]):
                fcount+=1
        
        if fmax<=fcount:
            fmax=fcount
            num=marks[i]
    
    return num, fmax
    

print("The average marks of students: ", avgmarks())

print("High and low score respectively are: ", highlow())

print("Total no. of absent students: ", absentstudent())

print(highfreq())






