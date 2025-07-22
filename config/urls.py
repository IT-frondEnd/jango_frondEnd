
from django.contrib import admin
from django.urls import path
from page.views import test_view
from page.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test_view, name='home'),
    path('home/', home, name='homes'),
]
