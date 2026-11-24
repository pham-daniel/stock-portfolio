from moomoo import *
import pandas as pd

trade_context = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host="127.0.0.1",port=11111)
ret, data = trade_context.position_list_query()
if ret == RET_OK:
    print(data)
trade_context.close()
