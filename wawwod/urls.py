'''
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

'''
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

admin.site.site_header = "WaWWoD (Administration)"
admin.site.site_title = "WaWWoD"
admin.site.index_title = "Welcome to the WaWWoD collector."

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('collector.urls')),
]