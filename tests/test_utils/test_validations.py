from unittest import TestCase, mock
from src.utils.validations import InputValidations

class TestInputValidations(TestCase):
    
    @mock.patch('src.utils.validations.re.match')
    @mock.patch('builtins.input')
    def test_input_name(self,mock_object1,mock_object2): 
        mock_object1.side_effect= ['243','hg','Krishna ']
        mock_object2.side_effect= [False,False,True]
        self.assertEqual(InputValidations.input_name(),"krishna")
    
    #can mock like this also @mock.patch('re.match',mock.Mock(side_effect=[False,True]))
    @mock.patch('src.utils.validations.re.match')
    @mock.patch('builtins.input')
    def test_input_email(self,mock_object1,mock_object2): 
        mock_object1.side_effect= ['243','krishna@gmail.com']
        mock_object2.side_effect= [False,True]
        self.assertEqual(InputValidations.input_email(),'krishna@gmail.com')

    @mock.patch('src.utils.validations.re.match')
    @mock.patch('src.utils.validations.maskpass.askpass')
    def test_input_password(self,mock_object1,mock_object2): 
        mock_object1.side_effect= ['243','Krishna@1']
        mock_object2.side_effect= [False,True]
        self.assertEqual(InputValidations.input_password(),'Krishna@1')

    @mock.patch('src.utils.validations.re.match')
    @mock.patch('builtins.input')
    def test_input_user_id(self,mock_object1,mock_object2): 
        mock_object1.side_effect= ['','EMP8dje']
        mock_object2.side_effect= [False,True]
        self.assertEqual(InputValidations.input_user_id(),'EMP8dje')

    @mock.patch('src.utils.validations.re.match')
    @mock.patch('builtins.input')
    def test_input_asset_id(self,mock_object1,mock_object2): 
        mock_object1.side_effect= ['3+d','ASN8dje']
        mock_object2.side_effect= [False,True]
        self.assertEqual(InputValidations.input_asset_id(),'ASN8dje')

    @mock.patch('src.utils.validations.re.match')
    @mock.patch('builtins.input')
    def test_input_vendor_id(self,mock_object1,mock_object2): 
        mock_object1.side_effect= ['','VEN8dje']
        mock_object2.side_effect= [False,True]
        self.assertEqual(InputValidations.input_vendor_id(),'VEN8dje')

    @mock.patch('src.utils.validations.re.match')
    @mock.patch('builtins.input')
    def test_input_category_id(self,mock_object1,mock_object2): 
        mock_object1.side_effect= ['3e3','CAT8dje']
        mock_object2.side_effect= [False,True]
        self.assertEqual(InputValidations.input_category_id(),'CAT8dje')

    @mock.patch('src.utils.validations.re.match')
    @mock.patch('builtins.input')
    def test_input_mapping_id(self,mock_object1,mock_object2): 
        mock_object1.side_effect= ['5$3','MPN8dje']
        mock_object2.side_effect= [False,True]
        self.assertEqual(InputValidations.input_mapping_id(),'MPN8dje')

    @mock.patch('src.utils.validations.re.match')
    @mock.patch('builtins.input')
    def test_input_issue_id(self,mock_object1,mock_object2): 
        mock_object1.side_effect= ['','ISN8dje']
        mock_object2.side_effect= [False,True]
        self.assertEqual(InputValidations.input_issue_id(),'ISN8dje')

    @mock.patch('src.utils.validations.re.match')
    @mock.patch('builtins.input')
    def test_input_maintenance_id(self,mock_object1,mock_object2): 
        mock_object1.side_effect= ['','MTN8dje']
        mock_object2.side_effect= [False,True]
        self.assertEqual(InputValidations.input_maintenance_id(),'MTN8dje')

    @mock.patch('builtins.input')
    def test_input_date(self,mock_object1): 
        mock_object1.side_effect= ['2023-87-34','32-23-1','2023-11-12']
        self.assertEqual(InputValidations.input_date(),'2023-11-12')
