# This repository was created by Ali Hajian as part of university coursework.
import json


carts = {}

def AddItem():
    Kala = input("enter Products Name: ")
    price = int(input("Enter The Price: "))
    carts[Kala]=price
    print(f"Name: {Kala} and price: {price}")

def show_carts():
    if not carts:
        print("Insufficient inventory")
    else:
        print("List Products")
        total = 0
        for i, (name, price) in enumerate(carts.items(), start=1):
            print(f"{i}. Product Name: {name:<10} || Price: {price}")
            total += price


        discount_rate = 0.02  
        tax_rate = 0.10     

        discount = total * discount_rate
        taxed_total = (total - discount) * (1 + tax_rate)

        print(f"\n Total Amount: {total}")
        print(f"Discount (2%): {discount}")
        print(f"Tax (10%): {(total - discount) * tax_rate:.2f}")
        print(f"Final Total: {taxed_total:.2f}")

def remove_item():
    Kala = input("Plz name products: ")
    if Kala in carts:
       del carts[Kala]
       print("Delete Item")
    else:
        print(f"Noting Item: {Kala}")
def Edit_item():
    if not carts:
        print("Empety")
        return
    Kala = input("Enter Name Product: ")
    if Kala in carts:
        
        new = int(input("Enter New Price: "))
        carts[Kala] = new
        print(f"{Kala} the updated! new price {new}")
    else:
        print(f"Product '{Kala}' not found.")
def Save_Item():
    with open("save.json","w") as file:
        json.dump(carts,file)
    print("Data saved successfully")

def load_items():
    global carts
    try:
        with open("save.json", "r") as file:
           
            carts = json.load(file)
            print("Data loaded successfully")
    except FileNotFoundError:
        carts = {}
        print("File not found. Starting with empty data.")
    except json.JSONDecodeError:
        carts = {}
        print("File is empty or invalid. Starting fresh.")


load_items()
while True:


    print("\n Menu:")
    print("1. Add item")
    print("2. Show Item")
    print("3. remove Item")
    print("4. Edit Item")
    print("5. Save Item")
    print("6. Exit")

    choice = int(input("choice?"))

    match choice:
        case 1:
            AddItem()
        case 2:
            show_carts()
        case 3:
            remove_item()
        case 4:
             Edit_item()
        case 5:
            Save_Item()
        case 6:
             print("Goodluck")
             break
        case _:
            print("not valid")

   

