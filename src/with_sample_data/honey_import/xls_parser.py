from honey_import_information import HoneyImportInfomation
from file_system_loader import load_xls_binary_data_from_file

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


def parse_xls_main(xls_file_list):
    honey_import_info_list = []
    for xls_file_name in xls_file_list:
        # xls_file_name = "src/with_sample_data/honey_import/resoiurces/k001-2024-05-a016.xls"
        print(f"Processing file: {xls_file_name}")
        xls_file_root = load_xls_binary_data_from_file(xls_file_name)
        honey_import_info_list.append(parse_xls_file(xls_file_root))
        print(f"Finished processing file: {xls_file_name}")
    return honey_import_info_list



