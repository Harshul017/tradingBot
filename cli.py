import argparse
from bot.orders import place_order
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser(description="Trading Bot CLI")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

result = place_order(
    args.symbol,
    args.side,
    args.type,
    args.quantity,
    args.price
)

print("\n====== ORDER SUMMARY ======")
print(f"Symbol: {args.symbol}")
print(f"Side: {args.side}")
print(f"Type: {args.type}")
print(f"Quantity: {args.quantity}")

if args.type == "LIMIT":
    print(f"Price: {args.price}")

print("\n====== RESPONSE ======")

if "error" in result:
    print("❌ Order Failed:", result["error"])
else:
    print("✅ Order Success")
    print(f"Order ID: {result.get('orderId')}")
    print(f"Status: {result.get('status')}")
    print(f"Executed Qty: {result.get('executedQty')}")
    print(f"Avg Price: {result.get('avgPrice')}")