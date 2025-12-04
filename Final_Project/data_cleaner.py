def clean_price(price_string):
    if price_string == "" or price_string == None:
        return 0.0
    cleaned = price_string.strip()
    cleaned = cleaned.replace('$','') 
    cleaned = cleaned.replace(',','')
    cleaned = cleaned.replace(' ','')
    price = float(cleaned)
    return price 

def parse_date(date_string):
    if date_string =="" or date_string == None:
        return None
    date_string = date_string.strip()
    if'/'in date_string:
        parts=date_string.split('/')
        if len(parts) == 3:
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
            if year < 100:
                year += 2000
            return {'year': year, 'month': month, 'day': day}
    if '-' in date_string:
        parts = date_string.split('-')
        if len(parts) == 3:
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            return {'year': year, 'month': month, 'day': day}
    return None

def get_month_key(date_dict):
    year = str(date_dict['year'])
    month = str(date_dict['month'])
    if len(month) == 1:
        month = '0' + month
    return year + '-' + month

def find_column_value(order, possible_names):
    for name in possible_names:
        if name in order:
            if order[name] != "" and order[name] != None:
                return order[name]
    return None

def clean_order_data(orders):
    cleaned_orders = []
    skipped = 0
    date_columns = ['Order Date', 'order date', 'Date', 'Purchase Date', 'order_date']
    price_columns = ['Item Total', 'Total', 'Price', 'Item Subtotal', 'item_total']
    category_columns = ['Category', 'category', 'Product Category', 'Department']
    title_columns = ['Title', 'Product Name', 'Item', 'item', 'Product Title']
    for order in orders:
        date_string = find_column_value(order, date_columns)
        date_value = None
        if date_string != None:
            date_value = parse_date(date_string)
        price_string = find_column_value(order, price_columns)
        price_value = 0.0
        if price_string != None:
            price_value = clean_price(price_string)
        category_value = find_column_value(order, category_columns)
        if category_value == None:
            category_value = "Uncategorized"
        title_value = find_column_value(order, title_columns)
        if title_value == None:
            title_value = "Unknown Item"
        if date_value != None and price_value > 0:
            cleaned_order = {
                'date': date_value,
                'month_key': get_month_key(date_value),
                'price': price_value,
                'category': category_value.strip(),
                'title': title_value.strip()
            }
            cleaned_orders.append(cleaned_order)
        else:
            skipped = skipped + 1
    
    if skipped > 0:
        print("Note: Skipped " + str(skipped) + " orders with missing data")
    
    print("Successfully processed " + str(len(cleaned_orders)) + " valid orders")
    return cleaned_orders

   

