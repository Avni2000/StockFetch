"""
StockFetch - Think Neofetch for stocks

A CLI tool for displaying stock information with ASCII art logos.
"""

from .Pyfinance import ticker, make_ascii, validate_ticker

__version__ = "1.0.0"
__all__ = ["ticker", "make_ascii", "validate_ticker"]
