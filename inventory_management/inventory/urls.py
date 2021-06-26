from django.conf.urls import url
from django.urls.resolvers import URLPattern
from .views import index

urlpatterns = [
    
    url(r'^$' , index , name='index')


]