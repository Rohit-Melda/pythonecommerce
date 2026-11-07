PRODUCTS = {
    "1": {"name": "Notebook", "price": 80.0},
    "2": {"name": "Pen Pack", "price": 50.0},
    "3": {"name": "USB Drive", "price": 450.0},
}

def main():
    cart = {}
    while True:
        print("\n--- ROHIT'S MINI STORE ---")
        for key, item in PRODUCTS.items():
            print(f"{key}. {item['name']} - ₹{item['price']:.2f}")
        print("0. Checkout")
        choice = input("Choose a product: ").strip()
        if choice == "0":
            break
        if choice not in PRODUCTS:
            print("Invalid product number.")
            continue
        try:
            qty = int(input("Quantity: "))
            if qty < 1:
                print("Quantity must be at least 1.")
                continue
        except ValueError:
            print("Enter a whole number.")
            continue
        cart[choice] = cart.get(choice, 0) + qty
        print("Added to cart.")

    print("\n--- RECEIPT ---")
    total = 0
    for key, qty in cart.items():
        item = PRODUCTS[key]
        line_total = item["price"] * qty
        total += line_total
        print(f"{item['name']} x {qty}: ₹{line_total:.2f}")
    print(f"Total: ₹{total:.2f}")
    print("Demo only — no payment was taken.")

if __name__ == "__main__":
    main()
