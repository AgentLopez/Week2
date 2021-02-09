stores = []
start = True

class Store:
    def __init__(self, storename, address):
        self.store = storename
        self.address = address
        self.list = []


class Item:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

def choices():
    print("Press 1 to Add Store")
    print("Press 2 to Add Shopping List")
    print("\nPress 3 to See Your List(s)")
    print("\nPress 4 to Delete a Store")
    print("Press 5 to Delete a Item from a Store")
    print("Press q to quit")

def add_store():
    new_store = input("What store are we going to be shopping at? > ")
    store_address = input("What is the address? > ")
    add_store = Store(new_store, store_address)
    stores.append(add_store)

def delete_store():
    print_stores()
    try:
        remove = int(input("Which Store are we Deleting? > "))
        del stores[remove - 1]
    except:
        print("That wasn't a number, back to the main menu!")

def delete_item():
    print_stores()
    try:
        storeindex = int(input("Which store has the item we're deleting?"))
        i=1
        for items in stores[storeindex - 1].list:
                print(f"{i} {items.title} ${items.price} Qty {items.quantity}")
                i += 1
        item_remove = int(input("Which item are we removing?"))
        del stores[storeindex - 1].list[item_remove -1]
    except:
        print("That wasn't a number, back to the main menu!")

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
        try:
            add_to = int(input("What Store Are We Adding To? > "))
            item = input("What item are we adding? > ")
            price = input("How much is the item? > ")
            quantity = input("How many are we buying? > ")
            new_item = Item(item, price, quantity)
            stores[add_to - 1].list.append(new_item)
        except:
            print("That wasn't a number, back to the main menu!")
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
    elif do == "4":
        delete_store()
    elif do == "5":
        delete_item()
    elif do == "q":
        start = False
    else:
        print("\nThat was not a valid entry. Try again.\n")




