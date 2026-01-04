import json, requests
CRYPTO_IDS = {"BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana"}
def load():
    try:
        with open("portfolio.json") as f: return json.load(f)["portfolio"]
    except: return []
def save(p):
    with open("portfolio.json", "w") as f: json.dump({"portfolio": p}, f)
    print("Saved")
def price(s):
    try:
        u = f"https://api.coingecko.com/api/v3/simple/price?ids={CRYPTO_IDS[s]}&vs_currencies=usd"
        return requests.get(u).json()[CRYPTO_IDS[s]]["usd"]
    except: return None
def show():
    p = load()
    if not p: print("Empty"); return
    for c in p:
        pr = price(c["symbol"])
        if pr: print(f"{c['symbol']}: ${pr} (bought at ${c['buy_price']})")
def add():
    p = load()
    s = input("Symbol: ").upper()
    a = float(input("Amount: "))
    b = float(input("Price: "))
    p.append({"symbol": s, "amount": a, "buy_price": b})
    save(p)
while True:
    print("1-View 2-Add 3-Exit")
    if input(">") == "1": show()
    elif input() == "2": add()
    elif input() == "3": break
