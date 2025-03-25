from django import forms
from . import models
from academic.models import ClassRegistration, calendarevents
from .models import ComputerScienceandEngineering, EventCalendar, jainevent  # Ensure EventCalendar exists in models.py

class calendareventsForm(forms.ModelForm):
    class Meta:
        model = calendarevents
        fields = '__all__'
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            '': forms.Select(attrs={'class': 'form-control'}),
        }
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
class eventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            '': forms.Select(attrs={'class': 'form-control'}),
        }
class ClassForm(forms.ModelForm):
    class Meta:
        model = models.ClassInfo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    class academiceventsForm(forms.ModelForm):
     class Meta:
        model = models.academicevents
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SectionForm(forms.ModelForm):
    class Meta:
        model = models.Section
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SessionForm(forms.ModelForm):
    class Meta:
        model = models.Session
        fields = '__all__'
        widgets = {
            'name': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ShiftForm(forms.ModelForm):
    class Meta:
        model = models.Shift
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClassRegistrationForm(forms.ModelForm):
    class Meta:
        model = ClassRegistration
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'class_name': forms.Select(attrs={'class': 'form-control'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
            'session': forms.Select(attrs={'class': 'form-control'}),
            'shift': forms.Select(attrs={'class': 'form-control'}),
            'guide_teacher': forms.Select(attrs={'class': 'form-control'}),
        }

class GuideTeacherForm(forms.ModelForm):
    class Meta:
        model = models.GuideTeacher
        fields = '__all__'
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
        }
from django import forms
from .models import EventCalendar

class EventCalendarForm(forms.ModelForm):
    event_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
    )
    image = forms.ImageField(required=False)
    pdf = forms.FileField(required=False)

    class Meta:
        model = EventCalendar
        fields = '__all__'  # Include all fields
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'faculty': forms.Select(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'coordinator': forms.TextInput(attrs={'class': 'form-control'}),
        }


##########################################
class jaineventForm(forms.ModelForm):
    event_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
    )
    image = forms.ImageField(required=False)
    class Meta:
        model = jainevent
        fields = '__all__'  # Include all fields
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'faculty': forms.Select(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'coordinator': forms.TextInput(attrs={'class': 'form-control'}),
        }
class ComputerScienceandEngineeringForm(forms.ModelForm):
    class Meta:
        model = ComputerScienceandEngineering
        fields = '__all__'

from django import forms
from .models import Module, ModuleYearPDF

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['semester', 'modulelist']  # ✅ No 'pdf' or 'submitted_by'

class ModuleYearPDFForm(forms.ModelForm):
    class Meta:
        model = ModuleYearPDF
        fields = ['year', 'pdf', 'submitted_by']  # ✅ PDF upload handled separately
