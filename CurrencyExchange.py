def exchange_money(budget, exchange_rate):
    return budget/exchange_rate


def get_change(budget, exchanging_value):
    return budget - exchanging_value


def get_value_bills(denomination, number_of_bills):
    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    return int(budget/denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    exchangeWithValue = (exchange_rate * spread/100) + exchange_rate
    budgetAfterExchange = (budget/exchangeWithValue//denomination)
    return int(budgetAfterExchange * denomination)


print(exchangeable_value(1500, 0.84, 25, 40))


def unexchangeable_value(budget, exchange_rate, spread, denomination):
    exchangeWithValue = (exchange_rate * spread/100) + exchange_rate
    budgetAfterExchange = budget/exchangeWithValue
    return int(budgetAfterExchange % denomination)
