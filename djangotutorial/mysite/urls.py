from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', lambda request: HttpResponse("Bem-vindo ao site!")),  # simples mensagem de boas-vindas
]