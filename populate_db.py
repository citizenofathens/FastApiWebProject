import sqlite3

connectinon = sqlite3.connect('app.db')
connectinon.row_factory = sqlite3.Row

cursor = connectinon.cursor()


cursor.execute("""
    SELECT symbol, company FROM stock
""")

rows = cursor.fetchall()
symbols = [row['symbol'] for row in rows]

cursor.execute("INSERT INTO stock (symbol, company) VALUES ('ADBE', 'Adobe Inc.')")
cursor.execute("INSERT INTO stock (symbol, company) VALUES ('VZ', 'Verizon')")
cursor.execute("INSERT INTO stock (symbol, company) VALUES ('Z', 'Zillow')")

# pip3 install alpaca-trade-api
# import alpaca_trade_api as tradeapi
#
# api = tradeapi.REST(APIKEY,APISECRETKEY,base_url ="https://paper-api.alpaca.markets" )
# assets  = api.list_assets()
#
# for asset in assets:
#     try:
#
#         # if asset.symbol not in symbols:
#         #     print(f"Added a new stock {asset.symbol} {asset.name}")
#         if asset.status =='active' and asset.tradable:
#             cursor.execute("INSERT INTO stock (symbol, company) VALUES (?,?)" , (asset.symbol, assets.name))
#     except Exception as e:
#         print(asset.symbol)
#         print(e)

connectinon.commit()