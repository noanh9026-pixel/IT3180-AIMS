
class DVD:
    def __init__(self, title, category, price):
        self.title = title
        self.category = category
        self.price = price

    def display(self):
        print(f"{self.title} | {self.category} | {self.price:,} VND")


class AIMS:
    def __init__(self):
        self.dvds = [
            DVD("The Lion King", "Animation", 50000),
            DVD("Titanic", "Romance", 60000),
            DVD("Avengers", "Action", 75000)
        ]
        self.cart = []

    def show_dvds(self):
        print("\n--- DVD LIST ---")
        for dvd in self.dvds:
            dvd.display()

    def add_to_cart(self):
        self.show_dvds()
        title = input("Enter DVD title: ")

        for dvd in self.dvds:
            if dvd.title.lower() == title.lower():
                self.cart.append(dvd)
                print("Added to cart!")
                return

        print("DVD not found!")

    
    def show_cart(self):
        print("\n--- YOUR CART ---")

        if not self.cart:
            print("Your cart is empty!")
            return

        total = 0

        for dvd in self.cart:
            dvd.display()
            total += dvd.price

        quantity = len(self.cart)

        if quantity >= 3:
            discount_rate = 0.15
        elif quantity >= 2:
            discount_rate = 0.10
        else:
            discount_rate = 0

        discount = total * discount_rate
        final_total = total - discount

        print(f"Subtotal: {total:,.0f} VND")
        print(f"Discount: {discount_rate * 100:.0f}%")
        print(f"Discount amount: {discount:,.0f} VND")
        print(f"Final total: {final_total:,.0f} VND")


    def search_dvd(self):
        keyword = input("Enter DVD title to search: ")
        found = False

        for dvd in self.dvds:
            if keyword.lower() in dvd.title.lower():
                dvd.display()
                found = True

        if not found:
            print("DVD not found!")


def main():
    app = AIMS()

    while True:
        print("\n===== AIMS MENU =====")
        print("1. Show DVDs")
        print("2. Add DVD to cart")
        print("3. Show cart")
        print("4. Search DVD")
        print("0. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            app.show_dvds()
        elif choice == "2":
            app.add_to_cart()
        elif choice == "3":
            app.show_cart()
        elif choice == "4":
            app.search_dvd()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
