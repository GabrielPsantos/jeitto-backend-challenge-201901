# Desafio Backend do Jeitto

Este desafio tem como intuito testar as habilidades de desenvolvimento e arquitetura de software do candidato à uma vaga no time de engenharia do Jeitto.
Não foque apenas em entregar este projeto, ele será sim avaliado porém foque mais em aprender durante o processo e tirar o máximo de proveito possível desta experiência.
Antes de começar a codificar, leia todo o texto. Entenda bem o problema, o que foi proposto e em caso de dúvida / sugestão entre em contato.
No final do texto existe uma sessão com leituras recomendadas. São textos variados que possuem o intuito auxiliar no processo de decisão e aprendizagem para chegar sucesso ao final deste desafio.

Divirta-se! :)


## Problema: Recarga de telefônica
Implementar uma API para permitir a compra de créditos telefônicos onde o usuário, após informar o número à ser recarregado a compra será efetuada.


### Pesquisa por produtos
O primeiro recurso que deve ser implementado é o que irá permitir a manutenção (CRUD) e busca por produtos compatíveis para serem utilizado na recarga. O mesmo deverá, em seu método GET, também receber um parâmetro "company_id" e retornar um json com os produtos daquela companhia informada. Como no exemplo abaixo:

Exemplo 1.1: GET /CompanyProducts?company_id=claro_11

```json
{
"company_id": "claro_11",
 "products":[
   {"id": "claro_10", "value": 10.0},
   {"id": "claro_20", "value": 20.0}
 ]
}
```

Exemplo 1.2: GET /CompanyProducts
```json
[
   {
       "company_id": "claro_11",
       "products":[
           {"id": "claro_10", "value": 10.0},
           {"id": "claro_20", "value": 20.0}
       ]
   },
   {
       "company_id": "tim_11",
       "products":[
           {"id": "tim_10", "value": 10.0},
           {"id": "tim_20", "value": 20.0}
       ]
   }
]
```

Obs.: Os demais metodos, deverão seguir a mesma estrutura do payload indicado no exemplo 1.1.


### Efetivação da recarga
O segundo recurso deverá efetivar a recarga telefônica propriamente dita. Permitirá um POST com os dados necessários para a recarga, bem como GETs para busca de dados como nos exemplos abaixo:

Exemplo 2.1: POST /PhoneRecharges
```json
{
   "company_id": "claro_11",
   "product_id": "claro_10",
   "phone_number": "5511999999999",
   "value": 10.00
}
```

Exemplo 2.2: GET /PhoneRecharges?id=id_da_recarga
```json
{
   "id": "id_da_recarga",
   "created_at": "2019-02-01T13:00:00.000Z",
   "company_id": "claro_11",
   "product_id": "claro_10",
   "phone_number": "5511999999999",
   "value": 10.00
}
```

Exemplo 2.3: GET /PhoneRecharges?phone_number=5511999999999
```json
[
   {
       "id": "id_da_recarga",
       "created_at": "2019-02-01T13:00:00.000Z",
       "company_id": "claro_11",
       "product_id": "claro_10",
       "phone_number": "5511999999999",
       "value": 10.00
   },
   {
       "id": "id_da_recarga",
       "created_at": "2019-03-14T13:00:00.000Z",
       "company_id": "claro_11",
       "product_id": "claro_10",
       "phone_number": "5511999999999",
       "value": 10.00
   }
]
```

Obs.: Os demais métodos não deverão ser permitidos para este recurso.


## Como enviar sua sua solução
Para participar você deverá fazer um fork deste repositório e submeter as alterações apenas para a sua cópia. Não faça um PR para este repositório, apenas envie um link para o avaliador que está em contato com você.

O que **queremos** ver:
- Python 3.
- Testes bem escritos e com uma boa cobertura.
- Legibilidade e manutenibilidade de código.
- Código em inglês.
- Segurança de dados e acesso.
- Tratamento de erros.
- Organização e insruções de como executar o projeto.

O que **gostariamos** de ver:
- Documentação fácil e bem escrita.
- Utilização de docker.
- Processamento assíncrono.
- AIOHTTP, Flask.
- Cache de dados.
- Deploy automatizado.
- Amigavel com Google Cloud.
- Segurança de dados.

## Trilha sonora utilizada 
- [Plantasia - Mort Garson](https://open.spotify.com/track/4CyTrR4c13d57jCVstfS8T?si=CmsPh3KzShiD3SaxNdH8gw)

## Instruções

#### Construa o ambiente

    docker-compose up --b --d

#### Rode as migrations

  docker-compose exec web flask db init
  docker-compose exec web flask db migrate
  docker-compose exec web flask db upgrade

#### Execute os testes

docker-compose exec web coverage run --source=project -m unittest discover -s tests/

#### Gere o HTML de Cobertura

docker-compose exec web coverage html

#### REST API

Se tudo deu certo, a um health-check estara disponivel no endereço http://localhost:5000/health-check

#### Com tudo rodando

exportar o arquivo Phone_recharger.postman_collection.json para o seu postman, se cadastrar, logar e usar os endpoints

# Perguntas que devem ser respondidas

- Quais foram os principais desafios durante o desenvolvimento?

O maior desafio foi deixar a estrutura de testes rodando dentro do container alem do fato de lidar com Schemas aninhados para a validação de duas entidades no mesmo endpoint  

- O que você escolheu como arquitetura/framework/banco e por que?

A escolha de Flask e postgress pela facilidade de deixar tudo de pé, alem de já ter lidado anteriormente

- O que falta desenvolver / como poderiamos melhorar o que você entregou?

Poderiamos melhorar automatizando o deploy e adicionar o Swagger ou algum tipo de acesso e documentação gerada para os endpoints

- Python é a melhor escolha para esta atividade? Por que?

Sim, porem, se possivel usaria serverless.

![alt text](https://i.kym-cdn.com/entries/icons/mobile/000/028/021/work.jpg)
