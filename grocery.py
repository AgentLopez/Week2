stores = []
start = True

class Store:
    def __init__(self, storename):
        self.store = storename
        self.address = ""
        self.list = []


class Item:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

def choices():
    print("Press 1 to Add Store")
    print("Press 2 to Add to Store Shopping List")
    print("Press 3 to See Your List(s)")
    print("Press q to quit")

def add_store():
    new_store = input("What store are we going to be shopping at? > ")
    add_store = Store(new_store)
    stores.append(add_store)

def print_stores():
    i = 1
    for values in stores:
       
       print(f"{i} {values.store}")
       i += 1
    #    for items in stores[i].list:
    #    print(items.stores[i].list)

def print_items():
    print("*** List ***")
    i=0
    for values in stores:
         
        print(f"\n{i + 1} {values.store}\n")
        
        for items in stores[i].list:
            print(f"{items.title} ${items.price} Qty {items.quantity}")
        
        i += 1

def add_item():
    # if len(stores == False):
    #     print("You need to add a store first.")
    # else:
        print_stores()
        add_to = int(input("What Store Are We Adding To? > "))
        item = input("What item are we adding? > ")
        price = input("How much is the item? > ")
        quantity = input("How many are we buying? > ")
        new_item = Item(item, price, quantity)
        stores[add_to - 1].list.append(new_item)
        # print(stores[add_to - 1].list[0])

while start == True:
    choices()
    do = input("\nWhat Would you like to do? >")
    if do == "1":
        add_store()
    elif do == "2":
        add_item()
    elif do == "3":
        print_items()
    elif do == "q":
        start = False
    else:
        print("\nThat was not a valid entry. Try again.\n")




