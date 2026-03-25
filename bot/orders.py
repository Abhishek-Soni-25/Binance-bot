from bot.client import get_client
from bot.logger import logger

client = get_client()

def place_market_order(symbol, side, quantity):
    try:
        
        logger.info(f"Placing MARKET order | Symbol={symbol} | Side={side} | Qty={quantity}")

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

        logger.info(
            f"Order SUCCESS | ID={response.get('orderId')} | "
            f"Status={response.get('status')} | "
            f"ExecutedQty={response.get('executedQty')} | "
            f"AvgPrice={response.get('avgPrice')}"
        )

        return response

    except Exception as e:
        logger.error(f"Order FAILED | Symbol={symbol} | Side={side} | Reason={str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(f"Placing LIMIT order | Symbol={symbol} | Side={side} | Qty={quantity} | Price={price}")

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )

        logger.info(
            f"Order SUCCESS | ID={response.get('orderId')} | "
            f"Status={response.get('status')} | "
            f"ExecutedQty={response.get('executedQty')} | "
            f"AvgPrice={response.get('avgPrice')}"
        )

        return response

    except Exception as e:
        logger.error(f"Order FAILED | Symbol={symbol} | Side={side} | Reason={str(e)}")
        raise