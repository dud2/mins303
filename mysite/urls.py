from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('vitraj.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),

]
