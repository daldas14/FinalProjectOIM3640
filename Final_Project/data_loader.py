import csv

def load_csv_file(filename):
    orders = []
    file = open(filename, 'r', encoding='utf-8')
    reader = csv.DictReader(file)
    for row in reader:
        orders.append(row)
    file.close()  # MOVED OUTSIDE THE LOOP(bug because it was inside)
    print("Successfully Loaded " + str(len(orders)) + " orders from " + filename)  # MOVED OUTSIDE + added space
    return orders

def pick_file():
    import tkinter as tk
    from tkinter import filedialog
    # Creates a hidden root window
    root = tk.Tk()
    root.withdraw()
    # Makes dialogue appear on the top of all windows
    root.attributes('-topmost', True)
    file_path = filedialog.askopenfilename(
        title="Select your Amazon CSV file",
        filetypes=[("CSV files", "*.csv")],
    )
    # Destroys the root window opened
    root.destroy()
    if file_path == "":
        return None
    return file_path
        
    