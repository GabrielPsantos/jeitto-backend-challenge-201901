from flask import url_for
from .flask_base_tests_cases import TestFlaskBase


class TestLogin(TestFlaskBase):
    def test_generate_token(self):
        self.create_user()
        login = self.client.post(url_for('user.login'), json=self.user)
        esperado = ['acess_token', 'message']

        self.assertEqual(list(login.json.keys()), esperado)
