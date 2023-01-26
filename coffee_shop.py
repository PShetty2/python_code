"""
The coffee shop module contains functions and contains variables
important to implementing a coffee shop.
"""

# Set some variables
shop_name = "Runestone Brew House"
coffee_sizes = ["small", "medium", "large"]
coffee_roasts = ["hot chocolate", "light", "medium", "dark", "espresso"]
doughnut_flavors = ["plain", "chocolate", "sprinkles"]

def order_coffee(size, roast):
    """
    Take an order from a user
    :param size: a string containing one of the coffee_sizes
    :param roast: a string containing one of the coffee_roasts
    :return: a message about the coffee order
    """
    return "Here's your {} coffee roasted {}".format(size, roast)

def add_milk_please(fat_content):
    """
    Pretend like we're adding some milk to a coffee
    :param fat_content: a string or integer containing the milkfat content
    :return: a message about having added the milk
    """
    return "I've added the {}% milk".format(fat_content)

def order_doughnut(flavor):
    """
    Take an order from a user
    :param flavor: a string containing one of the flavor
    :return: a message about the doughnut order
    """
    return "Here's your {} doughnut".format(flavor)

def give_tip(tip_amount):
    """
    Take a tip from the user, then be happy about it
    :param tip_amount: the tip amount
    :return: nothing
    """
    print("Thank you so much!  We don't make a ton of money.")

    # Not having a "return" statement causes our function to return None