# djangodjango/craseproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Mapeia o app 'craseapp' para o caminho raiz do site ('/')
    # Remova a linha 'path('', RedirectView.as_view(url='crase/', permanent=True)),' se estiver lá.
    path('', include('craseapp.urls')),

    path('admin/', admin.site.urls),
]