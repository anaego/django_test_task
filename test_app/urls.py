from django.urls import path
from . import views

app_name = 'test_app'
urlpatterns = [
    # TODO is it test_app?
    path('', views.IndexView.as_view(), name='index'),  # /test_app/
    path('task_2_1/', views.task_2_1, name='task_2_1'),
    path('task_2_2/', views.task_2_2, name='task_2_2'),
    path('task_2_3/', views.task_2_3, name='task_2_3'),
    path('task_3/', views.TaskThreeListView.as_view(), name='task_3')
]
