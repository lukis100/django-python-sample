from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'parse.views.home'),
    url(r'^parse/', 'parse.views.ParseFeed'),
)
