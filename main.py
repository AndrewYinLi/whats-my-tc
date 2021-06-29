from yahoo_fin import stock_info as si

share_price = si.get_live_price("cflt")
num_shares = 1.0

print(str(share_price * num_shares))
