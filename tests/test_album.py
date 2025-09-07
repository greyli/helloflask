import unittest
import os
import importlib.util
from pathlib import Path

class AlbumTestCase(unittest.TestCase):
    def setUp(self):
        # Import album app specifically
        album_dir = os.path.join(os.path.dirname(__file__), '..', 'examples', 'album')
        album_path = os.path.join(album_dir, 'app.py')
        
        # Change to the album directory temporarily for templates
        original_cwd = os.getcwd()
        os.chdir(album_dir)
        
        try:
            spec = importlib.util.spec_from_file_location("album_app", album_path)
            album_app = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(album_app)
            
            self.app = album_app.app
            self.app.config['TESTING'] = True
            self.app.config['WTF_CSRF_ENABLED'] = False
            # Use temp directory for testing uploads
            self.app.config['UPLOAD_PATH'] = Path(self.app.root_path) / 'test_uploads'
            self.client = self.app.test_client()
            
            # Create test upload directory
            os.makedirs(self.app.config['UPLOAD_PATH'], exist_ok=True)
        finally:
            os.chdir(original_cwd)

    def tearDown(self):
        # Clean up test upload directory
        import shutil
        if os.path.exists(self.app.config['UPLOAD_PATH']):
            shutil.rmtree(self.app.config['UPLOAD_PATH'])

    def test_app_exist(self):
        self.assertIsNotNone(self.app)

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('HelloFlask', data)

    def test_upload_page_get(self):
        response = self.client.get('/upload')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Upload Photo', data)

    def test_upload_no_file(self):
        response = self.client.post('/upload', data={})
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('This field is required', data)
