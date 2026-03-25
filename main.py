import click
from bot.orders import place_limit_order, place_market_order
from bot.validators import validate_order

@click.command()
@click.option('--symbol', required=True, help='Trading pair (e.g., BTCUSDT)')
@click.option('--side', required=True, help='BUY or SELL')
@click.option('--type', 'order_type', required=True, help='MARKET or LIMIT')
@click.option('--qty', type=float, required=True, help='Quantity')
@click.option('--price', type=float, default=None, help='Price (required for LIMIT)')

def main(symbol, side, order_type, qty, price):
    try:
        # Validate input
        validate_order(symbol, side, order_type, qty, price)

        print("\nOrder Summary:")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {qty}")
        if order_type == "LIMIT":
            print(f"Price: {price}")

        # Place order
        if order_type == "MARKET":
            response = place_market_order(symbol, side, qty)
        else:
            response = place_limit_order(symbol, side, qty, price)

        print("\nOrder Placed Successfully!")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("\nError:", str(e))


if __name__ == "__main__":
    main()