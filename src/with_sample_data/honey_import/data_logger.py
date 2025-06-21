def print_honey_import_info(_honey_import_info):
    print(f"Year: {_honey_import_info.year}, Month: {_honey_import_info.month}")
    for country, _ in _honey_import_info.country_amount_map.items():
        amount = _honey_import_info.country_amount_map[country]
        price = _honey_import_info.country_price_map[country]
        print(f"Country: {country}, Amount: {amount}, Price: {price}")

def print_honey_import_info_list(honey_import_info_list):
    for honey_import_info in honey_import_info_list:
        print_honey_import_info(honey_import_info)
        print("-" * 20)  # Separator for readability
    print(f"Total records: {len(honey_import_info_list)}")