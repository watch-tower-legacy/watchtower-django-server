from django.urls import path

from . import views

urlpatterns = [
	path("securitysearch/", views.security_search, name='security_search'),
	path("performancedata/", views.performance_data, name='performance_data'),
]