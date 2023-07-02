def tot_coins(X,Y):
    received_coins=(X*10)+(Y*5)
    return received_coins
X=int(input (" enter the number of 10 rupees coins :"))
Y=int(input (" enter the number of 5 rupees coins :"))
tot_received=tot_coins(X,Y)
print("total money",tot_received,"rupees")
