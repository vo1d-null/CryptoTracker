# app/gui.py
import wx
from app.api import get_crypto_prices


class CryptoPriceFrame(wx.Frame):
    def __init__(self, parent, title):
        super(CryptoPriceFrame, self).__init__(parent, title=title, size=(400, 300))

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)

        title_label = wx.StaticText(panel, label="Cryptocurrency Prices")
        sizer.Add(title_label, pos=(0, 0), span=(1, 2), flag=wx.ALIGN_CENTER_VERTICAL)

        update_button = wx.Button(panel, label="Update Prices")
        sizer.Add(update_button, pos=(1, 0), flag=wx.ALIGN_LEFT)

        self.result_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)  # Store as an instance attribute
        sizer.Add(self.result_text, pos=(2, 0), span=(1, 2), flag=wx.EXPAND)

        # Bind the button click event to the update_prices method
        update_button.Bind(wx.EVT_BUTTON, self.update_prices)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)

        panel.SetSizerAndFit(sizer)
        self.update_prices()

    def update_prices(self, event=None):
        prices = get_crypto_prices()
        self.result_text.Clear()

        for crypto, data in prices.items():
            price = data.get("usd","N/A")
            self.result_text.AppendText(f"{crypto}: ${price}\n")

        if event is None:
            wx.CallLater(300000, self.update_prices)
