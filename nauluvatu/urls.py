from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('datahub.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('lewenilotu/', include('api.urls'))
    

        
]


# Admin Site Config
admin.sites.AdminSite.site_header = 'Tabacakacaka Ko Nauluvatu DATA HUB'
admin.sites.AdminSite.site_title = 'Data Hub'
admin.sites.AdminSite.index_title = 'Tabacakacaka ko Nauluvatu'

