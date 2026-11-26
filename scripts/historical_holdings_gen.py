from moomoo import *
import pandas as pd
import sqlite3
from datetime import *

trade_context = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host="127.0.0.1",port=11111)
ret, data = trade_context.history_deal_list_query(start="2024-1-1",end=date.today())
if ret == RET_OK:
    pass
else:
    print('history_deal_list_query error: ', data)