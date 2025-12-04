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

