with open("logfile.txt","r") as f :
    data = f.read()
    
if "Python" in data:
    print("Python is present.")
else:
    print("Python is absent.")
    