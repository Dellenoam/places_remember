# places_remember
This is the site that saves your memories of the places you've visited.

If you want to use it, then you need to do a few things.
## 1. Set your settings
Go to places_remember/setting.py and change these settings to your own
```python
SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}

SOCIAL_AUTH_VK_OAUTH2_KEY = os.environ['VK_KEY']

SOCIAL_AUTH_VK_OAUTH2_SECRET = os.environ['VK_SECRET']
```
You also need to change [API key](https://www.geoapify.com/) in memories/static/memories/js/maps.js

```javascript
fetch("https://api.geoapify.com/v1/geocode/reverse?lat=" + lat.toString() + "&lon=" + lng.toString() + "&apiKey=dc47041477c1448599b4eab4be3141e1", requestOptions)
```
And [one more](https://mapsplatform.google.com/) in memories/templates/memories/new_memory.html

```html
<script defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCtM6oVFNXyJm8rHjiLHE-y4NkmxAA28wE&callback=initMap&v=weekly"></script>
```

## 2. Install requirements and venv
When the previous step is done, you need to install the requirements and venv.

First open your folder in cmd and write this
```
py -m venv venv
```
You created venv now activate it
```
venv/Scripts/activate
```
Install the requirements by writing the following command
```
pip install -r requirements.txt
```
## 3. Done, you can now launch the site
To launch the site you need to write this
```
py manage.py runserver --insecure
```
