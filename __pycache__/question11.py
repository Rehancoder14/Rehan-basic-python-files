

def remove(string, word):
    newstr =  string.replace(word, " ")
    return newstr.strip()


mystr =  "      Rehan is a coder      "
A = remove(mystr,"coder")
print(A)