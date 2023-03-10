import unittest

from flask import url_for
from sqlalchemy import select, func

from app import app, db, Note, fake, init


class NotebookTestCase(unittest.TestCase):
    def setUp(self):
        app.config.update(
            TESTING=True,
            WTF_CSRF_ENABLED=False
        )

        self.context = app.test_request_context()  # 创建请求上下文对象
        self.context.push()  # 推送上下文
        self.client = app.test_client()
        self.runner = app.test_cli_runner()

        db.create_all()
        note1 = Note(title='test note 1')
        note2 = Note(title='test note 2')
        note3 = Note(title='test note 3')
        db.session.add_all([note1, note2, note3])
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        self.context.pop()

    def test_app_exist(self):
        self.assertFalse(app is None)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    # 测试主页
    def test_index_page(self):
        response = self.client.get(url_for('index'))
        data = response.get_data(as_text=True)
        notes_count = db.session.execute(
            select(func.count(Note.id))
        ).scalars().one()
        self.assertIn(f'{notes_count} Notes', data)

    # 测试创建新笔记
    def test_create_note(self):
        response = self.client.post(
            url_for('new_note'),
            data={'title': 'new note', 'body': 'hello world'},
            follow_redirects=True
        )
        data = response.get_data(as_text=True)
        self.assertIn('Note saved.', data)
        self.assertIn('hello world', data)

    # 测试更新笔记
    def test_update_note(self):
        # test pre-fill form values
        response = self.client.get(
            url_for('edit_note', note_id=1)
        )
        data = response.get_data(as_text=True)
        self.assertIn('value="test note 1"', data)

        response = self.client.post(
            url_for('edit_note', note_id=1),
            data={'title': 'updated title', 'body': 'updated body'},
            follow_redirects=True
        )
        data = response.get_data(as_text=True)
        self.assertIn('Note updated.', data)
        self.assertIn('updated title', data)
        self.assertIn('updated body', data)
        self.assertIn('Updated at:', data)
        self.assertNotIn('test note 1', data)

    # 测试删除笔记
    def test_delete_note(self):
        response = self.client.post(
            url_for('delete_note', note_id=1),
            follow_redirects=True,
        )
        data = response.get_data(as_text=True)
        self.assertIn('Note deleted.', data)
        self.assertNotIn('test note 1', data)

    # 测试表单验证
    def test_form_validation(self):
        response = self.client.post(
            url_for('new_note'),
            data={'title': ' ', 'body': 'Hello, world.'},  # 填入空格作为标题
            follow_redirects=True
        )
        data = response.get_data(as_text=True)
        self.assertIn('This field is required.', data)

    def test_fake_command(self):
        result = self.runner.invoke(fake)
        self.assertIn('Created 20 notes.', result.output)
        note_count = db.session.execute(
            select(func.count(Note.id))
        ).scalars().one()
        self.assertEqual(note_count, 20)

    def test_fake_command_with_count(self):
        result = self.runner.invoke(fake, ['--count', '50'])
        self.assertIn('Created 50 notes.', result.output)
        note_count = db.session.execute(
            select(func.count(Note.id))
        ).scalars().one()
        self.assertEqual(note_count, 50)

    def test_init_command(self):
        result = self.runner.invoke(init)
        self.assertIn('Initialized.', result.output)

    def test_init_command_with_drop(self):
        result = self.runner.invoke(init, ['--drop-table'], input='y\n')
        self.assertIn('This operation will delete the tables, do you want to continue?', result.output)
        self.assertIn('Dropped tables.', result.output)


if __name__ == '__main__':
    unittest.main()
