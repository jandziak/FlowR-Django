from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /RBlocks/
    url(r'^$', views.index, name='index'),
    # ex: /RBlocks/index2/
    url(r'^index2/', views.start_page_2),
    url(r'^index/', views.start_page_2),
    # ex: /RBlocks/5/
    url(r'^(?P<type_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /RBlocks/5/results/
    url(r'^(?P<type_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /RBlocks/5/vote/
    url(r'^(?P<type_id>[0-9]+)/vote/$', views.vote, name='vote'),
]