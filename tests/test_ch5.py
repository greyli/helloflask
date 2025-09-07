import unittest
import os
import importlib.util

class Ch5TestCase(unittest.TestCase):
    def setUp(self):
        # Import ch5 app specifically
        ch5_path = os.path.join(os.path.dirname(__file__), '..', 'examples', 'ch5', 'app.py')
        spec = importlib.util.spec_from_file_location("ch5_app", ch5_path)
        ch5_app = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ch5_app)
        
        self.app = ch5_app.app
        self.db = ch5_app.db
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        self.cli_runner = self.app.test_cli_runner()
        
        with self.app.app_context():
            self.db.create_all()

    def tearDown(self):
        with self.app.app_context():
            self.db.drop_all()

    def test_app_exist(self):
        self.assertIsNotNone(self.app)

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])

    def test_cli_init_command(self):
        result = self.cli_runner.invoke(args=['init'])
        self.assertIn('Initialized.', result.output)

    def test_database_models(self):
        # Import ch5 app specifically for models
        ch5_path = os.path.join(os.path.dirname(__file__), '..', 'examples', 'ch5', 'app.py')
        spec = importlib.util.spec_from_file_location("ch5_models", ch5_path)
        ch5_models = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ch5_models)
        
        # Test model creation doesn't raise errors
        self.assertIsNotNone(ch5_models.Note)
        self.assertIsNotNone(ch5_models.Author)
        self.assertIsNotNone(ch5_models.Article)
        self.assertIsNotNone(ch5_models.Country)
        self.assertIsNotNone(ch5_models.Capital)
