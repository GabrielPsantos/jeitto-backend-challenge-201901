from flask import url_for
from .flask_base_tests_cases import TestFlaskBase


class TestInsert(TestFlaskBase):
    def test_company_product_ok(self):
        self.create_user()
        token = self.create_token()
        dado1 = {
            'company_id': 'vivo_11',
            'products': [
                {
                    'product_id': 'vivo_11',
                    'value': 10.00
                }
            ]
        }

        response = self.client.post(url_for('companyProducts.create'),
                                    json=dado1,
                                    headers=token)
        self.assertEqual(dado1, response.json)

    def test_company_product_without_fields(self):
        self.create_user()
        token = self.create_token()
        dado = {}

        expected = {
            'company_id': ['Missing data for required field.'],
            'products': ['Missing data for required field.']
        }

        response = self.client.post(
            url_for('companyProducts.create'), headers=token, json=dado)
        self.assertEqual(expected, response.json)
        self.assertEqual(response.status_code, 422)

    def test_company_product_duplicated_company_id(self):
        self.create_user()
        token = self.create_token()
        dado = {
            'company_id': 'claro_15',
            'products': [
                {
                          'product_id': 'claro_15',
                          'value': 10.00
                }
            ]
        }

        response = self.client.post(
            url_for('companyProducts.create'), headers=token, json=dado)
        self.assertEqual(dado, response.json)

        expected = {'error': 'Data related error'}

        response_2 = self.client.post(
            url_for('companyProducts.create'), headers=token, json=dado)
        self.assertEqual(expected, response_2.json)
        self.assertEqual(response_2.status_code, 422)


class TestShow(TestFlaskBase):
    def test_show_empty_query(self):
        self.create_user()
        token = self.create_token()
        response = self.client.get(
            url_for('companyProducts.listOneAll'),
            headers=token
        )
        self.assertEqual([], response.json)

    def test_show_element_inserted(self):
        self.create_user()
        token = self.create_token()
        dado1 = {
            'company_id': 'vivo_11',
            'products': [
                {
                    'product_id': 'vivo_11',
                          'value': 10.00
                }
            ]
        }
        response = self.client.post(url_for('companyProducts.create'), headers=token,
                                    json=dado1)
        response = self.client.get(
            url_for('companyProducts.listOneAll'), headers=token)
        self.assertEqual(1, len(response.json))

    def test_show_by_company_id(self):
        self.create_user()
        token = self.create_token()
        dado1 = {
            'company_id': 'vivo_11',
            'products': [
                {
                    'product_id': 'vivo_11',
                          'value': 10.00
                }
            ]
        }
        response = self.client.post(
            url_for('companyProducts.create'), json=dado1, headers=token)
        response = self.client.get(url_for('companyProducts.listOneAll',
                                           company_id=dado1['company_id']),
                                   headers=token)
        self.assertEqual(1, len(response.json))


class TestDelete(TestFlaskBase):
    def test_delete_non_existent(self):
        self.create_user()
        token = self.create_token()
        response = self.client.delete(url_for('companyProducts.delete',
                                              company_id='claro_11'), headers=token)
        self.assertEqual(response.status_code, 404)

    def test_delete_without_company_id(self):
        self.create_user()
        token = self.create_token()
        response = self.client.delete(
            url_for('companyProducts.delete'), headers=token)
        self.assertEqual(response.status_code, 401)

    def test_delete_success(self):
        self.create_user()
        token = self.create_token()
        dado1 = {
            'company_id': 'vivo_11',
            'products': [
                {
                    'product_id': 'vivo_11',
                          'value': 10.00
                }
            ]
        }
        self.client.post(url_for('companyProducts.create'),
                         json=dado1, headers=token)
        response = self.client.delete(
            url_for('companyProducts.delete',
                    company_id=dado1['company_id']),
            headers=token
        )
        self.assertEqual(response.status_code, 204)


class TestUpdate(TestFlaskBase):
    def test_update(self):
        self.create_user()
        token = self.create_token()
        estado_inicial = {
            'company_id': 'vivo_11',
            'products': [
                {
                    'product_id': 'vivo_11',
                          'value': 10.00
                }
            ]
        }

        estado_final = {
            'company_id': 'vivo_11',
            'products': [
                {
                    'product_id': 'vivo_13',
                    'value': 13.00
                }
            ]
        }

        self.client.post(url_for('companyProducts.create'),
                         headers=token,
                         json=estado_inicial)

        response = self.client.put(
            url_for('companyProducts.update'), json=estado_final, headers=token
        )
        self.assertEqual(estado_final, response.json)

    def test_update_error(self):
        self.create_user()
        token = self.create_token()
        estado_inicial = {
            'company_id': 'vivo_11',
            'products': [
                {
                    'product_id': 'vivo_11',
                          'value': 10.00
                }
            ]
        }

        estado_final = {
            'company_id': 'vivo_11',
            'products': [
                {
                    'value': 13.00
                }
            ]
        }

        expected = {'products':
                    {'0':
                        {'product_id':
                            ['Missing data for required field.']
                         }
                     }
                    }
        self.client.post(url_for('companyProducts.create'),
                         json=estado_inicial,
                         headers=token)

        response = self.client.put(
            url_for('companyProducts.update'),
            json=estado_final,
            headers=token
        )
        self.assertEqual(expected, response.json)
