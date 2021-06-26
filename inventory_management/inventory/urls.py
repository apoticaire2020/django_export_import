from django.conf.urls import url
from django.urls.resolvers import URLPattern
from .views import index , display_laptops , display_desktops  , display_mobiles

urlpatterns = [
    
    url(r'^$' , index , name='index') ,
    
    url(r'^display_laptops$' , display_laptops , name='display_laptops') ,
    
    url(r'^display_desktops$' , display_desktops , name='display_desktops') ,
    
    url(r'^display_mobiles$' , display_mobiles , name='display_mobiles')
    

]