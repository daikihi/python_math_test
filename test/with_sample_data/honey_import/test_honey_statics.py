import unittest
from src.with_sample_data.honey_import.honey_statics import get_honey_imports_average_by_country
from src.with_sample_data.honey_import.honey_import_information import HoneyImportInfomation


class TestHoneyStatics(unittest.TestCase):
    """  """ # todo write here
    def test_get_honey_imports_average_by_country(self):
        """ Test the average honey imports by country """
        info1 = HoneyImportInfomation("2023", "01", ["Japan", "USA"])
        info1.country_amount_map = {"Japan": 100, "USA": 200}
        info1.country_price_map = {"Japan": 1000, "USA": 2000}

        info2 = HoneyImportInfomation("2023", "02", ["Japan", "USA"])
        info2.country_amount_map = {"Japan": 150, "USA": 250}
        info2.country_price_map = {"Japan": 1500, "USA": 2500}
        
        info3 = HoneyImportInfomation("2023", "03", ["Japan", "USA"])
        info3.country_amount_map = {"Japan": 200, "USA": 300}
        info3.country_price_map = {"Japan": 2000, "USA": 3000}

        honey_imports = [
            info1, info2, info3
        ]

        result = get_honey_imports_average_by_country(honey_imports)

        expected_result = {
            "Japan": 150.0,
            "USA": 250.0
        }
        self.assertEqual(result, expected_result)

        """ HoneyInmportInformation has for three month but there are different countries in each month """
        info3 = HoneyImportInfomation("2023", "01", ["Japan", "USA"])
        info3.country_amount_map = {"Japan": 100, "USA": 200}
        info3.country_price_map = {"Japan": 1000, "USA": 2000}

        info4 = HoneyImportInfomation("2023", "01", ["Swiss", "Sweden"])
        info4.country_amount_map = {"Swiss": 150, "Sweden": 250}
        info4.country_price_map = {"Swiss": 1500, "Sweden": 2500}

        info5 = HoneyImportInfomation("2023", "01", ["Candana", "Australia"])
        info5.country_amount_map = {"Candana": 200, "Australia": 300}
        info5.country_price_map = {"Candana": 2000, "Australia": 3000}
        honey_imports = [
            info3, info4, info5
        ]

        result = get_honey_imports_average_by_country(honey_imports)

        expected_result = {
            "Japan": 33,
            "USA": 66,
            "Swiss": 50,
            "Sweden": 83,
            "Candana": 66,
            "Australia": 100
        }
        self.assertEqual(result, expected_result)