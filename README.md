# Django-rest-api
Api to handle incoming data from a sports provider

Django REST api which recives data from a provider and updates the api with the latest data on sporting events.

Models.py: Contains the database structure and behaviour of the data.  
Serializer.py: provides a way to deal with model instances, querrysets and presents data stored in json format.
Url.py: This allows the Django controller to look for corresponding view, and then return the HTML response or a 404 not found. Url.py is where you define the mapping between urls and views.
Viewsets.py: provides abstraction and consistency 
Test.py: test for creating an event.

