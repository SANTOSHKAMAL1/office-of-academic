from django import forms
from django.contrib import admin
from django.contrib import admin

from academic.forms import jaineventForm
from .models import Event, EventCalendar, Specialization, calendarevents, jainevent

# from advanced_filters.admin import AdminAdvancedFiltersMixin
  # Remove calendarevents

from . import models

####<!-- Dynamic Heading 


#@admin.register(Event)
#class EventAdmin(admin.ModelAdmin):
   # list_display = ("name", "date",)  # Ensure "name" exists in the model

#admin.site.register(models.ClassInfo)
#admin.site.register(models.academicevents)
#list_display = ("name", "description","date",) 

#admin.site.register(models.Shift)
#@admin.register(calendarevents)
#class EventAdmin(admin.ModelAdmin):
   
   #list_display = ("faculty","event_name", "description","event_date","venue","coordinator","pdf",) 
#admin.site.register(models.GuideTeacher)
#admin.site.register(models.ClassRegistration)


#@admin.register(models.ClassInfo)
#class ClassInfoAdmin(admin.ModelAdmin):
 #   list_display = ('name', 'display_name')-->
    # advanced_filter_fields = ('name', 'display_name')#####-->
from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import EventCalendar

# Custom form for EventCalendar to apply Date Picker
#class EventCalendarForm(forms.ModelForm):
    #class Meta:
        #model = EventCalendar
        #fields = '__all__'
        #widgets = {
          #  'event_date': AdminDateWidget(),  # Adds a date picker
      #  }

# Registering the model with custom admin configurations
#@admin.register(EventCalendar)
#lass EventCalendarAdmin(admin.ModelAdmin):
   # form = EventCalendarForm
    #list_display = ('event_name', 'event_date', 'faculty', 'venue','pdf')  # Displayed fields in the admin list view
    #list_filter = ('faculty', 'event_date')  # Filters for easier navigation
    #search_fields = ('event_name', 'venue', 'coordinator')  # Enables search
   # ordering = ('event_date',)  # Orders events by date

   # class Media:
       # """Ensures jQuery UI DatePicker works if needed."""
       # js = ('https://code.jquery.com/ui/1.12.1/jquery-ui.js',)
        #css = {'all': ('https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css',)}






##################################################################
#class jaineventForm(forms.ModelForm):
    #class Meta:
       # model = jainevent
        #fields = '__all__'
        #widgets = {
        #    'event_date': AdminDateWidget(),  # Adds a date picker
        #}




from .models import ComputerScienceandEngineering

from django.contrib import admin
from django.utils.html import format_html
from .models import ComputerScienceandEngineering, Specialization

@admin.register(ComputerScienceandEngineering)
class ComputerScienceandEngineeringAdmin(admin.ModelAdmin):
    list_display = ('department', 'location', 'degree', 'get_specializations')
    search_fields = ('department', 'location', 'director_name', 'degree', 'graduation')
    list_filter = ('location', 'degree', 'graduation')
    ordering = ('department',)

    def get_specializations(self, obj):
        # Generate clickable links to specialization pages
        specializations = obj.specializations.all()
        if specializations.exists():
            return format_html(
                ', '.join(
                    f'<a href="/admin/academic/specialization/{spec.id}/change/">{spec.name}</a>'
                    for spec in specializations
                )
            )
        return '-'
    
    get_specializations.short_description = 'Specializations'






# Registering the model with custom admin configurations
@admin.register(jainevent)
class jaineventAdmin(admin.ModelAdmin):
    form = jaineventForm
    list_display = ('event_name', 'event_date', 'faculty', 'venue','pdf')  # Displayed fields in the admin list view
    list_filter = ('faculty', 'event_date')  # Filters for easier navigation
    search_fields = ('event_name', 'venue', 'coordinator')  # Enables search
    ordering = ('event_date',)  # Orders events by date

    class Media:
        """Ensures jQuery UI DatePicker works if needed."""
        js = ('https://code.jquery.com/ui/1.12.1/jquery-ui.js',)
        css = {'all': ('https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css',)}
from django.contrib import admin
from .models import Specialization, Module

class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [ModuleInline]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('specialization', 'semester', 'modulelist')


