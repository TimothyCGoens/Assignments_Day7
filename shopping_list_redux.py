
from store import Store
from items import GroceryItem


stores = []

def view_all_stores():
    # store is not a string, but an object of the Store class
    for store in stores:
        print(f"""
        {stores.index(store) + 1}) {store.name} - {store.items}
        """)

def show_menu():
    print("""
    -------------------------------
    Press 1 to add store.
    Press 2 to add item to a store.
    Press 3 to view all stores.
    Press q to quit.
    -------------------------------
    """)

def add_store():
    name = input("""
    Enter store name:
    """)
    store = Store(name)
    stores.append(store)

def add_item():
    try:
        store_choice = int(input("""
    Press the number of the store you wish to shop from:
    """))
        item = input("""
    What would you like to buy and how many do you need?
    (Ex: Pizza 1)
    """)
        for store in stores:
            if store_choice == stores.index(store) + 1:
                store.items.append(GroceryItem(item))
        else:
            print("""
    That store doesn't exist!
    """)
    except ValueError:
        print("""
    DOH!  You're supposed to enter a NUMBER silly. Please try again:
        """)

user_input = ""

while user_input != "q":
    show_menu()
    user_input = input("""
    Enter your choice: """)

    if user_input == "1":
        add_store()
    elif user_input == "2":
        add_item()
    elif user_input == "3":
        view_all_stores()
    else:
        print("""
    Thank you and have a great day!
        """)
