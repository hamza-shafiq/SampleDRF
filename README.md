# SampleDRF

### Clone project 
```
git clone git@github.com:hamza-shafiq/SampleDRF.git
```

### Create & Activate Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```
pip3 install -r requirements.txt
```

### Run Migrations
```
python3 manage.py migrate
```

### Edit Swagger Template
```
venv > lib > rest_framework_swagger > templates > index.html
{% load staticfiles %} => {% load static %}
```

### Run Server
```
python3 manage.py runserver
```
