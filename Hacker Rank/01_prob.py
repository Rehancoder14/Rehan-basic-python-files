N = int(input())
mylist= []
for i in range(N):
    name = input()
    score = float(input())
    mylist.append([name,score])

mylist = sorted(list(set([x[1]] for x in mylist)))
second_lowest = mylist[1]

low_score = []
for name in mylist:
    if second_lowest==name[1]:
        low_score.append(name[0])
    
for name in sorted(low_score):
    print(name)
