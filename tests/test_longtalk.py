import unittest
import os
import importlib.util

class LongtalkTestCase(unittest.TestCase):
    def setUp(self):
        # Import longtalk app specifically
        longtalk_dir = os.path.join(os.path.dirname(__file__), '..', 'examples', 'longtalk')
        longtalk_path = os.path.join(longtalk_dir, 'app.py')
        
        # Change to the longtalk directory temporarily
        original_cwd = os.getcwd()
        os.chdir(longtalk_dir)
        
        try:
            spec = importlib.util.spec_from_file_location("longtalk_app", longtalk_path)
            longtalk_app = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(longtalk_app)
            
            self.app = longtalk_app.app
            self.app.config['TESTING'] = True
            self.client = self.app.test_client()
        finally:
            os.chdir(original_cwd)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_app_exist(self):
        self.assertIsNotNone(self.app)

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
