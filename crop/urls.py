from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
	path('', views.home, name ='crop-home'),
	path('about/', views.about, name ='crop-about'),
	path('upload/', views.photoform, name ='crop-abouta'),
	path('success/', views.success),
	#path('upload/', views.upload, name ='crop-upload'),
	

]


