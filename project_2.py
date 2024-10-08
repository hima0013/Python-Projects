# Building a tip calculator 
print("Welcome to the tip calculator")
Total= float(input("What is your total bill?\n"))
Tip= float(input ("How much tip you want to pay for the service (5%, 10%, 20%)?\n"))
Split= int(input("In How many people you want to spilt the bill?"))
Final = (((Tip/100)*Total)+Total)/Split
# or you can use this ...
# Final= round(Final ,2)

print(f"So, Each person should pay: ${round(Final, 2)}" )