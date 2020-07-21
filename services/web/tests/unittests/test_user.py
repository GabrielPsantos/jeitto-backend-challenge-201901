from flask import url_for
from .flask_base_tests_cases import TestFlaskBase


class TestUserBP(TestFlaskBase):
    def test_register_users_ok(self):
        user = {
            'email': 'mail@mail.com',
            'username': 'test',
            'password': '1234'
        }

        esperado = {
            'id': '1',
            'username': 'test'
        }
        response = self.client.post(url_for('user.register'), json=user)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['username'], esperado['username'])

    def test_register_users_error_validation(self):
        user = {
            'username': 'test',
            'email': 'mailtest@mailtest.com',
        }

        esperado = {'password': ['Missing data for required field.']}

        response = self.client.post(url_for('user.register'), json=user)

        self.assertEqual(response.status_code, 422)

        self.assertEqual(response.json, esperado)

    def test_login_user_bad_credentials(self):
        user = {
            'email': 'mail@mail.com',
            'username': 'test',
            'password': '1234'
        }

        esperado = {
            'id': '1',
            'username': 'test'
        }
        response = self.client.post(url_for('user.register'), json=user)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['username'], esperado['username'])

        wrong_pass = {'password': 'senha123'}
        user.update(wrong_pass)

        response_login = self.client.post(url_for('user.login'), json=user)
        self.assertEqual(response_login.status_code, 401)





