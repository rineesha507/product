# Django Product Management API with Token Authentication

## Project Overview
This project is a simple product management API built using Django and Django Rest Framework (DRF). It supports user authentication with token-based authentication, category management, product listing, and image uploads for products.

## Features
- **User Authentication**: Login using token-based authentication.
- **Category Management**: Create, update, delete, and view product categories.
- **Product Management**: CRUD operations for products, including image uploads.
- **Token-Based Authentication**: Uses `rest_framework.authtoken` for authentication.
- **File Uploads**: Allows product images to be uploaded and stored.

## Technologies Used
- **Django** - Backend framework
- **Django Rest Framework (DRF)** - API development
- **Django Token Authentication** - Token-based authentication
- **SQLite/PostgreSQL** - Database (default: SQLite)

## Installation
### Prerequisites
Ensure you have Python 3 and pip installed on your system.

### Clone the Repository
```sh
git clone https://github.com/rineesha507/product.git
cd product
```

### Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Apply Migrations
```sh
python manage.py migrate
```

### Create a Superuser
```sh
python manage.py createsuperuser
```

### Run the Development Server
```sh
python manage.py runserver
```

## API Endpoints

### Authentication
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/login/` | POST | Login and receive a token |

### Category Management
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/categories/` | GET | List all categories |
| `/categories/` | POST | Create a new category |
| `/categories/{id}/` | GET | Retrieve a category |
| `/categories/{id}/` | PUT | Update a category |
| `/categories/{id}/` | DELETE | Delete a category |

### Product Management
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/products/` | GET | List all products |
| `/products/` | POST | Create a new product with images |
| `/products/{id}/` | GET | Retrieve a product |
| `/products/{id}/` | PUT | Update a product |
| `/products/{id}/` | DELETE | Delete a product |

## Media & Static Files Setup
Ensure that your `settings.py` file includes:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
Update `urls.py`:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Running Tests
To run tests, execute:
```sh
python manage.py test
```

## Deployment
For deployment, configure `ALLOWED_HOSTS` in `settings.py` and use a production server like Gunicorn.

## License
This project is licensed under the MIT License.

