from event_site.models import Match, Sport, Market, Selection
from rest_framework import serializers


class Sport_ser(serializers.ModelSerializer):
    class Meta:
        model = Sport
        components = ('id', 'name')

class Selection_ser(serializers.ModelSerializer):
    class Meta:
        model = Selection
        components = ('id', 'name', 'odds')

class Market_ser(serializers.ModelSerializer):
    selections = Selection_ser(many=True)
    class Meta:
        model = Market
        components = ('id', 'name', 'selections')

class List_of_Matches_ser(serializers.ModelSerializer):
    class Meta:
        model = Match
        components = ('id', 'url', 'name', 'startTime') 


class Match_Detail_Ser(serializers.ModelSerializer):
    sport = Sport_ser()
    market = Market_ser()
    class Meta:
        model = Match
        components = ('id', 'url', 'name', 'startTime', 'sport', 'market')

