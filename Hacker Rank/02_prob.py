def print_full_name(first,last):
    msg = "Hello <|first|> <|last|>! You just delved in python."
    a= msg.replace("<|first|>",first)
    b = a.replace("<|last|>",last)
    print(b)



first_name = input()
last_name = input()
print_full_name(first_name,last_name)