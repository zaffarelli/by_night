'''
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

'''
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

admin.site.site_header = "By Night (Administration)"
admin.site.site_title = "By night"
admin.site.index_title = "Welcome to the By Night collector."

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('collector.urls')),
]
