def serve(x, y):
    packets_per_minute = x
    serve = x * y
    return serve
x= int(input("Enter the number of stoves in the restaurant: "))
y= int(input("Enter the number of minutes: "))
customers_served = serve(x,y)
print("The chef can serve a maximum of", customers_served, "customers in", y, "minutes.")
