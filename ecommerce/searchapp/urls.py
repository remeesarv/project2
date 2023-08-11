from django.urls import path
from . import views
from .views import searchresult

app_name='searchapp'
urlpatterns = [
    path('',views.searchresult,name='searchresult'),
]