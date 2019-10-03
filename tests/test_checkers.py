from unittest import TestCase

from core.checkers import does_folder_only_contain_files, is_folder_name_valid


class Test_Checkers(TestCase):
    def test_is_folder_name_valid(self):
        """On UNIX."""
        self.assertFalse(is_folder_name_valid(''))
        self.assertFalse(is_folder_name_valid('/home/Dropbox/fnc34'))
        self.assertTrue(is_folder_name_valid('fnc3'))
        self.assertTrue(is_folder_name_valid('/home/Dropbox/fnc3'))
