import json

from django.core import serializers
from django.db.models import Count, Q, F
from django.shortcuts import render
from django.views import generic
from rest_framework.generics import ListAPIView

from test_app.serializers import BSerializer
from .models import A, B


class IndexView(generic.TemplateView):
    template_name = 'test_app/index.html'


def task_2_1(request):
    """ 2.1) Count of "B" instances without related "a". """
    return render(request, 'test_app/task_2_1.html', {'query_result': B.objects.filter(a=None).count()})


def task_2_2(request):
    """ 2.2) "A" queryset with "b_count" field (amount of related "B" instances). """
    return render(request, 'test_app/task_2_2.html', {'query_result': A.objects.annotate(b_count=Count('b')).values()})


def task_2_3(request):
    """ 2.3) "A" queryset where any related "b" has flag=True or without related "b". """
    query_result = A.objects.filter(Q(b__isnull=True) | Q(b__flag=True)).values()
    return render(request, 'test_app/task_2_3.html', {'query_result': query_result})


class TaskThreeListView(ListAPIView):
    queryset = B.objects.all().annotate(a_name=F('a__name')).values('id', 'text', 'a_name', 'a_id')
    serializer_class = BSerializer
