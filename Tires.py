def total_tires(N,M):
        total_tires=(N*2)+(M*4)
        return total_tires
N=int(input ("enter number of bikes : "))
M=int (input ("enter number of cars : "))
total_no_of_tires=  total_tires(N,M)
print ("total no of tires on the road is" ,total_no_of_tires)
