# Bike Rental Service

## Установка и запуск

### Локальный запуск

1. Клонируйте репозиторий:
    ```bash
    git clone https://your-repository-url.git
    cd api_bikes/bike_rental
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

### Запуск с Docker

1. Перейдите в директорию:
    ```bash
    cd api_bikes/bike_rental
    ```

2. Запустите контейнеры:
    ```bash
    docker compose up --build
    ```

3. Выполните миграции:
    ```bash
    docker compose -f docker/docker-compose.yml exec web python manage.py makemigrations
    docker compose -f docker/docker-compose.yml exec web python manage.py migrate
    ```
Приложение будет доступно по адресу `http://localhost:8000`

### Документация API

Документация API доступна по адресу `http://localhost:8000/swagger/`

## Тестирование

Для запуска тестов используйте команду:
```bash
pytest
```

### 9. Примеры запросов для тестирования API

#### Регистрация пользователя
```http
POST /api/users/register/
Content-Type: application/json

{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "testpassword"
}

#### Авторизация пользователя
POST /api/users/token/
Content-Type: application/json

{
    "username": "testuser",
    "password": "testpassword"
}

#### Получение списка доступных велосипедов
GET /api/bikes/
Authorization: Bearer <token>

#### Аренда велосипеда
POST /api/rentals/rent/
Authorization: Bearer <token>
Content-Type: application/json

#### Возврат велосипеда
POST /api/rentals/return/
Authorization: Bearer <token>

#### Получение истории аренды пользователя
GET /api/rentals/history/
Authorization: Bearer <token>
