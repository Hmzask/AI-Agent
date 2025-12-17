from langchain.tools import tool
from datetime import datetime
import requests


@tool
def get_weather(param: str) -> str:
    """Get weather.""" # This works as Description for the model.
    return "It is very cold in {city}"

@tool
def get_capital(country: str) -> str:
    """Get the capital of a country."""
    if country.lower() == "india":
        return "New Delhi is the capital of India."
    return "I don't know the capital of that country."

@tool
def get_addition(number1: int, number2: int) -> int:
    """Add two numbers."""
    return number1 + number2

@tool
def get_datetime() -> str:
    """Get the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def get_crypto(param: str) -> str:
    """Fetch real-time data from an external API."""
    
    symbols = ["BTC-USD","SOL-USD","ETH-USD","XRP-USD","USDT-USD","USDC-USD"
               ,"BNB-USD","AVAX-USD","TRX-USD"]
    
     # Coindesk crypto API
    url = "https://data-api.coindesk.com/index/cc/v1/latest/tick"
    params = {
        "market": "cadli",
        "instruments": ",".join(symbols),
        "apply_mapping": "true"
    }
    response = requests.get(url, params=params)
    return response.json()

tools = [get_weather, get_capital, get_addition,get_datetime,get_crypto]