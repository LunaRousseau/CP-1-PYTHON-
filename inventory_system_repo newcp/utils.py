def format_currency(value):
    return f"R$ {value:,.2f}"

def low_stock_alert(product):
    try:
        return int(product.get('qty',0)) <= int(product.get('threshold',0))
    except Exception:
        return False
