file1 = "logfile.txt"
file2 = "copy.txt"

with open(file1) as f :
    f1 = f.read()
with open(file2) as f :
    f2 = f.read()

if f1 == f2:
    print("Text in the file are same.")
else :
    print("Text in the file are not same.")