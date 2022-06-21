from django.contrib import admin
from django.urls import include, path
from researchers.views import categories, index, pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('researchers.urls')),
]

handler404 = pageNotFound
