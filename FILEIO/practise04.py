with open("rs.txt", "r") as f:
    content = f.read()

content1 = content.replace("donkey","#$%#$#$")

with open("rs.txt", "w") as f:
    a= f.write(content1)
print(a)



