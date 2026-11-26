from moomoo import *
import pandas as pd

def get_individual_holdings(trade_context):
    ret, data = trade_context.position_list_query()
    if ret == RET_OK:
        return pd.DataFrame({
        "Symbol": data["code"],
        "Current Price": data["average_cost"].round(2),
        "Qty": data["qty"],
        "Market Value": data["market_val"],
        "Profit / Loss": data["pl_val"].round(2),
        "Profit% / Loss%": data["pl_ratio_avg_cost"]
        })
    
trade_context = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host="127.0.0.1",port=11111)
individual_holdings = get_individual_holdings(trade_context)

print(individual_holdings)
trade_context.close()
