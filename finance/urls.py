from django.conf.urls import patterns, url

urlpatterns = patterns('finance.views',
    url(r'^$', 'index'),
)