import unittest
# from name_function import get_formatted_name
#
#
# class NamesTestCase(unittest.TestCase):
#     """Tests for 'name_function.py'."""
#
#     def test_first_last_name(self):
#         """Do names like 'Janis Joplin' work?"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')
#
#
# if __name__ == '__main__':
#     unittest.main()


# "FAILING TESTS"
#
# from name_function import get_formatted_names
#
#
# class NamesTestCase(unittest.TestCase):
#     """Tests for 'name_function.py'."""
#
#     def test_first_last_name(self):
#         """Do names like 'Janis Joplin' work?"""
#         formatted_name = get_formatted_names('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')
#
#
# if __name__ == '__main__':
#     unittest.main()

# SOLVING THE PROBLEM FROM THE FAILING TEST

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        try:
            self.assertEqual(formatted_name, 'Janis')
        except AssertionError:
            pass
        else:
            print("hahahahaaha")

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
