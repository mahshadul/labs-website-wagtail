# ExcellaLabs Wagtail

An implementation of the [ExcellaLabs](https://excellalabs.com) website using the Wagtail CMS.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Docker](https://www.docker.com/community-edition)
- [Docker Compose](https://docs.docker.com/compose/install/) (comes bundled with Docker for Windows and Mac)

### Setup

Build the image and then create and run the containers in the background.
```
docker-compose up -d
```

Ensure the `web` container is up and running correctly by visiting `http://localhost:8000/`

Add a superuser account
```
docker-compose exec web python manage.py createsuperuser
```

Your site should now be fully functional.  Useful URLs for development are:
- ExcellLabs site - `http://localhost:8000`
- Wagtail admin - `http://localhost:8000/admin/`
- Django admin - `http://localhost:8000/django-admin/`