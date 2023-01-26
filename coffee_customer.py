import coffee_shop

# Output the information we know from the module
print("Welcome to", coffee_shop.shop_name)
print("Available sizes:", coffee_shop.coffee_sizes)
print("Available roasts:", coffee_shop.coffee_roasts)

# Get some inputs from the user
order_size = input("What size coffee do you want? ")
order_roast = input("What roast do you want? ")

# Send the order to the coffee shop module
shop_says = coffee_shop.order_coffee(order_size, order_roast)
# Print out whatever it gave back to us
print(shop_says)

# See if the user wants to add milk
add_milk_response = input("Do you want to add milk (y/n)? ")
# Convert the response to lowercase, then check for a "yes" answer
if "y" in add_milk_response.lower():
    milk_fat = input("What percent milk do you want added? ")
    shop_says = coffee_shop.add_milk_please(milk_fat)
    # Print out whatever it gave back to us
    print(shop_says)

print("THAT'S GOOD COFFEE!  Very good.  Your brain is working again.")

# See if the user wants to add a doughnut
add_doughnut_response = input("Do you want to add a doughnut (y/n)? ")
# Convert the response to lowercase, then check for a "yes" answer
if "y" in add_doughnut_response.lower():
    # Get some inputs from the user
    print("Available doughnuts", coffee_shop.doughnut_flavors)
    order_flavor = input("What type dougnut do you want? ")
    shop_says = coffee_shop.order_doughnut(order_flavor)
    print(shop_says)

# They better give a tip...
print("You better give a tip.")
tip_amount = input("Tip amount? $")
coffee_shop.give_tip(tip_amount)