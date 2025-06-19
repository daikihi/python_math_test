from file_system_loader import load_xls_binary_data_from_file
from honey_import_information import HoneyImportInfomation

def parse_first_row(line):
    year = line[0]
    month = line[1]
    countries = line[7:]
    return HoneyImportInfomation(year, month, countries)

def parse_fifth_row(line, honey_import_infp):
    i = 0
    for countryCount in line[7:]:
        ele = list(honey_import_infp.country_amount_map.items())[i]
        count = int(ele.__getitem__(1))
        country = ele.__getitem__(0)
        if count > 0:  # an element should be appeared only once
            panic(f"Error: {ele.__getitem__(0)} should be 0, but it is {ele.__getitem__(1)}")
        honey_import_infp.country_amount_map.update({country: int(countryCount)})
        i += 1

def parse_sixth_row(line, honey_import_infp):
    i = 0
    for countryCount in line[7:]:
        ele = list(honey_import_infp.country_price_map.items())[i]
        count = int(ele.__getitem__(1))
        country = ele.__getitem__(0)
        if count > 0:  # an element should be appeared only once
            panic(f"Error: {ele.__getitem__(0)} should be 0, but it is {ele.__getitem__(1)}")
        honey_import_infp.country_price_map.update({country: int(countryCount)})
        i += 1

def parse_xls_file(xls_file_root):
    i = 0
    for key in xls_file_root:
        if i == 0:
            honey_import_infp = parse_first_row(xls_file_root[key])
        elif i == 4: # 第二数量
            parse_fifth_row(xls_file_root[key], honey_import_infp)
        elif i == 5: # 第二価格
            parse_sixth_row(xls_file_root[key], honey_import_infp)
        i += 1
    return honey_import_infp


def print_honey_import_info(_honey_import_infp):
    print(f"Year: {_honey_import_infp.year}, Month: {_honey_import_infp.month}")
    for country, count in _honey_import_infp.country_amount_map.items():
        print(f"{country}: {count}")
    for country, price in _honey_import_infp.country_price_map.items():
        print(f"{country}: {price} JPY")

def parse_xls_main(xls_file_list):
    for xls_file_name in xls_file_list:
        # xls_file_name = "src/with_sample_data/honey_import/resoiurces/k001-2024-05-a016.xls"
        print(f"Processing file: {xls_file_name}")
        xls_file_root = load_xls_binary_data_from_file(xls_file_name)
        honey_import_indo = parse_xls_file(xls_file_root)
        print_honey_import_info(honey_import_indo)
        print(f"Finished processing file: {xls_file_name}")



# if getting files list contains trash files, then filter them
def filter_xls_only(file_list):
    xls_file = []
    for file in file_list:
        if file.endswith(".xls"):
            xls_file.append(file)
    return xls_file



# we assume that we execute this script from the root of the project
def main():
    print("statrting honey import...")
    from file_system_loader import get_file_list
    file_list = get_file_list("src/with_sample_data/honey_import/resoiurces")
    xls_file_list = filter_xls_only(file_list)
    non_xls_file_list = list(set(file_list) - set(xls_file_list))
    print(f"non_xls_file_list =  {non_xls_file_list}")
    result = parse_xls_main(xls_file_list)
    print("end honey import...")


if __name__ == "__main__":
    main()
