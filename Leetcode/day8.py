#PIZZA BILL GENERATOR
class Normal:
    def __init__(self):
        self.name = "Normal"
        self.veg = 300
        self.nonveg = 400
class Delux:
    def __int__(self):
        self.name = "Delux"
        self.veg = 600
        self.nonveg = 800
print("\nPizza Categories")
print("\n1.Normal \n2.Delux")
choice = int(input("\nEnter your Choice[1 or 2]: "))
if choice == 1:
    pizza = Normal()
elif choice == 2:   
    pizza = Delux()
else:
    print("Invalid Choice")
print("\nPizza Types")
print("\n1.Veg \n2.Non-Veg")
type_choice = int(input("\nEnter your Choice[1 or 2]: "))

choice_cheese = int(input("\n Enter Cheese? [1.Yes or 2.No]: "))
choice_toppings = int(input("\n Enter Toppings? [1.Yes or 2.No]: "))
choice_Water_bottle = int(input("\n Do you want Water Bottle? [1.Yes or 2.No]: "))
if choice_Water_bottle == 1:
    count_water_bottle = int(input("\n How many bottles?: "))
choice_ketchup = int(input("\n Do you want Ketchup? [1.Yes or 2.No]: "))
if choice_ketchup == 1:
    count_ketchup = int(input("\n How many packets?: "))
choice_Soft_Drinks = int(input("\n Do you want Soft Drinks? [1.Yes or 2.No]: "))
if choice_Soft_Drinks == 1:
    count_Soft_Drinks = int(input("\n How many Cans?: "))
choice_take_away = int(input("Is it a Take Away[1.Yes or 2.No]"))

print("-"*50)
print("\nPizza Bill Generator")
print("-"*50)
#base price 
if choice == 1 and type_choice == 1:
    print("\nBase Price     =", pizza.veg)
elif choice == 1 and type_choice == 2:
    print("\nBase Price     =", pizza.nonveg)
elif choice == 2 and type_choice == 1:
    print("\nBase Price     =", pizza.veg)
elif choice == 2 and type_choice == 2:
    print("\nBase Price     =", pizza.nonveg)
else:
    pass
#cheese
if choice_cheese == 1:
    cheese_price =100
    print("\nCheese         =",cheese_price)
else:
    pass
#toppings
if choice_toppings == 1:
    toppings_price = 100
    print("\nToppings       =",toppings_price)
else:
    pass
#water bottle
if choice_Water_bottle == 1:
    water_bottle_price = 20*count_water_bottle
    print("\nWater Bottle   =",water_bottle_price)
else:
    pass
#ketchup
if choice_ketchup == 1:
    ketchup_price = 5*count_ketchup
    print("\nKetchup Packets       =",ketchup_price)
else:
    pass
#soft drinks
if choice_Soft_Drinks == 1:
    soft_drinks_price = 75*count_Soft_Drinks
    print("\nSoft Drinks    =",soft_drinks_price)
else:
    pass
#take away
if choice_take_away == 1:
    take_away_price = 20
    print("\nTake Away      =",take_away_price)
else:
    pass
print("-"*50)
#total price
total_price = cheese_price+toppings_price+water_bottle_price+ketchup_price+soft_drinks_price+take_away_price
if choice == 1 and type_choice == 1:
    total_price += pizza.veg
elif choice == 1 and type_choice == 2:
    total_price += pizza.nonveg
elif choice == 2 and type_choice == 1:  
    total_price += pizza.veg
elif choice == 2 and type_choice == 2:
    total_price += pizza.nonveg
else:
    pass
print("\nTotal Price    =",total_price)
#GST
gst = total_price*0.18
print("\nGST Charges      =",round(gst,1))
print("-"*50)
final_amount = total_price + gst
print("\nFinal Amount     =",final_amount)
     
        


        

