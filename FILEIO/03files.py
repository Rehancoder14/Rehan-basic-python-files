with open('Another.txt', 'r') as f:
    a = f.read()
with open('Another.txt', 'w') as f:
    a = f.write("me")
print(a)