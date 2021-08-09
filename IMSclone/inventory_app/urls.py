from django.conf.urls import url
from .views import *
from django.urls import path, include
# It is a mapping between URL path expressions to the views.
# Documentation referred : https://docs.djangoproject.com/en/2.2/topics/http/views/
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin_module$',admin_module, name='admin_module'),
    url(r'^manager_module$',manager_module, name='manager_module'),
    url(r'^display_hatchbacks$',display_hatchbacks, name='display_hatchbacks'),
    url(r'^display_sedans$',display_sedans, name='display_sedans'),
    url(r'^display_SUVsMUVs$',display_SUVsMUVs, name='display_SUVsMUVs'),
    url(r'^display_vans$',display_vans, name='display_vans'),
    url(r'^display_hatchbacks_manager$',display_hatchbacks_manager, name='display_hatchbacks_manager'),
    url(r'^display_sedans_manager$',display_sedans_manager, name='display_sedans_manager'),
    url(r'^display_SUVsMUVs_manager$',display_SUVsMUVs_manager, name='display_SUVsMUVs_manager'),
    url(r'^display_vans_manager$',display_vans_manager, name='display_vans_manager'),
    url(r'^add_hatchback$',add_hatchback, name='add_hatchback'),
    url(r'^add_sedan$',add_sedan, name='add_sedan'),
    url(r'^add_SUVMUV$',add_SUVMUV, name='add_SUVMUV'),
    url(r'^add_van$',add_van, name='add_van'),
    url(r'^edit_hatchback/(?P<pk>\d+)$',edit_hatchback, name='edit_hatchback'),
    url(r'^edit_sedan/(?P<pk>\d+)$',edit_sedan, name='edit_sedan'),
    url(r'^edit_SUVMUV/(?P<pk>\d+)$',edit_SUVMUV, name='edit_SUVMUV'),
    url(r'^edit_van/(?P<pk>\d+)$',edit_van, name='edit_van'),
    url(r'^edit_hatchback_manager/(?P<pk>\d+)$',edit_hatchback_manager, name='edit_hatchback_manager'),
    url(r'^edit_sedan_manager/(?P<pk>\d+)$',edit_sedan_manager, name='edit_sedan_manager'),
    url(r'^edit_SUVMUV_manager/(?P<pk>\d+)$',edit_SUVMUV_manager, name='edit_SUVMUV_manager'),
    url(r'^edit_van_manager/(?P<pk>\d+)$',edit_van_manager, name='edit_van_manager'),
    url(r'^hatchback/delete/(?P<pk>\d+)$', delete_hatchback, name="delete_hatchback"),
    url(r'^sedan/delete/(?P<pk>\d+)$', delete_sedan, name="delete_sedan"),
    url(r'^SUVMUV/delete/(?P<pk>\d+)$', delete_SUVMUV, name="delete_SUVMUV"),
    url(r'^van/delete/(?P<pk>\d+)$', delete_van, name="delete_van"),
    path('accounts/', include('django.contrib.auth.urls')), # for login page
    
]

# pk stands for Primary Key
# ^ matches the start of the string.
# $ matches the end of the string.
# Using r'', Django will look for an empty string anywhere in the URL, which is true for every URL.
# Using both ^ and $ together as ^$ will match an empty line/string.
# (?P<pk>\d+) is used because we are passing pk with it