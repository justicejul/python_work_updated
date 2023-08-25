# Modify your function, so it requires a third parameter, population.
# It should now return a single string of the form City, Country – population xxx,
# such as Santiago, Chile – population 5000000.

# Run test_cities.py again.
# Make sure test_city_country() fails this time.

# Modify the function so the population parameter is optional.
# Run test_cities.py again, and make sure test_city_country() passes again.

# Write a second test called test_city_country_population() that verifies
# you can call your function with the values 'santiago', 'chile', and 'population=5000000'.
# Run test_cities.py again, and make sure this new test passes.
import unittest

from main import city_country_name as ccn

# name = ccn("Narayi", "Kaduna")
# print(name)


class CountryCityTestCase(unittest.TestCase):

    def test_city_country(self):
        """Trying to test my Country,City function"""
        name = ccn("Nigeria", "Kaduna")
        self.assertEquals(name, "Nigeria, Kaduna")

    def test_city_country_population(self):
        """Trying to test my Country,City and population function"""
        eve = ccn("Ghana", "Accra", "2,500,000")
        self.assertEquals(eve, "Ghana, Accra - population 2,500,000")

    if __name__ == "__main__":
        unittest.main()
