
# forthright-django


forthright-django is a Django app to allow developers to directly call server functions from the client. 

## Quick start

1. `pip install -i https://test.pypi.org/simple/ forthright-django`


2. Add forthright-django to INSTALLED_APPS in your django project settings.py:

```
INSTALLED_APPS = [
	...,
	'forthright_django.apps.ForthrightConfig',
]
```

3. Include the forthright-django URLconf in your django project urls.py:

```
urlpatterns = [
	path('forthright/', include('forthright_django.urls')),
	...,
]
```

4. Instantiate a forthright_server object and export your server functions. For example, place [tests/server_functions.py](./tests/server_functions.py) in your django project folder, and import this file in urls.py

	`from . import server_functions`



