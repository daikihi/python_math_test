def print_honey_import_info(_honey_import_infp):
    print(f"Year: {_honey_import_infp.year}, Month: {_honey_import_infp.month}")
    for country, count in _honey_import_infp.country_amount_map.items():
        print(f"{country}: {count}")
    for country, price in _honey_import_infp.country_price_map.items():
        print(f"{country}: {price} JPY")