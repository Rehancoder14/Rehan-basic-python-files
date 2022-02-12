def current(amp ):
    I = (amp/30)
    return I

charge = int(input("Enter the charge:\n"))
Q = current(charge)
print(Q)