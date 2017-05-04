from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('learning_logs.urls', namespace='learning_logs')),
    url(r'users/', include('users.urls', namespace='users')),
    #redirect after login
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='learning_logs/index.html'), name='home'),
]
