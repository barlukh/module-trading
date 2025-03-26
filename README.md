# Vendor Trading

<p align="center">
    <img width="1000" src="screenshot.png" alt="screenshot">
</p>

## About
Module for simulating a trading interaction. There is no graphical user interface, only text-based presentation in terminal.
The main functionality is the interaction between a fictional / fantasy vendor and a user (player) to buy and sell items.

## Functionality
- Items are predefined, but can be manually edited by the player in their respective .csv files. There are separate files for Armor and Weapons. These files can be therefore manipulated externally to add or remove items.
- Module 'classes' serves as blueprint module for classes of different items (Gold, Armor and Weapons).
- Armor and Weapons Class Objects inherit attributes from the parent Item class: name, price, tier. Both child classes also add their own attributes: Armor adds armor_rating and Weapons add their min_damage and max_damage.
- The 'vendor' module takes all the prewritten entries from .csv files, runs them through 'classes' and creates dictionaries for respective items.
- Vendor dictionaries contain all the items given by .csv files as Class Objects, under the key of the name of the item. Dictionaries are also separated for Armor and Weapons.
- With this setup, the 'vendor' module serves as a base shop where the player can buy and sell items.
- The 'inventory' module has its own dictionaries for Armor and Weapons, where the player owned items are stored. It also has all the main functions to manipulate these items (buy_...() and sell_...()).
- Module 'inventory' also manipulates vendor's and player's gold according to the transaction taking place.
- Trading happens through the 'trade' module, which contains the main written user interface and calls relevant functions based on the player's input.
- The input is protected, so if the player enters a wrong input, the module doesn't raise an error, but rather reminds the player of only allowed inputs.

## Installation
- Ensure Python is installed on your system.<br>
- Use pip to install all required packages listed in requirements.txt (pip install -r requirements.txt).<br>
- Variable default_path in the vendor.py must be set to the directory where the .csv files are located on the computer.
- Execute the main script to run the program (python main.py).