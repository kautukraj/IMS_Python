from django.conf.urls import url
from .views import *
# It is a mapping between URL path expressions to the views.
# Documentation referred : https://docs.djangoproject.com/en/2.2/topics/http/views/
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_hatchbacks$',display_hatchbacks, name='display_hatchbacks'),
    url(r'^display_sedans$',display_sedans, name='display_sedans'),
    url(r'^display_SUVsMUVs$',display_SUVsMUVs, name='display_SUVsMUVs'),
    url(r'^display_vans$',display_vans, name='display_vans'),
    url(r'^add_hatchback$',add_hatchback, name='add_hatchback'),
    url(r'^add_sedan$',add_sedan, name='add_sedan'),
    url(r'^add_SUVMUV$',add_SUVMUV, name='add_SUVMUV'),
    url(r'^add_van$',add_van, name='add_van'),
    url(r'^edit_hatchback/(?P<pk>\d+)$',edit_hatchback, name='edit_hatchback'),
    url(r'^edit_sedan/(?P<pk>\d+)$',edit_sedan, name='edit_sedan'),
    url(r'^edit_SUVMUV/(?P<pk>\d+)$',edit_SUVMUV, name='edit_SUVMUV'),
    url(r'^edit_van/(?P<pk>\d+)$',edit_van, name='edit_van'),
    url(r'^hatchback/delete/(?P<pk>\d+)$', delete_hatchback, name="delete_hatchback"),
    url(r'^sedan/delete/(?P<pk>\d+)$', delete_sedan, name="delete_sedan"),
    url(r'^SUVMUV/delete/(?P<pk>\d+)$', delete_SUVMUV, name="delete_SUVMUV"),
    url(r'^van/delete/(?P<pk>\d+)$', delete_van, name="delete_van"),

]
