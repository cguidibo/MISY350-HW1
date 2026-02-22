inventory = [
    {"item_id": 1, "name": "Espresso", "unit_price": 2.50, "stock": 40},
    {"item_id": 2, "name": "Latte", "unit_price": 4.25, "stock": 25},
    {"item_id": 3, "name": "Cold Brew", "unit_price": 3.75, "stock": 30},
    {"item_id": 4, "name": "Mocha", "unit_price": 4.50, "stock": 20},
    {"item_id": 5, "name": "Blueberry Muffin", "unit_price": 2.95, "stock": 18},
]

orders = [
    {
    "Order_ID": "Order_101",
     "item_id": 2,
     "Quantity": 2,
     "Status": "Placed",
     "Total": 8.50
    },
    {
        "Order_ID": "Order_102",
     "item_id": 3,
     "Quantity": 1,
     "Status": "Placed",
     "Total": 3.75
     }
]

#Create
# Query 1: Place a new order for an item and quantity.


# 1. Input:
# ...
item_id = int(input("Enter the Item ID to order: "))
quantity = int(input("Enter the quantity: "))
exist = False


# 2. Process: [Name process here, e.g. "Validate and create order"]
# ...

if 



# 3. Output:
# ...






#Read
# Query 2: View all orders placed for a particular item.
# Prompt the user for the item name.

# 1. Input:
# ...
search_item = input("Enter the item name to search (e.g. 'Latte'): ")



# 2. Process: [Name process here, e.g. "Find orders for item"]
# ...




# 3. Output:
# ...



# Query 3: Total number of orders placed for "Cold Brew".

# 1. Input:
# ...




# 2. Process: [Name process here, e.g. "Count orders"]
# ...




# 3. Output:
# ...




#Update
# Query 4: Update item stock quantity by item id.

# 1. Input:
# ...
item_id = int(input("Enter ID of item to update: "))
new_stock = int(input("Enter new stock quantity: "))



# 2. Process: [Name process here, e.g. "Validate and update stock"]
# ...




# 3. Output:
# ...





#Remove/Delete
# Query 5: Cancel an order and restore stock.

# 1. Input:
# ...
cancel_order_id = input("Enter Order ID to cancel: ")


# 2. Process: [Name process here, e.g. "Cancel order"]
# ...




# 3. Output:
# ...



