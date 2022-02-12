data = True
i = 1

with open("logfile.txt") as f :
    while data:
        data = f.readline()
        if "python" in data:
            print(data)
            print(f"Python is present in{i}")
            print(i)
        i+= 1
    
    
    

    
