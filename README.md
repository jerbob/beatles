# Beatles
A simple proof-of-concept API for rendering and querying beatles songs.

## Running the project
This project uses [`poetry`](https://python-poetry.org/docs/) for dependency management. To install on Linux or MacOS, use the following command:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

To prepare the database, run the following commands:
```
poetry run src/manage.py migrate
```
```
DJANGO_SUPERUSER_USERNAME=evident \
DJANGO_SUPERUSER_PASSWORD=dev_interview \
DJANGO_SUPERUSER_EMAIL=admin@adm.in \
poetry run src/manage.py createsuperuser --no-input
```

And to run the server locally, run the following command:
```
poetry run gunicorn --chdir src -w 12 -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker core.asgi:application
```

The browsable API will now be available in any web browser at http://localhost:8000/songs/. To view the songs individually, click on any `url` field's hyperlink to open the endpoint for that song, and go to `/lyrics` to view the relevant lyrics if they are stored on disk.
