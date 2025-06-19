from xls_parser import parse_xls_main

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
