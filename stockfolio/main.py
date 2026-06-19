stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 200
}

portfolio = {}
total_investment = 0

print("=" * 50)
print("        STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:

    stock_name = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Invalid Stock Name")
        continue

    try:
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0")
            continue

    except ValueError:
        print("❌ Please enter numbers only")
        continue

    investment = stock_prices[stock_name] * quantity

    portfolio[stock_name] = {
        "quantity": quantity,
        "investment": investment
    }

    total_investment += investment

print("\n" + "=" * 50)
print("           PORTFOLIO SUMMARY")
print("=" * 50)

for stock, details in portfolio.items():
    print(
        f"{stock} | Quantity: {details['quantity']} | Value: ${details['investment']}"
    )

print("\nTotal Investment Value: $", total_investment)

# Highest investment stock
if portfolio:

    highest_stock = max(
        portfolio,
        key=lambda x: portfolio[x]["investment"]
    )

    print("\n🏆 Top Investment Stock:", highest_stock)
    print(
        "Investment Value: $",
        portfolio[highest_stock]["investment"]
    )

    print("\n📊 Portfolio Distribution:")

    for stock, details in portfolio.items():
        percentage = (
            details["investment"] / total_investment
        ) * 100

        print(f"{stock}: {percentage:.2f}%")

# Save report to file
with open("portfolio_report.txt", "w") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=" * 40 + "\n\n")

    for stock, details in portfolio.items():
        file.write(
            f"{stock} | Quantity: {details['quantity']} | Value: ${details['investment']}\n"
        )

    file.write("\n")
    file.write(f"Total Investment Value: ${total_investment}\n")

    if portfolio:
        file.write(
            f"Top Investment Stock: {highest_stock}\n"
        )

print("\n✅ Report saved as portfolio_report.txt")
print("🎉 Thank you for using Stock Portfolio Tracker!")