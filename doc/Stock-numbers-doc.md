
Documentação API's - Estoque de números 
==========

> Documentação referente as API's do `Sistema de controle do estoque de números`.

* Inserir usuário
* Login.
* Inserir número.
* Atualizar número.
* Buscar números.
* Buscar número.
* Remover número.

---
**API**

	BASE_URL: http://127.0.0.1:5000
	
`Headers:`	
Authorization : Bearer ${token} 
> **Observações:** 
	  - O ${token} de acesso para as apis pode ser adquirido na etapa 2 (login), ou usando o usuário padrão criado no ambiente de desenvolvimento: `admin : usH5hRwxiZ`
	  - Documentação focada nas respostas de sucesso das APIs, em caso de erro será apenas retornado no campo "message" ou "data" (em casos de erros multiplos) a descrição correspondente.
---

**1 - Inserção de usuários**

API para cadastro de usuários no sistema.

	ROUTE: /users
	METHOD: POST

> Dados requeridos:

Nome | Tipo | Mínimo | Máximo | Formatação | Obrigatório | Descrição
:--: | :---:|:------:|:------:|:----------:|:-----------:|:--------:|
username | string | 1 | 50 | - | Sim | dado único para login do usuário 
password | string | 8 | - | - | Sim | senha do usuário 
name | string | 1 | 200 | - | Sim | nome do usuário
email | string | 1 | 120 | email | Sim | email do usuário

>Resposta:
 > - id  `(int)`
 > - username `(string)`
 >  - name `(string)`
 > - email `(string)`

	HTTP/1.0 200

Formatação:
```json
{
  "data": {
    "email": "franciscoaap7@gmail.com",
    "id": 1,
    "name": "Francisco Pessoa",
    "username": "francisca"
  },
  "message": "Usuário cadastrado com sucesso"
}
```
> **Validações adicionais:** 
	  - username único por usuário;
	  - email único por usuário;
---

**2 - Login**

API para login de usuário

	ROUTE: /login
	METHOD: POST

> Dados requeridos:

Nome | Tipo | Mínimo | Máximo | Formatação | Obrigatório | Descrição
:--: | :---:|:------:|:------:|:----------:|:-----------:|:--------:|
username | string | 1 | 50 | - | Sim | dado único para login do usuário 
password | string | 8 | - | - | Sim | senha do usuário 



>Resposta:
 > - token  `(string)`

	HTTP/1.0 200

Formatação:
```json
{
  "data": {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2MTUxMzI4ODV9.G9PY5Ku3_H5_kh2jg47y0L9ee_3Jbrs90WqqVxs9_ao"
  },
  "message": "Login efetuado com sucesso"
}
```
> **Validações adicionais:** 
	  - username deve pertencer a algum usuário;
	  - senha fornecida deve condizer com a do username;
---

**3 - Inserir número**

API que insere um novo número na base de dados.

	ROUTE: /numbers
	METHOD: POST

> Dados requeridos:

Nome | Tipo | Mínimo | Máximo | Formatação | Obrigatório | Descrição
:--: | :---:|:------:|:------:|:----------:|:-----------:|:--------:|
value | string | 1 | 25 | - | Sim | Número da linha telefonica 
monthy_price | decimal | - | - | - | Sim | Valor mensal 
setup_price | decimal | - | - | - | Sim | Valor de configuração
currency | string | 1 | 3 | - | Sim | Tipo de moeda

>Resposta:
 > - currency  `(string)`
 > - id `(int)`
 >  - monthy_price `(decimal)`
 > - setup_price `(decimal)`
 > - value `(string)`

	HTTP/1.0 200 
	
Formatação:
```json
{
  "data": {
    "currency": "BRL",
    "id": 1,
    "monthy_price": 1.89,
    "setup_price": 0.00,
    "value": "+55 88 999460004"
  },
  "message": "Número inserido com sucesso"
}
```
> **Validações adicionais:** 
	  - monthy_price deve conter valor maior ou igual a 0;
	  - setup_price deve conter valor maior ou igual a 0;
 	  - value deve ser único;
---


**4 - Atualizar número**

API que atualiza dados do número cadastrado.

	ROUTE: /number/${id}
	METHOD: PUT

> Dados requeridos:

Nome | Tipo | Mínimo | Máximo | Formatação | Obrigatório | Descrição
:--: | :---:|:------:|:------:|:----------:|:-----------:|:--------:|
id | int | - | - | - | Sim | ID do número 
value | string | 1 | 25 | - | Sim | Número da linha telefonica 
monthy_price | decimal | - | - | - | Sim | Valor mensal 
setup_price | decimal | - | - | - | Sim | Valor de configuração
currency | string | 1 | 3 | - | Sim | Tipo de moeda

>Resposta:
 > - currency  `(string)`
 > - id `(int)`
 >  - monthy_price `(decimal)`
 > - setup_price `(decimal)`
 > - value `(string)`
 > 
	HTTP/1.0 200 
	
Formatação:
```json
{
  "data": {
    "currency": "BRL",
    "id": 1,
    "monthy_price": 1.89,
    "setup_price": 0.00,
    "value": "+55 88 999460004"
  },
  "message": "Número atualizado com sucesso"
}
```
> **Validações adicionais:** 
	  - monthy_price deve conter valor maior ou igual a 0;
	  - setup_price deve conter valor maior ou igual a 0;
 	  - value deve ser único, não pode estar cadastrado em outro registro;

---


**4 - Buscar números**

API que busca os números cadastrados na base de dados

	ROUTE: /numbers
	METHOD: GET

> Dados requeridos:

Nome | Tipo | Mínimo | Máximo | Formatação | Obrigatório | Descrição
:--: | :---:|:------:|:------:|:----------:|:-----------:|:--------:|
page | int | 1 | - | - | Sim | Pagina requerida para paginação
limit | int | - | 100 | - | Sim | Limite de registros retornados 

>Resposta:
 > - currency  `(string)`
 > - id `(int)`
 >  - monthy_price `(decimal)`
 > - setup_price `(decimal)`
 > - value `(string)`
 
	HTTP/1.0 200 
	
Formatação:
```json
{
  "data": {
    "paginate": [
      {
        "currency": "BRL",
        "id": 1,
        "monthy_price": 1.89,
        "setup_price": 0.55,
        "value": "+55 8 88999460104"
      },
      {
        "currency": "BRL",
        "id": 2,
        "monthy_price": 1.89,
        "setup_price": 0.00,
        "value": "+55 8 88999460004"
      }
    ],
    "total": 3
  },
  "message": ""
}
```
> **Validações adicionais:** 
	  - caso o limit for maior que 100, será convertido para 100

---


**5 - Buscar número**

API que busca os dados de um determinado número cadastrado.

	ROUTE: /number/${id}
	METHOD: GET

> Dados requeridos:

Nome | Tipo | Mínimo | Máximo | Formatação | Obrigatório | Descrição
:--: | :---:|:------:|:------:|:----------:|:-----------:|:--------:|
id | int | - | - | - | Sim | ID do número 

>Resposta:
 > - currency  `(string)`
 > - id `(int)`
 >  - monthy_price `(decimal)`
 > - setup_price `(decimal)`
 > - value `(string)`
 
	HTTP/1.0 200 
	
Formatação:
```json
{
  "data": {
    "currency": "BRL",
    "id": 1,
    "monthy_price": 1.89,
    "setup_price": 0.00,
    "value": "+55 88 999460004"
  },
  "message": ""
}
```
---

**6 - Remover número**

API que remove um determinado número especificado

	ROUTE: /number/${id}
	METHOD: DELETE

> Dados requeridos:

Nome | Tipo | Mínimo | Máximo | Formatação | Obrigatório | Descrição
:--: | :---:|:------:|:------:|:----------:|:-----------:|:--------:|
id | int | - | - | - | Sim | ID do número 

>Resposta:

	HTTP/1.0 200 
	
Formatação:
```json
{
  "data": "",
  "message": "Número removido com sucesso"
}
```
> **Validações adicionais:** 
	  - o id deve existir na base de dados
