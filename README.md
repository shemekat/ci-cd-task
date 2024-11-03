# Task Приложение на Python

Этот проект представляет собой простое приложение, написанное на Python, которое распределяет количество золотых слитков среди трех кошельков.

## Файлы
- `app/app.py` - Основной файл приложения.
- `Dockerfile` - Dockerfile для сборки Docker-образа.
- `.github/workflows/docker-ci.yml` - GitHub Actions workflow для CI/CD.

## Предварительные условия
- [Docker](https://www.docker.com/get-started)
- [GitHub аккаунт](https://github.com/) с доступом к GitHub Actions
- [Docker Hub аккаунт](https://hub.docker.com/)

## Запуск приложения локально

### Использование Docker

1. **Клонирование репозитория:**
    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Сборка Docker-образа:**
    ```sh
    docker build -t bytescriptdev/task_container:latest .
    ```

3. **Запуск Docker-контейнера:**
    ```sh
    docker run -it --name my_container bytescriptdev/task_container:latest
    ```

## CI/CD Pipeline

### GitHub Actions Workflow

Файл GitHub Actions workflow `.github/workflows/docker-ci.yml` настроен на автоматическую сборку и публикацию Docker-образа в Docker Hub при каждом push в ветку `main`.

### Шаги:

1. **Сборка Docker-образа:**
    Workflow клонирует код, настраивает Docker Buildx и собирает Docker-образ с использованием предоставленного Dockerfile.

2. **Публикация Docker-образа:**
    Workflow входит в Docker Hub с использованием секретов, указанных в настройках репозитория, а затем отправляет Docker-образ в Docker Hub.

## Доступ к Docker-образу

Docker-образ опубликован в Docker Hub и может быть загружен с использованием следующей команды:

```sh
docker pull bytescriptdev/task_container:main
