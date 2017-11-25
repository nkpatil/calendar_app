from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.signin, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/cal/'}),
    url(r'^save_record/', views.save_record, name='save record'),
]
