
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
            DVD("Avengers", "Action", 70000)
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
        total = 0

        for dvd in self.cart:
            dvd.display()
            total += dvd.price

        print(f"Total: {total:,} VND")

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
