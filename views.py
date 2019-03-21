from django.shortcuts import render

from django.shortcuts import render
from event_site.models import Match, Sport, Selection, Market
from event_site.serializers import MatchListSerializer, MatchDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

# Create your views here.

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializers =  List_of_Matches_ser # for list view
    detail_serializer = Match_Detail_Ser # for detail view
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = '__all__'

    def serializer(self):
        """Decide on the view to use"""
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer'):
                return self. detail_serializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = Match.objects.all()
        sport = self.request.query_params.get('sport', None)
        name = self.request.query_params.get('name', None)
        return queryset

    def create(self, request):
        """
        create a new match or update existing odds.
        """
        message = request.data.pop('message_type')
        # check if incoming request is for event creation
        if message == "NewEvent":
            event = request.data.pop('event')
            sport = event.pop('sport')
            markets = event.pop('markets')[0]
            selections = markets.pop('selections')
            sport = Sport.objects.create(**sport)
            markets = Market.objects.create(**markets, sport=sport)
            for selection in selections:
                markets.selections.create(**selection)
            match = Match.objects.create(**event, sport=sport, market=markets)
            return Response(status=status.HTTP_201_CREATED)
        # check if incoming request is for updating odds
        elif message == "UpdateOdds":
            event = request.data.pop('event')
            markets = event.pop('markets')[0]
            selections = markets.pop('selections')
            for selection in selections:
                s = Selection.objects.get(id=selection['id'])
                s.odds = selection['odds']
                s.save()
            match = Match.objects.get(id=event['id'])
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)