"""Formatting utilities for numbers and strings."""


def format_currency(amount: float, currency: str = "USD") -> str:
    symbols = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥"}
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"


def format_percentage(value: float, decimals: int = 1) -> str:
    return f"{value * 100:.{decimals}f}%"
