from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('id/<int:id>', views.detail, name = 'detail'),
    # re_path('^from/(.*)', views.fromsrc, name = 'fromsrc'),
    # re_path('^type/(.*)', views.newstype, name = 'newstype'),
    # re_path('^src/(.*)', views.src, name = 'src'),
    # re_path('^search/(.*)', views.search, name = 'search'),
]