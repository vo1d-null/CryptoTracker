# app/main.py
import tkinter as tk
from .api import get_crypto_prices


class CryptoPriceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Price Tracker")

        self.label = tk.Label(root, text="Cryptocurrency Prices")
        self.label.pack()

        self.update_button = tk.Button(root, text="Update Prices", command=self.update_prices)
        self.update_button.pack()

        self.result_text = tk.Text(root)
        self.result_text.pack()

        # Schedule the first update immediately
        self.update_prices()

    def update_prices(self):
        prices = get_crypto_prices()
        self.result_text.delete("1.0", tk.END)

        for crypto, data in prices.items():
            price = data.get("usd", "N/A")
            self.result_text.insert(tk.END, f"{crypto}: ${price}\n")

        # Schedule the next update after 5 minutes (300,000 milliseconds)
        self.root.after(300000, self.update_prices)
