from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'portfolio'
urlpatterns = [
    path("base/",baseview, name="base"),
    path("",homeview, name="home"),
    path("work/",workview, name="work"),
    path("about/",aboutview, name="about"),
    path('contact/', contactview, name='contact'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)