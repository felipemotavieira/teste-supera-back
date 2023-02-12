# teste-supera-back

## Acesso à aplicação 
Para facilitar o acesso à aplicação, optei por fazer deploy no render. Assim, ela pode ser acessada através do link: "https://teste-supera-back.onrender.com/api/{rota desejada: users/products/orders}/". Acessar esse link dará acesso aos templates do Django Rest Framework, onde é possível ter um retorno visual do banco de dados. Esse deploy está conectado com um banco postgres no próprio render, conforme solicitado pelos requisitos do teste.

### Mas também é possível rodar a aplicação locamente:

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
É importante lembrar que ao rodar o servidor localmente o DB utilizado pela aplicação será o db.sqlite3 por padrão. Optei por deixar assim graças à praticidade do sqlite3 para ambientes de desenvolvimento locais. Porém, reitero que o requisito de utilizar o postgres foi cumprido no deploy da aplicação, pois o render necessariamente utiliza o postgres como DB.

Pronto! O servidor está rodando.
