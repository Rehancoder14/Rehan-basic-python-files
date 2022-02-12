# Write a Python program to convert temperatures to and from celsius, fahrenheit
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
temp = int(input("Enter temperature:\n "))

convotempF =  ((temp - 32) * (5/9) )
print(convotempF , "is the temperature in degrees")
# convert farenheit into degree celcius

convotempC = ((temp * 9/5) + 32)
print (convotempC, "is the temperature in farenheit")
# convert degree celcius into farenheit