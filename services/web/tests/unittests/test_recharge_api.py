from flask import url_for
from .flask_base_tests_cases import TestFlaskBase


class TestCadastro(TestFlaskBase):
    def test_company_product_ok(self):
        self.create_user()
        token = self.create_token()
        dado1 = {
            "company_id": "claro_11",
            "product_id": "claro_10",
            "phone_number": "5511999999999",
            "value": 10.00
        }

        response = self.client.post(
            url_for('phoneRecharges.create'),
            json=dado1,
            headers=token
        )
        response.json.pop('id')
        self.assertEqual(dado1, response.json)

    def test_company_product_without_fields(self):
        self.create_user()
        token = self.create_token()
        expected = {
            'company_id': ['Missing data for required field.'],
            'phone_number': ['Missing data for required field.'],
            'product_id': ['Missing data for required field.'],
            'value': ['Missing data for required field.']
        }

        response = self.client.post(
            url_for('phoneRecharges.create'),
            headers=token,
            json={}
        )

        self.assertEqual(expected, response.json)
        self.assertEqual(response.status_code, 422)


class TestMostrar(TestFlaskBase):
    def test_mostrar_deve_retornar_uma_query_vazia(self):
        self.create_user()
        token = self.create_token()
        response = self.client.get(
            url_for('phoneRecharges.listOneAll'),
            headers=token
        )
        self.assertEqual([], response.json)

    def test_mostrar_deve_retornar_um_query_com_elemento_iserido(self):
        self.create_user()
        token = self.create_token()
        dado1 = {
            "company_id": "claro_11",
            "product_id": "claro_10",
            "phone_number": "5511999999999",
            "value": 10.00
        }
        response = self.client.post(url_for('phoneRecharges.create'), headers=token,
                                    json=dado1)
        response = self.client.get(
            url_for('phoneRecharges.listOneAll'), headers=token)
        self.assertEqual(1, len(response.json))

    def test_mostrar_deve_retornar_um_query_com_elemento_inserido_busca_by_phone(self):
        self.create_user()
        token = self.create_token()
        dado1 = {
            "company_id": "claro_11",
            "product_id": "claro_10",
            "phone_number": "5511999999999",
            "value": 10.00
        }
        response = self.client.post(
            url_for('phoneRecharges.create'), json=dado1, headers=token)
        response = self.client.get(url_for('phoneRecharges.listOneAll',
                                           phone_number=dado1['phone_number']),
                                   headers=token)
        self.assertEqual(1, len(response.json))

    def test_mostrar_deve_retornar_um_query_com_elemento_inserido_busca_by_id(self):
        self.create_user()
        token = self.create_token()
        dado1 = {
            "company_id": "claro_11",
            "product_id": "claro_10",
            "phone_number": "5511999999999",
            "value": 10.00
        }
        response_create = self.client.post(
            url_for('phoneRecharges.create'),
            json=dado1,
            headers=token)
        id = response_create.json['id']

        response_list = self.client.get(url_for('phoneRecharges.listOneAll',
                                                id=id),
                                        headers=token)
        self.assertEqual(1, len(response_list.json))
