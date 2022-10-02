# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, amount in inventory.items():
        item_total = item_total + amount
        print(str(item) + ' ' + str(amount))
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for addedItem in addedItems:
        inventory.setdefault(addedItem, 0)
        inventory[addedItem] = inventory[addedItem] +1
    return inventory 

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = addToInventory(stuff, dragonLoot)

displayInventory(stuff)