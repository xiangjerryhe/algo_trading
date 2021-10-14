import pandas as pd

symbol_chart = pd.DataFrame([
   ["S&P 500 atm implied vol","^VIX", None],
   ["Nasdaq 100 atm implied vol","^VXN",None],
   ["Korea stock index / Kospi", "^KS11", None],
   ["Hong Kong stock index /Hang Seng", "^HSI", None],
   ["Samsung", "005930.KS", None], 
   ["Sk Hynix", "000660.KS", None],
   ["S&P Futures /Dec 2021","ES=F",'/ESZ21'],
   ["Dow Futures /Dec 2021", "YM=F", '/YMZ21'],
   ["Nasdaq Futures /Dec 2021","NQ=F", "/NQZ21"],
   ["Russel Futures /Dec 2021", "RTY=F", "/RTYZ21"],
   ["2 yr Treasury Futures /Dec 2021","ZT=F","/ZTZ21"],
   ["5 yr Treasury Futures /Dec 2021", "ZF=F","/ZFZ21"],
   ["5 yr Treasury Yield", "^FVX", None],
   ["10 yr Treasury Futures /Dec 2021", "ZN=F", "/ZNZ21"],
   ["10 yr Treasury Yield", "^TNX", None],
   ["30 yr Treasury Futures /Dec 2021","ZB=F",  "/ZBZ21"],
   ["30 yr Treasury Yield","^TYX", None],
   ["Copper Futures /Dec 2021", "HG=F","/HGZ21"],
   ["Iron Futures /Dec 2021", "HG=F","/HGZ21"],
   ["WTI Oil Futures /Dec 2021",'CL=F', '/CLZ21'],
   ["Natural Gas Futures /Nov 2021","NG=F", "NGZ21"],
   ["Cotton Futures /Dec 2021", "CT=F", ],
   ["Lumber Futures /Jan 2022","LBS=F",],
   ["Live Cattle Futures,Dec-2021", "LE=F", "LEZ21"]
   ["Corn Futures /Dec 2021", "ZC=F", ],
   ["Wheat Futures /Dec 2021", "ZW=F", ],
   ["Gold futures /Dec 2021", "GC=F","/GCZ21"],
   ["Aluminum Futures /Nov 2021", "ALI=F",], 
   ["Bitcoin", "BTC-USD", None]
], columns=['description', 'yfinance ticker symbol', 'TDAmeritrade ticker symbol'])
