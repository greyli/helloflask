import unittest
import os
import importlib.util

class Ch2TestCase(unittest.TestCase):
    def setUp(self):
        # Import ch2 app specifically
        ch2_path = os.path.join(os.path.dirname(__file__), '..', 'examples', 'ch2', 'app.py')
        spec = importlib.util.spec_from_file_location("ch2_app", ch2_path)
        ch2_app = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ch2_app)
        
        self.app = ch2_app.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_app_exist(self):
        self.assertIsNotNone(self.app)

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])

    def test_hello_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, Human!', data)
        self.assertIn('[Not Authenticated]', data)

    def test_hello_with_name_query(self):
        response = self.client.get('/?name=Flask')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, Flask!', data)

    def test_hello_route(self):
        response = self.client.get('/hello')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, Human!', data)

    def test_hi_redirect(self):
        response = self.client.get('/hi', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        data = response.get_data(as_text=True)
        self.assertIn('Hello, Human!', data)

    def test_time_machine(self):
        response = self.client.get('/back/2020')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to 4!', data)

    def test_three_colors(self):
        for color in ['blue', 'white', 'red']:
            response = self.client.get(f'/colors/{color}')
            self.assertEqual(response.status_code, 200)
            data = response.get_data(as_text=True)
            self.assertIn('Love is patient and kind', data)

    def test_teapot_coffee(self):
        response = self.client.get('/brew/coffee')
        self.assertEqual(response.status_code, 418)

    def test_teapot_tea(self):
        response = self.client.get('/brew/tea')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('A drop of tea', data)

    def test_404_error(self):
        response = self.client.get('/answer')
        self.assertEqual(response.status_code, 404)

    def test_note_text(self):
        response = self.client.get('/note')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'text/plain')
        data = response.get_data(as_text=True)
        self.assertIn('Note', data)
        self.assertIn('Morty', data)

    def test_note_html(self):
        response = self.client.get('/note/html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'text/html')
        data = response.get_data(as_text=True)
        self.assertIn('<h1>Note</h1>', data)

    def test_note_xml(self):
        response = self.client.get('/note/xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/xml')
        data = response.get_data(as_text=True)
        self.assertIn('<?xml version="1.0"', data)

    def test_note_json(self):
        response = self.client.get('/note/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        json_data = response.get_json()
        self.assertIn('note', json_data)
        self.assertEqual(json_data['note']['to'], 'Morty')

    def test_note_invalid_format(self):
        response = self.client.get('/note/invalid')
        self.assertEqual(response.status_code, 400)

    def test_set_cookie(self):
        response = self.client.get('/set/TestUser', follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertIn('name=TestUser', response.headers.get('Set-Cookie', ''))

    def test_login(self):
        with self.client.session_transaction() as sess:
            sess.clear()
        response = self.client.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        data = response.get_data(as_text=True)
        self.assertIn('[Authenticated]', data)

    def test_admin_access_denied(self):
        with self.client.session_transaction() as sess:
            sess.clear()
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 403)

    def test_admin_access_granted(self):
        with self.client.session_transaction() as sess:
            sess['logged_in'] = True
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 200)
        data = response.get_data(as_text=True)
        self.assertIn('Welcome to admin page', data)

    def test_logout(self):
        with self.client.session_transaction() as sess:
            sess['logged_in'] = True
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        data = response.get_data(as_text=True)
        self.assertIn('[Not Authenticated]', data)

    def test_foo_page(self):
        response = self.client.get('/foo')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Foo page', data)
        self.assertIn('Do something and redirect', data)

    def test_bar_page(self):
        response = self.client.get('/bar')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Bar page', data)
        self.assertIn('Do something and redirect', data)

    def test_do_something_redirect(self):
        response = self.client.get('/do-something?next=/foo', follow_redirects=False)
        self.assertEqual(response.status_code, 302)
