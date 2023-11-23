import tkinter as tk

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Web App")

        # Create and pack widgets for the home page
        self.create_widgets()

    def create_widgets(self):
        # Welcome message label
        welcome_label = tk.Label(self.root, text="Welcome to Our Restaurant!", font=("Helvetica", 16))
        welcome_label.pack(pady=20)

        # Quick links buttons
        button_frame = tk.Frame(self.root)
        buttons = [
            ("Food Order", self.open_food_order),
            ("Breakfast", self.open_breakfast),
            ("Lunch", self.open_lunch),
            ("Snacks", self.open_snacks),
            ("Sunday Special", self.open_sunday_special),
            ("Reviews", self.open_reviews),
            ("Dine Out", self.open_dine_out),
            ("Drinks", self.open_drinks),
        ]

        for text, command in buttons:
            button = tk.Button(button_frame, text=text, width=15, height=2, command=command)
            button.pack(side=tk.LEFT, padx=10)

        button_frame.pack(pady=20)

    # Functions to open different sections
    def open_food_order(self):
        print("Opening Food Order section")

    def open_breakfast(self):
        print("Opening Breakfast section")

    def open_lunch(self):
        print("Opening Lunch section")

    def open_snacks(self):
        print("Opening Snacks section")

    def open_sunday_special(self):
        print("Opening Sunday Special section")

    def open_reviews(self):
        print("Opening Reviews section")

    def open_dine_out(self):
        print("Opening Dine Out section")

    def open_drinks(self):
        print("Opening Drinks section")


if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()
