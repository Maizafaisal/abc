class Cafe:
    def __init__(self):
        self.menu = {}
        self.orders = {}

    def add_item(self, name, price):
        self.menu[name] = price

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:}")

    def place_order(self, order_no, items):
        self.orders[order_no] = items

    def display_orders(self):
        print("Orders:")
        for order_no, items in self.orders.items():
            print(f"Order no: {order_no}")
            print("Items:")
            for item in items:
                item = item.strip().lower()
                if item in [i.lower() for i in self.menu.keys()]:
                    print(f"- {item} (${self.menu[[i for i in self.menu.keys() if i.lower() == item][0]]:})")
                else:
                    print(f"- {item} (Not found in menu)")
            print()

    def calculate_bill(self, order_no):
        bill = 0
        for item in self.orders[order_no]:
            item = item.strip().lower()
            if item in [i.lower() for i in self.menu.keys()]:
                bill += self.menu[[i for i in self.menu.keys() if i.lower() == item][0]]
            else:
                print(f"Item '{item}' not found in menu.")
        print(f"Bill for Order {order_no}: ${bill:.2f}")


def main():
    my_cafe = Cafe()  

    while True:
        print("Cafe Management System")
        print("1.Add Item to Menu")
        print("2.Display Menu")
        print("3.Place Order")
        print("4.Display Orders")
        print("5.Calculate Bill")
        print("6.Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num_items = int(input("Enter number of items:"))
            for i in range(num_items):
                item_name = input(f"Enter Item {i+1} Name: ")
                while True:
                    try:
                        price = float(input(f"Enter Item {i+1} Price: "))
                        if price < 0:
                            print("Price cannot be negative.")
                        else:
                            break
                    except ValueError:
                        print("Invalid price. Please enter a number.")
                my_cafe.add_item(item_name, price)
        elif choice == "2":
            if len(my_cafe.menu) == 0:
                print("Menu is empty.")
            else:
                print("Menu:")
                for item, price in my_cafe.menu.items():
                    print(f"{item}: ${price:}")
        elif choice == "3":
            order_no = input("Enter Order no: ")
            items = input("Enter Items (comma-separated): ").split(',')
            my_cafe.place_order(order_no, items)
        elif choice == "4":
            if len(my_cafe.orders) == 0:
                print("No orders placed.")
            else:
                my_cafe.display_orders()
        elif choice == "5":
            order_no = input("Enter Order no: ")
            my_cafe.calculate_bill(order_no)
        elif choice == "6":
            break


if __name__ == "__main__":
    main()
    
