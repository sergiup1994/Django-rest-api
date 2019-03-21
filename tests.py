from django.test import TestCase
from django.urls import include, path
from event_site.models import Match, Market, Selection, Sport
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient, URLPatternsTestCase

# Create your tests here.


class ApiTests(APITestCase):

    def create_event(self):
        url = ('http://127.0.0.1:8000/api/match/')
        data = {
                 "id": 8661032861909884224,
                 "message_type": "NewEvent",
                 "event": {
                     "id": 994839351740,
                     "name": "Real Madrid vs Barcelona",
                     "startTime": "2018-06-20 10:30:00",
                     "sport": {
                         "id": 221,
                         "name": "Football"
                     },
                     "markets": [
                         {
                         "id": 385086549360973392,
                         "name": "Winner",
                         "selections": [
                             {
                             "id": 8243901714083343527,
                             "name": "Real Madrid",
                             "odds": 1.01
                             },
                             {
                             "id": 5737666888266680774,
                             "name": "Barcelona",
                             "odds": 1.01
                             }
                            ]
                        }
                     ]
                    }
                }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Match.objects.get().name, 'Real Madrid vs Barcelona')