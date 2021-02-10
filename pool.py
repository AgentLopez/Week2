# 12 Pool Tables
# See them all
# Write when closing table to file
import math
import datetime
now = datetime.datetime.now()

# Setting New Time For Table
from datetime import timedelta
now = datetime.datetime.now()
hour = now.strftime("%H")
minute = now.strftime("%M")
second = now.strftime("%S")
month = now.strftime("%m")
day = now.strftime("%d")
year = now.strftime("%Y")

date = now.strftime("%m-%d-%Y")

#Elapsed Time Table
# elapsed_time = ""


#Table Array
tables = []
awake = True

class Pooltable:
    def __init__(self, occupied = "Available", second = "00", minute = "00", hour = "00", day = "00", month = "00", year = "0000" ):
        self.occupied = occupied
        self.second = second
        self.minute = minute
        self.hour = hour
        self.day =  day
        self.month = month
        self.year = year
  
#Create Tables for Program Start
for i in range(0, 12):
    new_table = Pooltable()
    tables.append(new_table)

def menu():
    print("\n-------------------------\n")
    print("Press 1 To Assign a Table")
    print("Press 2 to Close a Table")
    print("Press q to quit\n")
 
def view_tables():
    i = 1
    print("\n\n***** Pool Tables *****\n")
    for items in tables:
        if items.occupied == "Available":
            print(f"Table {i} is {items.occupied}")
        else:
            print(f"Table {i} is {items.occupied} since {items.hour}:{items.minute} Current Tab: ${cost_now(i - 1)}")
        i += 1

def close_table():
    try:
        closing = int(input("Which Pool Table are we Closing? >"))
        table_number = closing - 1
        date = now.strftime("%m-%d-%Y")
        eltime = tardis(table_number)
        f= open(f"{date}.txt", "a")
    
        f.write(f"Table {closing}, {tables[table_number].hour}:{tables[table_number].minute}, {hour}:{minute}, Occupied for {eltime} and Cost ${cost_now(table_number)}")
        f.close()
    
        # print(tardis(table_number))

        vacate_table = Pooltable("Available")
        tables[table_number] = vacate_table
    except:
        print("\nWoops, Let's start from the top!\n")


def assign_table():
    try:
        assign = int(input("What Pool Table are we Assigning? >"))
        if tables[assign - 1].occupied == "Occupied":
            print("Table is occupied, Can Not Assign")
        else:
            new_table = Pooltable("Occupied", second, minute, hour, day, month, year)
            tables[assign - 1] = new_table
    except:
        print("\nWoops, Let's start from the top!\n")

def tardis(table):
    refresh_time()
    start_time = datetime.datetime(year = int(tables[table].year), month = int(tables[table].month), day = int(tables[table].day), minute = int(tables[table].minute)) #, second = int(tables[table].second)
    end_time = datetime.datetime(year = int(year), month = int(month), day = int(day), minute = int(minute)) #, second = int(second)
    # print(end_time)
    # print(start_time)
    # elapsed_time = end_time - start_time
    # print(elapsed_time)
    return end_time - start_time

def cost_now(table):
    time_to_charge = tardis(table)
    time_test = str(time_to_charge)
    seperate = time_test.split(":")
    total_minutes = int(seperate[1]) + int((seperate[0] * 60))
    cost = (total_minutes / 60) * 30
    formatted_cost = "{0:.2f}".format(cost)
    return formatted_cost
    # print(total_minutes)
    # print(cost)
    # print(seperate)
    # print(time_to_charge)
    # print(type(time_test))
    # print(type(time_to_charge))
    
    # print(seperate)


def refresh_time():
    now = datetime.datetime.now()
    global hour
    global minute
    global second
    global month
    global day
    global year
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    month = now.strftime("%m")
    day = now.strftime("%d")
    year = now.strftime("%Y")
    

while awake == True:
    view_tables()
    menu()
    option = input("What Shall We Do? >")
    if option == "1":
        refresh_time()
        assign_table()
    elif option == "2":
        refresh_time()
        close_table()
    elif option == "q":
        awake = False
    # elif option == "c":
    #     ss = int(input("What Table Number?"))
    #     cost_now(ss)
    else:
        print("Not A Valid Choicem, Please Try Again")




