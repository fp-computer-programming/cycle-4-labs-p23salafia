#Creator JS 10/13/2022
#Input Animal and Dish
animal = input("Please enter the name of the animal attening the feast:")

#Prompt user to enter desired dish
dish = input("Please enter the name of the dish that your animal is bringing:")


#Conditional statement to determine whether the animal is allowed to bring the dish
if animal[0] == dish[0] and animal[0] == dish[len(dish)-1]:
    print("Your beast can bring " + dish + " to the feast!")
else: 
    print("Your beast may not bring " + dish + " to the feast")