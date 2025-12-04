def calculate_total_spending(orders):
    total = 0.0
    for order in orders:
        total = total + order['price']
    total = round(total, 2)
    return total

def calculate_spending_by_category(orders):
    category_totals = {}
    for order in orders:
        category = order['category']
        price = order['price']
        if category in category_totals:
            category_totals[category] = category_totals[category] + price
        else:
            category_totals[category] = price
    for category in category_totals:
        category_totals[category] = round(category_totals[category], 2)
    return category_totals

def sort_categories_by_amount(category_totals):
    category_list = []
    for category in category_totals:
        amount = category_totals[category]
        category_list.append((category, amount))
    n = len(category_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if category_list[j][1] < category_list[j + 1][1]:
                temp = category_list[j]
                category_list[j] = category_list[j + 1]
                category_list[j + 1] = temp
    return category_list

def calculate_monthly_spending(orders):
    monthly_totals = {}
    for order in orders:
        month_key = order['month_key']
        price = order['price']
        if month_key in monthly_totals:
            monthly_totals[month_key] = monthly_totals[month_key] + price
        else:
            monthly_totals[month_key] = price
    for month in monthly_totals:
        monthly_totals[month] = round(monthly_totals[month], 2)
    return monthly_totals

def sort_months(monthly_totals):
    month_list = []
    for month in monthly_totals:
        amount = monthly_totals[month]
        month_list.append((month, amount))
    n = len(month_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if month_list[j][0] > month_list[j + 1][0]:
                temp = month_list[j]
                month_list[j] = month_list[j + 1]
                month_list[j + 1] = temp
    return month_list

def count_items(orders):
    return len(orders)

def calculate_average(orders):
    if len(orders) == 0:
        return 0.0
    total = calculate_total_spending(orders)
    average = total / len(orders)
    return round(average, 2)

def find_highest_order(orders):
    if len(orders) == 0:
        return 0.0
    highest = orders[0]['price']
    for order in orders:
        if order['price'] > highest:
            highest = order['price']
    return round(highest, 2)

def find_lowest_order(orders):
    if len(orders) == 0:
        return 0.0
    lowest = orders[0]['price']
    for order in orders:
        if order['price'] < lowest:
            lowest = order['price']
    return round(lowest, 2)