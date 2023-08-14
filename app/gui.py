# app/gui.py
import wx
from app.api import get_crypto_prices  # Import the get_crypto_prices function


class CryptoPriceFrame(wx.Frame):
    def __init__(self, parent, title):
        super(CryptoPriceFrame, self).__init__(parent, title=title, size=(400, 300))

        panel = wx.Panel(self)

        self.label = wx.StaticText(panel, label="Cryptocurrency Prices", pos=(10, 10))
        self.update_button = wx.Button(panel, label="Update Prices", pos=(10, 40))
        self.result_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY, pos=(10, 70), size=(380, 180))

        # Bind the button click event to the update_prices method
        self.update_button.Bind(wx.EVT_BUTTON, self.update_prices)

        self.update_prices()

    def update_prices(self, event=None):
        prices = get_crypto_prices()
        self.result_text.Clear()

        for crypto, data in prices.items():
            price = data.get("usd", "N/A")
            self.result_text.AppendText(f"{crypto}: ${price}\n")

        if event is None:
            wx.CallLater(300000, self.update_prices)
