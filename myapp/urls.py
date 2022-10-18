from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('hello', hello_world),
    path('task', task),

    path('shorten/', shorten_url),
    path('redirect/<slug:custom_name>', redirect_url),
    path('all-analytics', all_analytics),
]