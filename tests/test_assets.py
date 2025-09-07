import unittest
import os
import importlib.util

class AssetsTestCase(unittest.TestCase):
    def setUp(self):
        # Import assets app specifically
        assets_dir = os.path.join(os.path.dirname(__file__), '..', 'examples', 'assets')
        assets_path = os.path.join(assets_dir, 'app.py')
        
        # Change to the assets directory temporarily
        original_cwd = os.getcwd()
        os.chdir(assets_dir)
        
        try:
            spec = importlib.util.spec_from_file_location("assets_app", assets_path)
            assets_app = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(assets_app)
            
            self.app = assets_app.app
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
