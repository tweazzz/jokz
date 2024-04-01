from django_filters import rest_framework as filters
from .models import *


class UniversitiesFilter(filters.FilterSet):
    class Meta:
        model = Universities
        fields = '__all__'
        exclude = ['logo']


class AvailableUniversitiesFilter(filters.FilterSet):
    class Meta:
        model = Universities
        fields = '__all__'
        exclude = ['logo']


class ProffessionsFilter(filters.FilterSet):
    class Meta:
        model = Proffessions
        fields = '__all__'

class InternshipsFilter(filters.FilterSet):
    class Meta:
        model = Internships
        fields = '__all__'
        exclude = ['organization_logo']


class NewsFilter(filters.FilterSet):
    class Meta:
        model = News
        fields = '__all__'
        exclude = ['photo1','photo2','photo3']