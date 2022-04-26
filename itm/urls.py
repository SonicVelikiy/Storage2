from django.urls import path
from .views import Home,Storage


urlpatterns = [
    path('', Home, name='home'),
    path('/storage', Storage, name='storage')

]