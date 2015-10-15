from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
     url(r'^$', 'shortner.views.home', name='home'),
     url(r'^(?P<hash>[a-zA-Z0-9]{8})$', 'shortner.views.extract', name='extract'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^shortner/(?P<pk>[0-9]+)/$','shortner.views.display',name="display"),
    url(r'^admin/', include(admin.site.urls)),
    
]
