import unittest

# allow imports from parent directory
import sys
sys.path.append('../project_xl')
import util.line_extract as line_extract

class Test_Util_line(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """We only want to pull this data once for each TestCase since it is an expensive operation"""
        #self.df = get_stock_data('^DJI')
 
    def test_truncate_value(self):
        
        returned_value=line_extract.tidy_matched_value("some","something found")
        self.assertEqual("thing found",returned_value)

        returned_value=line_extract.tidy_matched_value("something","something :found")
        self.assertEqual("found",returned_value)
        
        print(returned_value)



unittest.main()

 