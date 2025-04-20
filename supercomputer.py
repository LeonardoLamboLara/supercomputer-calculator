import math
#Asks the user how many supercomputers they have.
supercomputer = math.ceil(float(input("How many supercomputers do you have? ")))

#Asks for power per computer
power = math.ceil(float(input("How much power per machine (in petaflops)? ")))

#Asks from what country
country = input("From what country are you running your supercomputer? ")

total_power = supercomputer * power

#Prints total compute power
print(f"Your total compute power in {country} is {total_power} petaflops  king!")

#Rounding note
print(f"Note: Rounded number of supercomputers to {supercomputer}")