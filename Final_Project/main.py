import os
SCRIPT_FOLDER= os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_FOLDER)
from data_loader import load_csv_file
from data_loader import pick_file
from data_cleaner import clean_order_data
from display import display_full_report
from display import display_category_spending 
from display import display_monthly_spending
from export import export_report 
from html_report import generate_html_report

def show_welcome():
    print("")
    print("=" * 50)
    print("   AMAZON SPENDING TRACKER")
    print("=" * 50)
    print("")
    print("This tool analyzes your Amazon order history.")
    print("")
    print("To get your Amazon data:")
    print("1. Go to Amazon.com")
    print("2. Go to Account > Download order reports")
    print("3. Download the CSV file")

def show_menu():
    print("")
    print("-" * 40)
    print("MENU")
    print("-" * 40)
    print("1. Browse for CSV file")
    print("2. Type CSV filename")
    print("3. View full report")
    print("4. View categories only")
    print("5. View monthly spending only")
    print("6. Export report to text file")
    print("7. Export report to HTML")
    print("8. Exit")
    print("-" * 40)

def main():
    show_welcome()
    orders = []
    running = True
    
    while running:
        show_menu()
        choice = input("Enter choice (1-8): ")
        choice = choice.strip()
        
        if choice == "1":
            print("")
            print("Opening file picker...")
            filename = pick_file()
            if filename == None:
                print("No file selected.")
            else:
                print("Selected: " + filename)
                raw_orders = load_csv_file(filename)
                if len(raw_orders) > 0:
                    orders = clean_order_data(raw_orders)
                    print("")
                    print("Data loaded! Choose option 3 to see results.")
        
        elif choice == "2":
            print("")
            filename = input("Enter CSV filename: ")
            filename = filename.strip()
            if filename == "":
                filename = "sample_amazon_orders.csv"
                print("Using default: " + filename)
            raw_orders = load_csv_file(filename)
            if len(raw_orders) > 0:
                orders = clean_order_data(raw_orders)
                print("")
                print("Data loaded! Choose option 3 to see results.")
        
        elif choice == "3":
            if len(orders) > 0:
                display_full_report(orders)
            else:
                print("")
                print("No data loaded. Load a CSV file first.")
        
        elif choice == "4":
            if len(orders) > 0:
                display_category_spending(orders)
            else:
                print("")
                print("No data loaded. Load a CSV file first.")
        
        elif choice == "5":
            if len(orders) > 0:
                display_monthly_spending(orders)
            else:
                print("")
                print("No data loaded. Load a CSV file first.")
        
        elif choice == "6":
            if len(orders) > 0:
                print("")
                filename = input("Enter output filename: ")
                filename = filename.strip()
                if filename == "":
                    filename = "spending_report.txt"
                export_report(orders, filename)
            else:
                print("")
                print("No data loaded. Load a CSV file first.")
        
        elif choice == "7":
            if len(orders) > 0:
                print("")
                filename = input("Enter output filename: ")
                filename = filename.strip()
                if filename == "":
                    filename = "spending_report.html"
                generate_html_report(orders, filename)
                print("Open " + filename + " in a browser to view!")
            else:
                print("")
                print("No data loaded. Load a CSV file first.")
        
        elif choice == "8":
            print("")
            print("Goodbye!")
            print("")
            running = False
        
        else:
            print("")
            print("Invalid choice. Enter 1-8.")

main()