from analytics import calculate_total_spending
from analytics import calculate_spending_by_category
from analytics import calculate_monthly_spending
from analytics import sort_categories_by_amount
from analytics import sort_months
from analytics import calculate_average

def export_report(orders,filename):
    if len(orders)==0:
        print("No data to export.")
        return
    total = calculate_total_spending(orders)
    average = calculate_average(orders)
    category_spending = calculate_spending_by_category(orders)
    sorted_categories = sort_categories_by_amount(category_spending)
    monthly_totals = calculate_monthly_spending(orders)
    sorted_months = sort_months(monthly_totals)

    file = open(filename,"w")

    file.write("AMAZON ORDER REPORT\n")
    file.write("=" *50 + "\n")
    file.write("\n")
    
    file.write("SPENDING BY CATEGORY\n")
    file.write("-" *50 + "\n")

    for item in sorted_categories:
        category = item[0]
        amount = item[1]
        file.write(f"{category}: ${amount:.2f}\n")
    file.write("\n")
    file.write("MONTHLY SPENDING\n")
    file.write("-" *50 + "\n")
    for item in sorted_months:
        month = item[0]
        amount = item[1]
        file.write(f"{month}: ${amount:.2f}\n")

    file.close()
    print(f"Report exported to {filename}")
    