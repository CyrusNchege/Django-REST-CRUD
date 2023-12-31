# Django-REST-CRUD
A repository that contains django application that uses REST framework to create CRUD functionality

## Installation
```
https://github.com/CyrusNchege/Django-REST-CRUD.git
```

```
cd Django-REST-CRUD
```


### Create a virtual environment  and activate environment

#### linux
```
 python3 -m venv env

source env/bin/activate
```
#### windows
```
 python -m venv env

.\env\Scripts\activate

```

### Install requirements
```
pip install -r requirements.txt
```
### Create a .env file

create a .env file and add variables as shown in .env.example

creating a django SECRET_KEY
```
python manage.py shell
```
```
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
copy the generated key and paste it in the .env file

### Make migrations

```
python manage.py makemigrations

python manage.py migrate
```
### Run server
```
python manage.py runserver
```
### Hosted API endpoint (Azure)
[API endpoint](https://cyrus-django-application.azurewebsites.net/api/)

This endpoint is hosted on Azure and is used to perform CRUD operations on the database

Note: It might be deleted after a while

### Database Modelling(UML Diagram)
![UML Diagram](/images/uml.png)

### API Endpoints
```
- POST /api/ - Create a new name

- GET /api/ - Get all names 

- GET /api/<int:pk>/ - Get a single name

- PUT /api/<int:pk>/ - Update a name

- DELETE /api/<int:pk>/ - Delete a name

```


