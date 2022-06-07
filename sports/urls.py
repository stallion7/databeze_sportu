from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sporty/', views.sportListView.as_view(), name='sporty'),
    path('sporty/<int:pk>', views.sportDetaily.as_view(), name='sporty_detail')

]