# 12 Pool Tables
# See them all
# Write when closing table to file
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
elapsed_time = ""


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
    print("-------------------------")
    print("Press 1 To Assign a Table")
    print("Press 2 to Close a Table")
    print("Press q to quit")
 
def view_tables():
    i = 1
    print("***** Pool Tables *****")
    for items in tables:
        if items.occupied == "Available":
            print(f"Table {i} is {items.occupied}")
        else:
            print(f"Table {i} is {items.occupied} since {items.hour}:{items.minute}")
        i += 1

def close_table():
    closing = int(input("Which Pool Table are we Closing? >"))
    table_number = closing - 1
    date = now.strftime("%m-%d-%Y")
    eltime = tardis(table_number)
    f= open(f"{date}.txt", "a")
    

    f.write(f"Table {closing}, {tables[table_number].hour}:{tables[table_number].minute}, {hour}:{minute}, Occupied for {eltime}\n")
    f.close()
    
    
    # print(tardis(table_number))

    vacate_table = Pooltable("Available")
    tables[table_number] = vacate_table


def assign_table():
    
    assign = int(input("What Pool Table are we Assigning? >"))
    if tables[assign - 1].occupied == "Occupied":
        print("Table is occupied, Can Not Assign")
    else:
        new_table = Pooltable("Occupied", second, minute, hour, day, month, year)
        tables[assign - 1] = new_table

def tardis(table):
    refresh_time()
    start_time = datetime.datetime(year = int(tables[table].year), month = int(tables[table].month), day = int(tables[table].day), minute = int(tables[table].minute)) #, second = int(tables[table].second)
    end_time = datetime.datetime(year = int(year), month = int(month), day = int(day), minute = int(minute)) #, second = int(second)
    # print(end_time)
    # print(start_time)
    elapsed_time = end_time - start_time
    # print(elapsed_time)
    return end_time - start_time

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
    else:
        print("Not A Valid Choicem, Please Try Again")




