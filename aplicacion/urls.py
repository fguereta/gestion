from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

	path('<int:aerosol_id>/', views.detail, name='detail'),
	path('<int:aerosol_id>/results/', views.results, name='results'),
]