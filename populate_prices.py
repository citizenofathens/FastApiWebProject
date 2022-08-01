import alpaca_trade_api as tradeapi

api = tradeapi.REST(APIKEY,APISECRETKEY,base_url ="https://paper-api.alpaca.markets" )

barsets = api.get_barset(['AAPL','MSFT'],'day')


# loop over the keys in the barsets dictionary
for symbol in barsets:
    print(f"processing symbol {symbol}")

    for bar in barsets[symbol]:
        print(bar.t, bar.o, bar.h , bar.l , bar.c, bar.v)


minute_bars = api.polygon.historic_agg_v2('Z', 1, 'minute', _from='2022-07-01' , to='2022-08-01')
for bar in minute_bars:
    print(bar.timstamp, bar.open, bar.high , bar.low , bar.close)