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

for item in inventory:
    if item["item_id"] == item_id:
        exists = True
        if item["stock"] >= quantity:
            item["stock"] -= quantity
            total_price = quantity* item["unit_price"]

            new_order = {
                "Order_ID": "Order_103",
                "item_id": item["item_id"],
                "Quantity": quantity,
                "Status": "Placed",
                "Total": total_price
            }
            orders.append(new_order)
            print("Order Placed Successfully!")
        else:
            print("Not Enough Stock Available.")
            break
if not exists:
        print("Item Not Found.")


# 3. Output:
# ...
print(new_order)


#Read
# Query 2: View all orders placed for a particular item.
# Prompt the user for the item name.

# 1. Input:
# ...
search_item = input("Enter the item name to search (e.g. 'Latte'): ").capitalize()
exsits = False
matching_id = None
found_orders = False

# 2. Process: [Name process here, e.g. "Find orders for item"]
# ...
for item in inventory:
     if item["name"] == search_item.lower():
          exists = True
          matching_id = item["item_id"]
          break
if matching_id is not None:
     for order in orders:
          if order["item_id"] == matching_id:
               found_orders = True
               print(f"Order ID: {order['order_id']}, Quantity: {order['quantity']}, Total: {order['total']:.2f}, Status: {order['status']}")
if not found_orders:
                print("No orders found for this item.")
else:
     print("Item not found in inventory.")   

# 3. Output:
# ...




# Query 3: Total number of orders placed for "Cold Brew".
# 1. Input:
# ...
exists = False
matching_id = None

# 2. Process: [Name process here, e.g. "Count orders"]
# ...

for item in inventory:
      if item["name"] == "Cold Brew":
            exists = True
            matching_id = item["item_id"]
            break
counter = 0
for order in orders:
      if order["item_id"] == matching_id:
            counter+=1

# 3. Output:
# ...
print(f"Total Number of orders placed for Cold Brew: {counter}")

#Update
# Query 4: Update item stock quantity by item id.

# 1. Input:
# ...
item_id = int(input("Enter ID of item to update: "))
new_stock = int(input("Enter new stock quantity: "))
update = False

# 2. Process: [Name process here, e.g. "Validate and update stock"]
# ...

for item in inventory:
      if item["item_id"] == item_id:
            item["stock"] = new_stock
            update = True
            break

# 3. Output:
# ...
if update:
      print("Stock has been successfully updated!")
else:
      print("Item not found.")


#Remove/Delete
# Query 5: Cancel an order and restore stock.

# 1. Input:
# ...
cancel_order_id = input("Enter Order ID to cancel: ")
found = False

# 2. Process: [Name process here, e.g. "Cancel order"]
# ...

for order in orders:
      if order["Order_ID"] == cancel_order_id:
            found = True
            if order["Status"] == "placed":
                  order["Status"] = "canceled"

                  item_id = order["item_id"]
                  quantity = order["Quantity"]
for item in inventory:
      if item["item_id"] == order["item_id"]:
            item["stock"] += order["Quantity"]
            break
      print("Order Canceled and Stock Restored Successfully!")

else:
    print("Order not found or already canceled.")


# 3. Output:
# ...
if not found:
      print("Order not found.")




