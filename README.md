# teste-supera-back

Após as instruções de como rodar a aplicação há algumas observações sobre sua construção e os endpoints disponíveis.

## Acesso à aplicação 
Para facilitar o acesso à aplicação, optei por fazer deploy no render. Assim, ela pode ser acessada através do link: "https://teste-supera-back.onrender.com/api/{rota desejada: users/products/orders}/". Acessar esse link dará acesso aos templates do Django Rest Framework, onde é possível ter um retorno visual do banco de dados. Esse deploy está conectado com um banco postgres no próprio render, conforme solicitado pelos requisitos do teste.

### Mas também é possível rodar a aplicação localmente:

Para rodar localmente a aplicação é necessário primeiro abrir um terminal na pasta teste-supera-back. Para rodar o servidor é necessário um ambiente virtual do python. Para criá-lo basta rodar o comando

```
python -m venv venv
```

Em seguida é necessário ativá-lo:

```
source venv/bin/activate
```

E então instalar as libs do projeto (que podem ser encontradas no arquivo requirements.txt) com o comando seguinte: 

```
pip install -r requirements.txt
```

Também é necessário rodar as migrações. Isso criará um arquivo db.sqlite3 que funcionará como banco de dados de ambiente de desenvolvimento:

```
python manage.py migrate
```

Por fim, basta rodar o servidor com:

```
python manage.py runserver
```

Um link aparecerá com a porta em que o servidor está rodando ("Starting development server at..."). Acessar esse link também dará acesso aos templates do Django Rest Framework, onde é possível ter um retorno visual do banco de dados. É importante notar que é necessário adicionar o final da URL ao link fornecido, já que não existe rota '/' no projeto. Portanto, para visualizar os dados dos produtos registrados o link deve ser "{link fornecido no terminal}api/produtos/" e assim por diante para as outras rotas.
É importante lembrar que ao rodar o servidor localmente o DB utilizado pela aplicação será o db.sqlite3 por padrão. Optei por deixar assim graças à praticidade do sqlite3 para ambientes de desenvolvimento locais. Porém, reitero que o requisito de utilizar o postgres foi cumprido no deploy da aplicação, pois o render necessariamente utiliza o postgres como DB. Também é fundamental lembrar que, caso a aplicação esteja rodando localmente o deploy do front não funcionará, pois no repositório o link utilizado foi aquele do deploy no render. Portanto, optar por rodar o server locamente implica na necessidade de rodar o front também locamente, já que será necessário alterar a configuração do axios no arquivo api.js na pasta services na src do nosso front-end e passar o link que retorna após o comando python manage.py runserver mencionado acima.

Pronto! O servidor está rodando.

### Sobre a aplicação:
Há três entidades, users, products e orders. Eles podem ser acessados através dos endpoints "{url, seja local ou a do deploy}/api/users/", "{url, seja local ou a do deploy}/api/products/" e "{url, seja local ou a do deploy}/api/orders/", respectivamente. Além delas, há também a rota "{url, seja local ou a do deploy}/api/login/", utilizada para login. 
Para cada uma das entidades as rotas disponíveis são GET, POST, PATCH e DELETE. A lógica exigida pelos requisitos do teste pode ser encontrada nos arquivos views.py e serializers.py de cada um dos apps da aplicação django. Por opção própria, também desenvolvi validadores de email e cpf que impedem o cadastro de usuários com o mesmo email ou cpf ja existentes no banco. O filtro de produtos foi desenvolvido no views.py do app products. Também desenvolvi uma tabela pivô customizada para a relação ManyToMany existente entre users e orders. Optei por fazer isso para que eu pudesse adicionar, através da lógica desenvolva no serializers.py do app orders, a quantidade de produtos iguais pedida a cada compra, caso o usuário comprasse dois ou mais produtos idênticos na mesma compra. Essa quantidade fica armazenada na tabela pivô chamada OrdersRelation encontrada no arquivo models.py do app orders. No entanto, o usuário não tem retorno visual sobre essa informação na listagem porque como o foco do teste é o back, preferi focar em outras features, já que um retorno visual dessa informação é de fácil implementação. Caso a aplicação esteja sendo rodada locamente é possível consultar a tabela no db e verificar o cálculo das quantidades de produtos iguais por pedido. Optei também por incluir rotas extras não solicitadas, como PATCH, DELETE e GET na função retrieve (em que só um objeto é localizado através do id) simplesmente porque as generics views do django permitem um rápido desenvolvimento dessas rotas. Por fim, mais uma informação importante dis respeito à lógica de funcionamento da listagem de produtos do próprio usuário: ela foi desenvolvida nas views do app orders e tal busca é realizada através do token do usuário logado. Portanto, caso um cliente HTTP como insomnia ou postman seja utilizado para os testes, basta inserir o token de login para que o usuário seja reconhecido pela aplicação e somente os seus pedidos retornem na resposta. Segue também em anexo um diagrama com a modelagem do banco que utilizei para desenvolver as entidades.
