import unittest
import os
import importlib.util

class Ch3TestCase(unittest.TestCase):
    def setUp(self):
        # Import ch3 app specifically
        ch3_dir = os.path.join(os.path.dirname(__file__), '..', 'examples', 'ch3')
        ch3_path = os.path.join(ch3_dir, 'app.py')
        
        # Change to the ch3 directory temporarily for templates
        original_cwd = os.getcwd()
        os.chdir(ch3_dir)
        
        try:
            spec = importlib.util.spec_from_file_location("ch3_app", ch3_path)
            ch3_app = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(ch3_app)
            
            self.app = ch3_app.app
            self.app.config['TESTING'] = True
            self.client = self.app.test_client()
        finally:
            os.chdir(original_cwd)

    def test_app_exist(self):
        self.assertIsNotNone(self.app)

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])

    def test_watchlist_page(self):
        response = self.client.get('/watchlist')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Grey Li', data)
        self.assertIn('My Neighbor Totoro', data)
        self.assertIn('The Matrix', data)
        self.assertIn('CoCo', data)
