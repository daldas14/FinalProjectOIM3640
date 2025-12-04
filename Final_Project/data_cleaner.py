def clean_price(price_string):
    if price_string == "" or price_string == None:
        return 0.0
    cleaned = price_string.strip()
    cleaned = cleaned.replace('$','') 
    cleaned = cleaned.replace(',','')
    cleaned = cleaned.replace( '','')
    price = float(cleaned)
    return price 
