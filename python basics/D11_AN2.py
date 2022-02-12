# Name : Rehan Sameer Mahat
# Div: D
# roll no : D11
# Assignment no 2

# To accept an object mass in kilograms and velocity in meters per second and display its momentum.
# Momentum is calculated as e=mc2 where m is the mass of the object and c is its velocity.


try:
 mass = float(input("Enter mass in kgs: "))  # m is mass in kgs
 velocity = float(input("Enter velocity in m/s: ")) # c is velocity in m/s
 momentum = mass*(velocity**2)    # e=mc2
 print('Momentum of object is', momentum)
except ValueError:
    print("Enter mass and velocity in int/float")



