def calculate_water(N):
    hour = 2
    total_required = hour * N
    return total_required
N = int(input("Enter the number of hours: "))
water_required = calculate_water(N)
print("The water cooler would require", water_required, "liters of water to cool for", N, "hours.")
