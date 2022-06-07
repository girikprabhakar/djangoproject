from django.urls import path
from myapp import views
from django.urls import include, path

app_name = 'myapp'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'myapp/', include('myapp.urls')),
    path(r'', views.about, name='about'),
    path(r'myapp/<int:top_no>/', name='detail')
]
