# Beserat Tafesse
# define variables
# Inputs
length = float(input("What's the Length? "))
height = float(input("What's the Height? "))
baseW = float(input("What's the Base Width? "))
topW = float(input("What's the Top Width? "))

# Process equation
volume = length * height * ((baseW + topW) / 2)

# output variables, volume and reduced volume

print("The length is:", length)
print("THe height is:", height)
print("The Base Width is:", baseW)
print("The Top Width is:", topW)
print("The Volume is:", volume)
print("The reduced Volume is:", float(volume * .25))
