print("Welcome to Pizza Deliveries!")
pizza_S = 15
pizza_M = 20
pizza_L = 25
pepporoni_S = 2
pepporoni_ML = 3
xtra_cheese_SML = 1
Pizza_Size = input("What size pizza do you want? S, M or L: ")
Pepporoni = input("Do you want Pepporoni? Y or N: ")
Xtra_Cheese = input("Do you want extra cheese? Y or N: ")

if Pizza_Size == "S":
    if Pepporoni == "Y":
        if Xtra_Cheese == "Y":
            Total_bill = pizza_S + pepporoni_S + xtra_cheese_SML
        else:
            Total_bill = pizza_S + pepporoni_S
    else:
        if Xtra_Cheese == "Y":
            Total_bill = pizza_S + xtra_cheese_SML
        else:
            Total_bill = pizza_S
elif Pizza_Size == "M":
    if Pepporoni == "Y":
        if Xtra_Cheese == "Y":
            Total_bill = pizza_M + pepporoni_ML + xtra_cheese_SML
        else:
            Total_bill = pizza_M + pepporoni_ML
    else:
        if Xtra_Cheese == "Y":
            Total_bill = pizza_M + xtra_cheese_SML
        else:
            Total_bill = pizza_M
else:
    if Pepporoni == "Y":
            if Xtra_Cheese == "Y":
                Total_bill = pizza_L + pepporoni_ML + xtra_cheese_SML
            else:
                Total_bill = pizza_L + pepporoni_ML
    else:
            if Xtra_Cheese == "Y":
                Total_bill = pizza_L + xtra_cheese_SML
            else:
                Total_bill = pizza_L


print(f"Your total bill: ${Total_bill}")
