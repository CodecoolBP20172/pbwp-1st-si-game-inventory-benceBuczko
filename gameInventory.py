# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification


# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    for i, k in inventory.items():
        print (str(k)+" "+i)
    print("Total number of items: "+str(sum(inventory.values())))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.update({i: 1})


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    l = dict(inventory)
    l.update({"item name": "count"})
    n1 = max(len(str(i)) for i in l.values())
    n2 = max(len(i) for i in l.keys())

    print("Inventory:")
    print("  "+" "*(n1-len("count"))+"count"+"    "+" "*(n2-len("item name"))+"item name")
    print("-"*(n1+n2+6))
    if order == "count,asc":
        c = sorted(inventory.items(), key=lambda x: x[1])
    elif order == "count,desc":
        c = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    else:
        c = list(inventory.items())
    for i in c:
        print("  "+" "*(n1-len(str(i[1])))+str(i[1])+"    "+" "*(n2-len(i[0]))+i[0])
    print("-"*(n1+n2+6))
    print("Total number of items: "+str(sum(inventory.values())))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    import csv
    with open(filename) as f:
        newitems = csv.reader(f)
        for row in newitems:
            add_to_inventory(inventory, row)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    import csv
    cuccok = []
    j = list(inventory.keys())
    for i in j:
        for k in range(inventory[i]):
            cuccok.append(i)
    print(cuccok)
    with open(filename, "w") as f:
        printitems = csv.writer(f)
        printitems.writerow(cuccok)
