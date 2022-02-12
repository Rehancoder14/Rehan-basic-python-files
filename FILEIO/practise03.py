# writing the table in file 


for i in range(2,21):
    with open(f"Tables.txt", "w") as f:
        for j in range(1,11):
            a= f.write(f"{i} x {j} = {i*j}\n")
            print(a)
        break
