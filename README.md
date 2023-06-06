### Fastapi users

RESTful API для регистрации, авторизации и управления записями пользователей.

#### Технологии
- Python
- FastAPI
- Redis для хранения данных в NoSQL формате
- PostgreSQL для хранения данных пользователей и их записей
- JWT-токены для проверки авторизации пользователей
- slowapi для ограничения количества запросов
- Docker для контейнеризации приложения

## **Запуск проекта**

Выполните следующие команды в терминале:

1. Клонировать проект из репозитория

```
git clone https://github.com/DoDmAnat/fastapi_users
```

2. Перейти в папку проекта и создать файл «.env», добавив в него переменные окружения.

```
cd fastapi_users
```

```
touch .env
```

```
DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=postgres

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

REDIS_HOST=redis
REDIS_PORT=6379
```

3. Выполнить команду запуска docker-compose в «фоновом режиме»

```
docker-compose up -d --build
```

4. Документация

```
localhost:8000/docs
```

Функциональность:

- Регистрация нового пользователя

```

POST - '/register/'

```

- Авторизация пользователя

```

POST - '/login/'

```

- Разлогинивание пользователя

```

POST - '/logout/'

```
#### - Создание новой записи

```
POST - '/tasks/'
```

```json
{
  "title": "string",
  "description": "string"
}
```

#### - Получение списка всех записей

```
GET - '/tasks/'
```


#### - Получение конкретной записи

```
POST - '/tasks/{task_id}/'
```

#### - Изменение записи

```
PUT - '/tasks/{task_id}/'
```

#### - Удаление записи

```
DELETE - '/tasks/{task_id}/'
```

