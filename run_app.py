# run_app.py
import wx
from app.gui import CryptoPriceFrame

if __name__ == "__main__":
    app = wx.App()
    frame = CryptoPriceFrame(None, "Crypto Price Tracker")
    frame.Show()
    app.MainLoop()
