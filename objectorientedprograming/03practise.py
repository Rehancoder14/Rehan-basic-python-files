class sample:
    a = "harry"
# class attribute does not change by the entity of the instance attribute
obj = sample()
obj.a = "Rehan"


print(sample.a) #this line will return harry
print(obj.a) #this line will return rehan