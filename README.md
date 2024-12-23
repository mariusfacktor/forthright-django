
# forthright-django


forthright-django is a Django app to allow developers to directly call server functions from the client. 

## Quick start


1. Add "forthright" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "forthright_django",
    ]

2. Include the forthright URLconf in your project urls.py like this::

    path("forthright/", include("forthright_django.urls")),
