from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^execute$', views.execute, name='execute'),
    url(r'^saveFile$', views.saveFile, name='save_file'),
    url(r'^refreshDirectory$', views.refreshDirectory, name='refreshDirect'),
    url(r'^viewfilecontents$', views.viewfilecontents, name='viewfileconts'),
    url(r'^deleteRemoteDir$', views.deleteRemoteDir, name='delRemoteDir'),
    url(r'^renameRemoteFile$', views.renameRemoteFile, name='renameRemoteFile')
]
