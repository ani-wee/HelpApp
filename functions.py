# Function to calculate the area of a circle
def circle_area(radius):
    pi = 3.1416
    area = pi * (radius ** 2)
    return area

#   Function to calculate total due with tax
def total_due(money, tax):
    total = money + (money * tax)
    return total

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

# Main Program

# Area of a Circle
radius = float(input("Enter the radius:"))
print(round(circle_area(radius), 2))

# Taxes
money = float(input("Enter the amount of money:"))
tax_percent = float(input("Enter the tx rate (%):"))
tax_rate = tax_percent / 100
print(f"{total_due(money, tax_rate):.2f}")

# Temperature
fahrenheit = float(input("Enter the fahrenheit temperature:"))
print(round(fahrenheit_to_celsius(fahrenheit), 4))
