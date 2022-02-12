# # prob 1 
name = input("Enter your name\n") 
print("Good Morning," + name) 

#prob 2 
msg = ''' Dear <|name|>, 
you are selected for the job interview which will be held on Monday

 <|date|>
''' 
name = input("Enter your name:\n")
date = input("Date:\n")
msg = msg.replace("<|name|>", name)
msg= msg.replace ("<|date|>", date) 
print(msg)

# prob3 
st = " My name is Rehan Sameer Mahat"
instant = st.replace(" ", "  ") 
print(instant) 


# prob4 
letter = "Dear Rehan, you are the best person in the world! Thanks!" 
print(letter) 
format = "Dear Rehan, \nyou are the best person in the world!\n Thanks!" 
print(format) 