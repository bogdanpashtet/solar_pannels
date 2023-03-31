from django.contrib import admin
from django.urls import path
from main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # path('stations/<int:id>/', )
]
