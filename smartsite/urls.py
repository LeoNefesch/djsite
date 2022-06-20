from django.contrib import admin
from django.urls import include, path
from researchers.views import categories, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('researchers/', include('researchers.urls')),
]
