from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from academic.models import ClassRegistration
from django.http import HttpResponseForbidden, JsonResponse
from .models import academicevents
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import calendarevents  # Ensure this matches your model name
from .forms import calendareventsForm
from django.shortcuts import render, redirect
from .models import EventCalendar
from .forms import EventCalendarForm


@login_required(login_url='login')
def add_department(request):
    forms = DepartmentForm()
    if request.method == 'POST':
        forms = DepartmentForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('add-department')
    department = Department.objects.all()
    context = {'forms': forms, 'department': department}
    return render(request, 'academic/add-department.html', context)

def academicevents(request):
    events_list = list(academicevents.objects.values())  # Fetch all records as a list of dictionaries
    return JsonResponse({'academic_events': events_list})
                        
def events(request):
    if request.method == "POST":
        form = eventForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = eventForm()

    events = Event.objects.all()  # Fetch all events

    return render(request, 'academic/events.html', {'form': form, 'events': events})


def add_class(request):

    forms = ClassForm()
    if request.method == 'POST':
        forms = ClassForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('create-class')
    class_obj = ClassInfo.objects.all()
    context = {
        'forms': forms,
        'class_obj': class_obj
    }
    return render(request, 'academic/create-class.html', context)

def create_section(request):
    forms = SectionForm()
    if request.method == 'POST':
        forms = SectionForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('create-section')
    section = Section.objects.all()
    context = {
        'forms': forms,
        'section': section
    }
    return render(request, 'academic/create-section.html', context)

def create_session(request):
    forms = SessionForm()
    if request.method == 'POST':
        forms = SessionForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('create-session')
    session = Session.objects.all()
    context = {
        'forms': forms,
        'session': session
    }
    return render(request, 'academic/create-session.html', context)

def create_shift(request):
    forms = ShiftForm()
    if request.method == 'POST':
        forms = ShiftForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('create-shift')
    shift = Shift.objects.all()
    context = {
        'forms': forms,
        'shift': shift
    }
    return render(request, 'academic/create-shift.html', context)

def class_registration(request):
    forms = ClassRegistrationForm()
    if request.method == 'POST':
        forms = ClassRegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('class-list')
    context = {'forms': forms}
    return render(request, 'academic/class-registration.html', context)

def class_list(request):
    register_class = ClassRegistration.objects.all()
    context = {'register_class': register_class}
    return render(request, 'academic/class-list.html', context)

def create_guide_teacher(request):
    forms = GuideTeacherForm()
    if request.method == 'POST':
        forms = GuideTeacherForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('guide-teacher')
    guide_teacher = GuideTeacher.objects.all()
    context = {
        'forms': forms,
        'guide_teacher': guide_teacher
    }
    return render(request, 'academic/create-guide-teacher.html', context)



def calendarevents(request, event_id=None):
    if event_id:
        event = get_object_or_404(calendarevents, id=event_id)
    else:
        event = None
    
    if request.method == 'POST':
        form = calendareventsForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('calendarevents')  # Change this to your event list view name
    else:
        form = calendareventsForm(instance=event)
    
    return render(request, 'academic/calendarevents.html', {'form': form, 'event': event})





    def EventCalendar(request):
        if request.method == "POST":
            form = EventCalendarForm(request.POST, request.FILES)  # Handle file uploads
            if form.is_valid():
                form.save()
                return redirect('event_calendar')  # Redirect to avoid form resubmission

        else:
            form = EventCalendarForm()

        events = EventCalendar.objects.all().order_by('event_date')  # Fetch and order events by date

        return render(request, 'academic/eventcalendar.html', {'form': form, 'events': events})


def jainevent_view(request):
    if request.method == "POST":
        form = jaineventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jainevent_list')
    else:
        form = jaineventForm()
    
    events = jainevent.objects.all().order_by('event_date')
    return render(request, 'academic/jainevent.html', {'form': form, 'events': events})



from django.shortcuts import render
from .models import academicevents

def computerscienceeng(request):
    # Fetch all events from the model
    return render(request, 'academic/computerscienceeng.html')


##############
def cse_list(request):
    cse_data = ComputerScienceandEngineering.objects.all()
    return render(request, 'academic/cse_list.html', {'cse_data': cse_data})

def cse_detail(request, pk):
    cse = get_object_or_404(ComputerScienceandEngineering, pk=pk)
    return render(request, 'academic/cse_detail.html', {'cse': cse})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Specialization, Module
from .forms import ModuleForm

from django.shortcuts import get_object_or_404, redirect, render
from .models import Specialization, Module
from .forms import ModuleForm

def specialization_detail(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    modules = Module.objects.filter(specialization=specialization).order_by('semester')

    if request.method == 'POST':
        form = ModuleForm(request.POST, request.FILES)
        if form.is_valid():
            new_module = form.save(commit=False)
            new_module.specialization = specialization
            new_module.save()
            return redirect('academic/specialization_detail', pk=pk)
    else:
        form = ModuleForm()

    context = {
        'specialization': specialization,
        'modules': modules,
        'form': form
    }
    return render(request, 'academic/specialization_detail.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from .models import Module, ModuleYearPDF
from .forms import ModuleYearPDFForm

def module_detail(request, module_id):
    module = get_object_or_404(Module, pk=module_id)
    year_pdfs = module.year_pdfs.all().order_by('-year')  # Get PDFs for all years

    if request.method == "POST":
        form = ModuleYearPDFForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_entry = form.save(commit=False)
            pdf_entry.module = module  # Assign the module
            pdf_entry.save()
            return redirect('module_detail', module_id=module.id)
    else:
        form = ModuleYearPDFForm()

    return render(request, 'academic/module_detail.html', {'module': module, 'year_pdfs': year_pdfs, 'form': form})
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)  # ✅ Logging for debugging

def delete_pdf(request, pdf_id):
    logger.info(f"Delete request received for PDF ID: {pdf_id}")  # ✅ Log request

    if request.method == "POST":  # ✅ Ensure it's a POST request
        pdf_entry = get_object_or_404(ModuleYearPDF, id=pdf_id)
        pdf_entry.delete()
        messages.success(request, "PDF deleted successfully!")
        return JsonResponse({"success": True})  # ✅ Return JSON response

    logger.warning("Invalid request method. Expected POST.")
    return HttpResponseForbidden("Invalid request method.")
