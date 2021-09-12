from tda.auth import easy_client
from tda.client import Client
from tda.streaming import StreamClient
import asyncio

def make_webdriver():
    from selenium import webdriver
    driver = webdriver.Chrome("<directory where you downloaded chromedriver>")
    return driver

client = easy_client(
        '<your app token>',
        'http://localhost:8080',
        'token.pickle', make_webdriver)

stream_client = StreamClient(client, account_id=<your own account id as integer>)

async def update_SPY_momentum_indicator(futures_msg, equity_msg):
    ....

async def update_XLU_momentum_indicator(futures_msg, equity_msg):
    ....

async def process_level1_futures_mkt_data(msg):
    redis = aioredis.from_url("redis://localhost")
    await new_SPY_momentum_indicator, confidence_score = update_SPY_momentum_indicator(futures_msg=msg, equity_msg=None)
    if new_SPY_momentum_indicator != old_SPY_momentum_indicator:
        redis.set("momentum_indicator:SPY", new_SPY_momentum_indicator)
        redis.publish("momentumchange:SPY", confidence_score) 
    ...
    <similar lines of code for XLU>
    ...

async def process_level2_equity_book(msg, exchange):
    if exchange== 'NASDAQ':
        ...
    else: # exchange must be NYSE
        ...

async def process_level1_options_mkt_data(msg):
    if <time is before 9:51 am>:
         <update on redis the lowest bid/ask price for all strikes>

async def process_options_trades(msg):
    if <time is before 9:51 am>:
         <update on redis the lowest traded price for all strikes>

async def read_stream():
    await stream_client.login()
    await stream_client.quality_of_service(StreamClient.QOSLevel.EXPRESS)
    stream_client.add_level_one_futures_handler(process_level1_futures_mkt_data)
    stream_client.add_options_book_handler(process_level1_options_mkt_data)
    stream_client.add_listed_book_handler(lambda msg: process_level2_equity_book(msg, 'NYSE'))
    stream_client.add_nasdaq_book_handler(lambda msg: process_level2_equity_book(msg, 'NASDAQ'))
    stream_client.add_timesale_options_handler(process_options_trades)
    await stream_client.level_one_futures_subs(['/VXU21','/ZBU21','/ESU21', '/NQU21', '/YMU21'])
    await stream_client.level_one_option_subs(['SPY','XLU'])
    await stream_client.timesale_options_subs(['SPY','XLU'])
    await stream_client.listed_book_subs(['XLRE', 'SPY', 'XLU'])
    await stream_client.nasdaq_book_subs(['QQQ', 'AAPL', 'MSFT'])
    while True:
        await stream_client.handle_message()

asyncio.run(read_stream())
