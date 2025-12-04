from analytics import calculate_total_spending 
from analytics import calculate_spending_by_category
from analytics import calculate_monthly_spending
from analytics import sort_categories_by_amount 
from analytics import sort_months
from analytics import count_items
from analytics import calculate_average 
from analytics import find_highest_order
from analytics import find_lowest_order

def display_header():
    print("")
    print("="*60)
    print("       AMAZON ORDER ANALYSIS REPORT")
    print("="*60)

def display_total_spending(orders):
    total = calculate_total_spending(orders)
    print("")
    print("T0TAL SPENDING:$" + str(total))

def display_item_count(orders):
    count = count_items(orders)
    print("TOTAL ITEMS ORDERED: " + str(count))

def display_statistics(orders):
    average = calculate_average(orders)
    highest = find_highest_order(orders)
    lowest = find_lowest_order(orders)
    print("")
    print("AVERAGE ORDER VALUE: $" + str(average))
    print("HIGHEST ORDER VALUE: $" + str(highest))
    print("LOWEST ORDER VALUE: $" + str(lowest))

def display_category_spending(orders):
    total = calculate_total_spending(orders)
    category_spending = calculate_spending_by_category(orders)
    sorted_categories = sort_categories_by_amount(category_spending)
    print("")
    print("SPENDING BY CATEGORY:")
    print("-"*40)
    for category, amount in sorted_categories:
        percent = (amount/total)*100
        percent = round(percent, 2)
        print(f"  {category}: ${amount} ({percent}%)")

def display_top_categories(orders,limit):
    category_totals = calculate_spending_by_category(orders)
    sorted_categories = sort_categories_by_amount(category_totals)
    print("")
    print(f"TOP {limit} CATEGORIES BY SPENDING:")
    print("-"*40)
    count = 0 
    for item in sorted_categories:
        if count>=limit:
            break
        category = item[0]
        amount = item[1]
        count += 1
        print(f"{count}. {category}: ${amount}")

def display_monthly_spending(orders):
    total = calculate_total_spending(orders)
    monthly_totals = calculate_monthly_spending(orders)
    sorted_months = sort_months(monthly_totals)
    print("")
    print("MONTHLY SPENDING:")
    print("-"*40)
    for item in sorted_months:
        month= item[0]
        amount = item[1]
        bar_length = int((amount/total)*40)
        bar = "#" * bar_length
        print(f"{month}: ${amount} {bar}")
    
def display_footer(): 
    print("")
    print("="*60)
    print("         END OF AMAZON ORDER ANALYSIS REPORT")
    print("="*60)

def display_full_report(orders):
    if len(orders) == 0:
        print("")
        print("No orders to display.")
        return
    display_header()
    display_total_spending(orders)
    display_item_count(orders)
    display_statistics(orders)
    display_category_spending(orders)
    display_top_categories(orders, limit=5)
    display_monthly_spending(orders)
    display_footer()



