from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from page.views import test_view
from page.views import home, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test_view, name='home'),
    path('home/', home, name='homes'),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
]
