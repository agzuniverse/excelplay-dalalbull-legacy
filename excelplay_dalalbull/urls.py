from django.conf.urls import url,include
from django.contrib import admin
app_name='api'
urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^dalalbull/',include('api.urls'),name='api'),
]
