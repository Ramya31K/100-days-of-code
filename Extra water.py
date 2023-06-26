def calculate_water (x,y):
    water = x - y
    return water
x = float(input("Enter the bucket capacity in liters: "))
y = float(input("Enter the current water level in liters: "))
extra_water= calculate_water(x,y)
print("extra water:", extra_water)
