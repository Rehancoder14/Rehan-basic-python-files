A = {
    "Rehan": "A chess player ",
    "scotch": "favourite opening",
    "SKN": "An engineering college",
    14 : "birth date"
}
print(A.keys) # will type all keys 
print(type(A.keys()))#will type the class which dictionary
print(A.values())#will all the value for keys
print(A.items())#will give the output of all keys and value collectively

B= {
    "abundant": " in very large quantity"
}
A.update(B)# update function will add the key and value according to our will
print(A)

print(A.get("Rehan")) #both will give the same output
#it the element or key is slightly changes it get function will not throw an error
print(A["Rehan"]) #this function will throw  error if key is changed