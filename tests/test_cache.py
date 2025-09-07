import unittest
import os
import importlib.util

class CacheTestCase(unittest.TestCase):
    def setUp(self):
        # Import cache app specifically
        cache_dir = os.path.join(os.path.dirname(__file__), '..', 'examples', 'cache')
        cache_path = os.path.join(cache_dir, 'app.py')
        
        # Change to the cache directory temporarily
        original_cwd = os.getcwd()
        os.chdir(cache_dir)
        
        try:
            spec = importlib.util.spec_from_file_location("cache_app", cache_path)
            cache_app = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(cache_app)
            
            self.app = cache_app.app
            self.app.config['TESTING'] = True
            self.client = self.app.test_client()
        finally:
            os.chdir(original_cwd)

    def test_app_exist(self):
        self.assertIsNotNone(self.app)

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
