import unittest
from Employee import Employee


class testingEmployeeClass(unittest.TestCase):

    def setUp(self):
        self.employer = Employee("Justice", "Julius", 10000)

    def test_give_default_raise(self):
        self.employer.give_raise()
        self.assertEquals(15000, self.employer.annual_salary)

    def test_give_custom_raise(self):
        self.employer.give_raise(10000)
        self.assertEquals(20000, self.employer.annual_salary)


if __name__ == "__main__":
    unittest.main()
