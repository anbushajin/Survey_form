from django.urls import path, include
from .views import *
urlpatterns = [
    path('',dashboard),
    path('home/', home ),
    path('question/',question),
    path('survey/',survey)
]
