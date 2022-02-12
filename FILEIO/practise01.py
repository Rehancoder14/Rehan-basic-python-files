file = open("twinkle.txt")
t = file.read()
if "star" in t:
    print("star is present in it")
else:
    print("star is absent")

file.close()   
