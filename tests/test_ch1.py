import unittest
import os
import importlib.util

class Ch1TestCase(unittest.TestCase):
    def setUp(self):
        # Import ch1 app specifically
        ch1_path = os.path.join(os.path.dirname(__file__), '..', 'examples', 'ch1', 'app.py')
        spec = importlib.util.spec_from_file_location("ch1_app", ch1_path)
        ch1_app = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ch1_app)
        
        self.app = ch1_app.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.cli_runner = self.app.test_cli_runner()

    def test_app_exist(self):
        self.assertIsNotNone(self.app)

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, world!', data)

    def test_ping_page(self):
        response = self.client.get('/ping')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, Flask!', data)

    def test_pong_page(self):
        response = self.client.get('/pong')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, Flask!', data)

    def test_greet_default(self):
        response = self.client.get('/greet')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, Programmer!', data)

    def test_greet_with_name(self):
        response = self.client.get('/greet/Flask')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, Flask!', data)

    def test_hello_cli_command(self):
        result = self.cli_runner.invoke(args=['hello'])
        self.assertIn('Hello, Human!', result.output)
