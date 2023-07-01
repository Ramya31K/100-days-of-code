def need_money(C,X,Y):
    add_choc=C-X
    need_money=add_choc*Y
    return need_money
C=int(input ("enter the number of chocolate chef wants to gift:"))
X=int(input ("enter the number of chocolate chef already has:"))
Y=int(input ("enter the cost of one chocolate :"))
minimum_money_required=need_money(C,X,Y)
print("Minimum money required",minimum_money_required,"rupees")
