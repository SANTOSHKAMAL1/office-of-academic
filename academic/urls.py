from django.urls import path

from . import views

urlpatterns = [
     path('calendarevents', views.calendarevents, name='calendarevents'),
    path('events', views.events, name='events'),
    path('add-department', views.add_department, name='add-department'),
    path('create-class', views.add_class, name='create-class'),
    path('create-section', views.create_section, name='create-section'),
    path('create-session', views.create_session, name='create-session'),
    path('create-shift', views.create_shift, name='create-shift'),
    path('class-registration', views.class_registration, name='class-registration'),
    path('class-list', views.class_list, name='class-list'),
    path('guide-teacher', views.create_guide_teacher, name='guide-teacher'),
    path('calendarevents', views.EventCalendar, name='eventcalendar'),
    path('jainevent/', views.jainevent_view, name='jainevent'),
    path('computerscienceeng', views.computerscienceeng, name='computerscienceeng'),
    path('cse_list/', views.cse_list, name='cse_list'),
    path('cse/<int:pk>/', views.cse_detail, name='cse_detail'),
    path('specialization/<int:pk>/', views.specialization_detail, name='specialization_detail'),
    path('module/<int:module_id>/', views.module_detail, name='module_detail'), 
      
   path('delete_pdf/<int:pdf_id>/', views.delete_pdf, name='delete_pdf'),  # Add this line

]
