I've added redis for store previous added questions.

I've also created simple GUI with JS and HTML.

You could check it after running compose by 

    http://localhost:8000
You have just write the number in input and click ADD button

![img.png](readme_img/img2.png)
Config docker compose:

If you have an 8000 port bound 

you could select any free port by set it in mapping instead of PORT:

ports:
 
   - "PORT:8000"

![img.png](readme_img/img.png)

You could start compose by 

    docker compose up -d

And stop it by

    docker compose down

If you want to remove all volumes and all images

    docker compose down -v --rmi all


Request Example:

request url: http://localhost:8000/api/v1/questions

request body: {
  "questions_num": 1
}

curl -X 'POST' \
  'http://localhost:8000/api/v1/questions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 1
}'

Project Tree:

    .
    ├── app
    │   ├── alembic.ini
    │   ├── api
    │   │   ├── __init__.py
    │   │   └── v1.py
    │   ├── core
    │   │   ├── config.py
    │   │   ├── dals.py
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   ├── schema.py
    │   │   └── services.py
    │   ├── __init__.py
    │   ├── main.py
    │   ├── migration
    │   │   ├── env.py
    │   │   ├── README
    │   │   ├── script.py.mako
    │   │   └── versions
    │   │       ├── cb34a9e53b12_init.py
    │   ├── static
    │   │   ├── css
    │   │   │   └── style.css
    │   │   ├── index.html
    │   │   └── script
    │   │       └── script.js
    │   └── utils
    │       ├── __init__.py
    ├── docker-compose.yml
    ├── Dockerfile
    ├── poetry.lock
    ├── pyproject.toml
    ├── readme_img
    │   ├── img2.png
    │   └── img.png
    ├── README.MD
    └── tests
        ├── conftest.py
        ├── docker-compose.yml
        ├── __init__.py
        ├── test_dals.py
        ├── test_models.py
        └── test_services.py
  