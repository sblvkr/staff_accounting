from django.urls import path

from staff import views


app_name = 'staff'

urlpatterns = [
    path('', views.employer_list, name='employer_list'),
    path('employers/create/', views.employer_create, name='employer_create'),
    path('employers/<int:employer_id>/edit/', views.employer_edit, name='employer_edit'),
    path('employers/<int:employer_id>/remove/', views.employer_remove, name='employer_remove'),

    path('positions/', views.positions_list, name='positions_list'),
    path('positions/create/', views.position_create, name='position_create'),
    path('positions/<int:position_id>/edit/', views.position_edit, name='position_edit'),
    path('positions/<int:position_id>/remove/', views.position_remove, name='position_remove'),
]
