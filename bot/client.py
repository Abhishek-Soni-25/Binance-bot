from binance.client import Client
from config import API_KEY, SECRET_KEY

def get_client():
    client = Client(API_KEY, SECRET_KEY)
    
    # Set testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    
    return client