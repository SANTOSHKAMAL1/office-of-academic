from django.urls import path
from . import views
from .views import detail

from django.urls import path



urlpatterns = [
    path('login', views.admin_login, name='login'),
    path('logout', views.admin_logout, name='logout'),
    path('designation', views.add_designation, name='designation'),
   
   path('school', views.admin_school, name='school'),
   path('department', views.admin_department, name='department'),
   path('designation/<int:id>/', detail, name='detail'),
   path('add/', views.designation_detail, name='designation_detail'),
   
  

    path('departments/', views.department_list, name='department_list'),
    path('facultyofmanagement/', views.facultyofmanagement, name='facultyofmanagement'),
    path('engineering_and_technology/', views.engineering_and_technology, name='engineering_and_technology'),
   

    path('bangalorebba/', views.bangalore_bba, name='bangalorebba'),
    path('bangalorebms/', views.bangalore_bms, name='bangalorebms'),
    path('bangaloremba/', views.bangalore_mba, name='bangaloremba'),
    path('kochibba/', views.kochi_bba, name='kochibba'),
    path('kochimba/', views.kochi_mba, name='kochimba'),

]


    


