from django.urls import path
from school.views import get_pupils

urlpatterns = [
    path('', get_pupils),

]