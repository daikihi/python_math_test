def get_total_honey_import_amount(honey_imports):
    # honey_imports is a list of HoneyImportInfomation objects
    total_amount = 0
    for honey_import in honey_imports:
        for amount in honey_import.country_amount_map.values():
            total_amount += amount
    return total_amount

def get_honey_amount_by_country(honey_imports):
    # honey_imports is a list of HoneyImportInfomation objects
    honey_amounts_by_country = {}
    for honey_import in honey_imports:
        for country, amount in honey_import.country_amount_map.items():
            if country not in honey_amounts_by_country:
                honey_amounts_by_country[country] = 0
            honey_amounts_by_country[country] += amount
    return honey_amounts_by_country

def get_honey_imports_average_by_country(honey_imports):
    honey_imports_average_by_country = {} 
    for honey_import in honey_imports:
        for country, amount in honey_import.country_amount_map.items():
            if country not in honey_imports_average_by_country:
                honey_imports_average_by_country[country] = 0
            honey_imports_average_by_country[country] += amount

    for country, amount in honey_imports_average_by_country.items():
        honey_imports_average_by_country[country] = int(amount / len(honey_imports))
    return honey_imports_average_by_country
