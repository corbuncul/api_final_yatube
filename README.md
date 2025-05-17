# api_yatube
## Описание
Проект api_yatube представляет из себя API для блога.

## Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/corbuncul/api_final_yatube.git
cd yatube_api
```
- Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
- Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
- Выполнить миграции:
```
python3 manage.py migrate
```
- Запустить проект:
```
python3 manage.py runserver
```

## Примеры запросов:

### Получение публикаций
Получить список всех публикаций. При указании параметров `limit` и `offset` выдача работает с пагинацией.
> [GET] http://api.example.org/api/v1/posts/

### Создание публикации
Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
> [POST] http://api.example.org/api/v1/posts/

поле `text` обязательное.

### Получение публикации
Получение публикации по `id`.
> [GET] http://api.example.org/api/v1/posts/{id}/

### Обновление публикации
Обновление (полное/частичное) публикации по `id`. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
> [PUT/PATCH] http://api.example.org/api/v1/posts/{id}/

### Удаление публикации
Удаление публикации по `id`. Удалить публикацию может только автор публикации. Анонимные запросы запрещены.
> [DELETE] http://api.example.org/api/v1/posts/{id}/

### Получение комментариев
Получение всех комментариев к публикации.
> [GET] http://api.example.org/api/v1/posts/{post_id}/comments/

### Добавление комментария
Добавление нового комментария к публикации. Анонимные запросы запрещены.
> [POST] http://api.example.org/api/v1/posts/{post_id}/comments/

### Получение комментария
Получение комментария к публикации по `id`.
> [GET] http://api.example.org/api/v1/posts/{post_id}/comments/{id}/

### Обновление комментария
Обновление (полное/частичное) комментария к публикации по `id`. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
> [PUT/PATCH] http://api.example.org/api/v1/posts/{post_id}/comments/{id}/

### Удаление комментария
Удаление комментария к публикации по `id`. Удалить комментарий может только автор комментария. Анонимные запросы запрещены.
> [DELETE] http://api.example.org/api/v1/posts/{post_id}/comments/{id}/

### Список сообществ
Получение списка доступных сообществ.
> [GET] http://api.example.org/api/v1/groups/

### Информация о сообществе
Получение информации о сообществе по `id`.
> [GET] http://api.example.org/api/v1/groups/{id}/

### Подписки
Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены. Возможен поиск по подпискам по параметру `search`
> [GET] http://api.example.org/api/v1/follow/

### Подписка
Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.
> [POST] http://api.example.org/api/v1/follow/

### Получить JWT-токен
Получение JWT-токена.
> [POST] http://api.example.org/api/v1/jwt/create/

### Обновить JWT-токен
Обновление JWT-токена.
> [POST] http://api.example.org/api/v1/jwt/refresh/

### Проверить JWT-токен
Проверка JWT-токена.
> [POST] http://api.example.org/api/v1/jwt/verify/
