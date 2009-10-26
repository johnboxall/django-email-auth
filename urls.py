from django.conf.urls.defaults import *

urlpatterns += patterns('email_auth.views',
    (r'^login/$', 'login'),
)

urlpatterns += patterns('django.contrib.auth.views',
    (r'^logout/$', 'logout'),
    (r'^password_change/$', 'password_change'),
    (r'^password_change/done/$', 'password_change_done'),
    (r'^password_reset/$', 'password_reset'),
    (r'^password_reset/done/$', 'password_reset_done'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm'),
    (r'^reset/done/$', 'password_reset_complete'),
)