from django.urls import path
from . import views

urlpatterns=[
    path('dashboard/',views.dashborad_viwes,name='dashboard'),
    path('employee_list/',views.employee_list_views,name='employee_list'),
    path('department_list/',views.department_list_views,name='department_list'),
    path('create_department/',views.create_department_view,name='create_department'),
    path('create_employee/',views.create_employee_view,name='create_employee'),
    
    #employee profile
    path('create/employee-profile/<int:pk>',views.create_employee_profile_view,name='create_profile'),
]