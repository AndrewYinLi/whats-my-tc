import bios
from yahoo_fin import stock_info as si

share_price = si.get_live_price("cflt")

numbers = bios.read("/Users/anli/git/go/src/github.com/confluentinc/whats-my-tc/numbers.yaml")

num_shares = float(numbers["num_shares"])
num_sold = float(numbers["num_sold"])
strike_price = float(numbers["strike_price"])
base_salary = float(numbers["base_salary"])

remaining_grant_value = (share_price-strike_price) * (num_shares-num_sold)
annual_grant_value = remaining_grant_value / 4

print("Current share price: " + str(share_price))
print("Remaining grant value: " + str(remaining_grant_value))
print("Annual grant value: " + str(annual_grant_value))
print("Annual TC: " + str(base_salary + annual_grant_value))
