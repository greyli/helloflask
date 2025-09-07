import unittest
import sys
import os
import importlib.util

class Ch4TestCase(unittest.TestCase):
    def setUp(self):
        # Import ch4 app specifically
        ch4_dir = os.path.join(os.path.dirname(__file__), '..', 'examples', 'ch4')
        ch4_path = os.path.join(ch4_dir, 'app.py')
        
        # Change to the ch4 directory temporarily for templates and forms
        original_cwd = os.getcwd()
        original_path = sys.path.copy()
        
        os.chdir(ch4_dir)
        sys.path.insert(0, ch4_dir)
        
        try:
            spec = importlib.util.spec_from_file_location("ch4_app", ch4_path)
            ch4_app = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(ch4_app)
            
            self.app = ch4_app.app
            self.app.config['TESTING'] = True
            self.app.config['WTF_CSRF_ENABLED'] = False
            self.client = self.app.test_client()
        finally:
            os.chdir(original_cwd)
            sys.path[:] = original_path

    def test_app_exist(self):
        self.assertIsNotNone(self.app)

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Home', data)

    def test_html_form_get(self):
        response = self.client.get('/html')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', data)

    def test_html_form_post(self):
        response = self.client.post('/html', data={'username': 'testuser'}, follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome home, testuser!', data)

    def test_basic_form_get(self):
        response = self.client.get('/basic')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', data)

    def test_basic_form_post_valid(self):
        response = self.client.post('/basic', data={
            'username': 'testuser',
            'password': 'password123'
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome home, testuser!', data)

    def test_basic_form_post_invalid(self):
        response = self.client.post('/basic', data={
            'username': 'testuser',
            'password': '123'  # Too short
        })
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Field must be between 8 and 128 characters long', data)
