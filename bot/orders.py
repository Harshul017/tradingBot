def place_order(symbol, side, order_type, quantity, price=None):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        logging.info(f"REQUEST: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"RESPONSE: {order}")
        return order   # ✅ IMPORTANT

    except Exception as e:
        logging.error(f"ERROR: {str(e)}")
        return {"error": str(e)}   # ✅ ALWAYS return something