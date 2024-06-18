import unittest
import os
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'

from sqlalchemy import select, func

from app import app, db, Note, lorem_command, init_command


class NotebookTestCase(unittest.TestCase):
    def setUp(self):
        app.config.update(
            TESTING=True,
            WTF_CSRF_ENABLED=False
        )

        self.context = app.app_context()  # create app context
        self.context.push()  # push context
        self.client = app.test_client()
        self.cli_runner = app.test_cli_runner()

        db.create_all()
        note1 = Note(title='test note 1', body='test body 1')
        note2 = Note(title='test note 2', body='test body 2')
        note3 = Note(title='test note 3', body='test body 3')
        db.session.add_all([note1, note2, note3])
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        self.context.pop()

    def test_app_exist(self):
        self.assertFalse(app is None)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        notes_count = db.session.scalar(select(func.count(Note.id)))
        self.assertIn(f'{notes_count} Notes', data)

    def test_create_note(self):
        response = self.client.post(
            '/new',
            data={'title': 'new note', 'body': 'hello world'},
            follow_redirects=True
        )
        data = response.get_data(as_text=True)
        self.assertIn('Note saved.', data)
        self.assertIn('hello world', data)

    def test_update_note(self):
        # test pre-fill form values
        response = self.client.get('/edit/1')
        data = response.get_data(as_text=True)
        self.assertIn('value="test note 1"', data)

        response = self.client.post(
            '/edit/1',
            data={'title': 'updated title', 'body': 'updated body'},
            follow_redirects=True
        )
        data = response.get_data(as_text=True)
        self.assertIn('Note updated.', data)
        self.assertIn('updated title', data)
        self.assertIn('updated body', data)
        self.assertIn('Updated at:', data)
        self.assertNotIn('test note 1', data)

    def test_delete_note(self):
        response = self.client.post(
            '/delete/1',
            follow_redirects=True,
        )
        data = response.get_data(as_text=True)
        self.assertIn('Note deleted.', data)
        self.assertNotIn('test note 1', data)

    def test_form_validation(self):
        response = self.client.post(
            '/new',
            data={'title': ' ', 'body': 'Hello, world.'},  # use whitespace for invalid title
            follow_redirects=True
        )
        data = response.get_data(as_text=True)
        self.assertIn('This field is required.', data)

    def test_lorem_command(self):
        result = self.cli_runner.invoke(lorem_command)
        self.assertIn('Created 20 notes.', result.output)
        note_count = db.session.scalar(select(func.count(Note.id)))
        self.assertEqual(note_count, 20)

    def test_lorem_command_with_count(self):
        result = self.cli_runner.invoke(lorem_command, ['--count', '50'])
        self.assertIn('Created 50 notes.', result.output)
        note_count = db.session.scalar(select(func.count(Note.id)))
        self.assertEqual(note_count, 50)

    def test_init_command(self):
        result = self.cli_runner.invoke(init_command)
        self.assertIn('Initialized.', result.output)

    def test_init_command_with_drop(self):
        result = self.cli_runner.invoke(init_command, ['--drop-table'], input='y\n')
        self.assertIn('This operation will delete the tables, do you want to continue?', result.output)
        self.assertIn('Dropped tables.', result.output)


if __name__ == '__main__':
    unittest.main()
