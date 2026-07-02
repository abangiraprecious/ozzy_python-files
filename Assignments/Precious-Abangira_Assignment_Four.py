# Assignment Four

# A function is a block of code that performs a specific task and can be reused whenever needed. Instead of writing the same calculation many times, we write it once inside a function and call it whenever we want a given task to be done. In a market, this is like a vendor who has a fixed way of doing something, for example calculating cost, every single day, instead of doing it manually each time.

# My case study is Nakato who is a vendor who sells tomatoes at Owino market. We can use functions to calculate her cost, selling price, profit and turnover.

def calculate_cost(buying_price, transport):
    cost = buying_price + transport
    return cost

def calculate_selling_price(price_per_basin, basins_sold):
    selling_price = price_per_basin * basins_sold
    return selling_price

def calculate_profit(cost, selling_price):
    profit = selling_price - cost
    return profit

def calculate_turnover(price_per_basin, basins_sold):
    turnover = calculate_selling_price(price_per_basin, basins_sold)
    return turnover


# If Nakato  buys tomatoes worth 60000 shillings, pays 10000 shillings transport from Mukono on a boda, sells each small basin at 5000 shillings and sells 8 basins that day:

cost = calculate_cost(60000, 10000)
selling_price = calculate_selling_price(12000, 8)
profit = calculate_profit(cost, selling_price)
turnover = calculate_turnover(5000, 8)

print("Cost:", cost)
print("Selling price:", selling_price)
print("Profit:", profit)
print("Turnover:", turnover)