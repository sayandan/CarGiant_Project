import json


class TestData:
    CarsData = None
    cars = None
    BASE_URL = 'https://www.cargiant.co.uk/'
    USERNAME = 'satdb_ec@yahoo.com'
    PASSWORD = 'password'

    CHROME_EXECUTABLE_PATH = 'c://WebDrivers//chromedriver.exe'
    EDGE_EXECUTABLE_PATH = 'c://WebDrivers//msedgedriver.exe'

    PAGE_TITLE = "Cargiant - London's Largest Car Dealership"
    LOGIN_TITLE = 'My Garage - Cargiant'
    LOGIN_VERIFY_TEXT = 'Welcome'

    RESULTS_HEADER = 'Your Search Results'


# Open the existing json file for loading into a variable
class CarsData:

    def __init__(self):
        with open('cars.JSON', 'r') as f:
            self.cars = json.load(f)


