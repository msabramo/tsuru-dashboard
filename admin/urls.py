from django.conf.urls import patterns, url

from admin import views

urlpatterns = patterns(
    '',
    url(r'^$', views.ListNode.as_view(), name='list-node'),
    url(r'^healing/$', views.ListHealing.as_view(), name='list-healing'),
    url(r'^(?P<address>[http://\w.:1-9-]+)/containers/$', views.ListContainer.as_view(),
        name='list-container'),
    url(r'^deploys/$', views.ListDeploy.as_view(), name='list-deploys'),
    url(r'^deploys/graph$', views.DeploysGraph.as_view(), name='deploys-graph'),
    url(r'^deploys/(?P<deploy>[\s\w@\.-]+)/$', views.DeployInfo.as_view(), name='deploy-info'),
)
