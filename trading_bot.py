import json
import logging
import signal
import sys
from binance import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

# Configure logging
logging.basicConfig(filename='trading_bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce='GTC'
                )
            else:
                logging.error("Invalid order type")
                return None
            
            logging.info(f"Order placed: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"API error: {e.message}")
            return None
        except BinanceOrderException as e:
            logging.error(f"Order error: {e.message}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return None

    def run(self):
        try:
            symbol = input("Enter trading pair (e.g., BTCUSDT): ")
            side = input("Enter order side (BUY/SELL): ").upper()
            order_type = input("Enter order type (MARKET/LIMIT): ").upper()
            quantity = float(input("Enter quantity: "))
            price = None
            
            if order_type == 'LIMIT':
                price = float(input("Enter limit price: "))
            
            order = self.place_order(symbol, side, order_type, quantity, price)
            if order:
                print("Order details:", order)
            else:
                print("Failed to place order.")
        except Exception as e:
            logging.error(f"Error in run method: {e}")

def signal_handler(sig, frame):
    logging.info("Shutting down the bot gracefully...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    
    # Use the provided API key and secret
    API_KEY = 'Enter your'
    API_SECRET = 'Enter your'
    
    bot = BasicBot(API_KEY, API_SECRET)
    bot.run()
