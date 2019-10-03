from unittest import TestCase

from core.filenameextractors import extract_date_str, extract_name, trim_extension


class Test_FilenameExtractors(TestCase):
    def test_trim_extension(self):
        self.assertEqual('name', trim_extension('name.pdf'))
        self.assertEqual('', trim_extension(''))
        self.assertEqual('', trim_extension('.jpeg'))
        self.assertRaises(ValueError, trim_extension, filename='name.pdf.pdf')

    def test_name_extractor(self):
        self.assertEqual(('name', ''), extract_name('name'))
        self.assertEqual(('hello', 'y2019_m10_d3'), extract_name('hello_y2019_m10_d3'))

    def test_extract_date_str(self):
        self.assertEqual('y2019_m10_d3', extract_date_str('y2019_m10_d3_doc_fp'))
        self.assertEqual('y2015_m2', extract_date_str('y2015_m2'))
        self.assertEqual('y2017_m1_d1_h4_mte6_s2', extract_date_str('y2017_m1_d1_h4_mte6_s2_img'))
