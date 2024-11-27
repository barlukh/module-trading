""" Trading module. Handles the trading interaction with the vendor. """

import inventory
import vendor

def item_selection(function):
    """ Asks the player for a name of the item to buy or sell. """
    print("")
    print("-- Item selection --")
    print("0 : Previous menu\n")
    command = input("Enter a name of an item: ")
    print("")
    if command == "0":
        if function == inventory.buy_armor or function == inventory.buy_weapon:
            buy_items()
        else:
            sell_items()
    else:
        function(command)
        if function == inventory.buy_armor or function == inventory.buy_weapon:
            buy_items()
        else:
            sell_items()

def trade_categories(category):
    """ Prints available commands to the player to operate the buy / sell interaction. """
    print(f"-- Main menu -> {category} items --")
    print("0 : Previous menu")
    print("1 : Armor")
    print("2 : Weapons\n")

def buy_items():
    """ Function for buying items from the vendor. """
    trade_categories("Buy")
    allowed_input = [0, 1, 2]
    command = input_check()
    if command not in allowed_input:
        print("Wrong choice, only presented numbers allowed.\n")
        buy_items()
    elif command == 0:
        trade_main()
    elif command == 1:
        print(f"-- Main menu -> Buy items -> Armor --")
        print(f'{"Name" : <18}{"Price" : ^10}{"Tier" : ^10}{"Armor Rating" : ^15}')
        for key, value in vendor.vendor_armor.items():
            print(f'{key : <18}{value.price : ^10}{value.tier : ^10}{value.armor_rating : ^15}')
        item_selection(inventory.buy_armor)
    elif command == 2:
        print(f"-- Main menu -> Buy items -> Weapons --")
        print(f'{"Name" : <18}{"Price" : ^10}{"Tier" : ^10}{"Avg. Damage" : ^15}')
        for key, value in vendor.vendor_weapons.items():
            avg_damage = (value.min_dmg + value.max_dmg) / 2
            print(f'{key : <18}{value.price : ^10}{value.tier : ^10}{avg_damage : ^15.1f}')
        item_selection(inventory.buy_weapon)

def sell_items():
    """ Function for selling items to the vendor. """
    trade_categories("Sell")
    allowed_input = [0, 1, 2]
    command = input_check()
    if command not in allowed_input:
        print("Wrong choice, only presented numbers allowed.\n")
        sell_items()
    elif command == 0:
        trade_main()
    elif command == 1:
        if bool(inventory.player_armor) == False:
            print("Your Armor inventory is empty.\n")
            sell_items()
        else:
            print(f"-- Main menu -> Sell items -> Armor --")
            print(f'{"Name" : <18}{"Price" : ^10}{"Tier" : ^10}{"Armor Rating" : ^15}')
            for key, value in inventory.player_armor.items():
                print(f'{key : <18}{value.price : ^10}{value.tier : ^10}{value.armor_rating : ^15}')
            item_selection(inventory.sell_armor)
    elif command == 2:
        if bool(inventory.player_weapons) == False:
            print("Your Weapon inventory is empty.\n")
            sell_items()
        else:
            print(f"-- Main menu -> Sell items -> Weapons --")
            print(f'{"Name" : <18}{"Price" : ^10}{"Tier" : ^10}{"Avg. Damage" : ^15}')
            for key, value in inventory.player_weapons.items():
                avg_damage = (value.min_dmg + value.max_dmg) / 2
                print(f'{key : <18}{value.price : ^10}{value.tier : ^10}{avg_damage : ^15.1f}')
            item_selection(inventory.sell_weapon)

def available_gold():
    """ Prints the vendor's and player's gold balance. """
    print(f"The vendor has {vendor.vendor_gold.gold} gold.")
    print(f"You have {inventory.player_gold.gold} gold.\n")

def input_check():
    """ Checks if the input is a valid integer. """
    try:
        command = int(input("Enter a choice: "))
        print("")
        return command
    except ValueError:
        print("")
        return None

def player_input():
    """ Asks the player for an input and calls relevant functions based on the input. """
    allowed_input = [0, 1, 2, 3]
    command = input_check()
    if command not in allowed_input:
        print("Wrong choice, only presented numbers allowed.\n")
        player_input()
    elif command == 0:
        print('"Goodbye, traveler!"')
    elif command == 1:
        buy_items()
    elif command == 2:
        sell_items()
    elif command == 3:
        available_gold()
        trade_main()

def trade_main():
    """ Prints available commands to the player to operate the main trade interaction. """
    print("-- Main menu --")
    print("0 : Exit game")
    print("1 : Buy items")
    print("2 : Sell items")
    print("3 : Available gold\n")
    player_input()

def trade():
    """ Starts trading with the vendor. Prints welcoming message. """
    print('"Welcome to my shop, traveler! Buying, selling, or just looking around? You won\'t find better prices anywhere else! Now, how can I help?"\n')
    trade_main()