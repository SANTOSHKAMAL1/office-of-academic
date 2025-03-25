from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Event(models.Model):  # Model names are usually singular
    name = models.CharField(max_length=255)  # Ensure this field exists
    date = models.DateField()

class ClassInfo(models.Model):
    name = models.CharField(max_length=45, unique=True)
    description= models.CharField(max_length=10, unique=True)
    date = models.DateField(auto_now_add=True)



   


class academicevents(models.Model):
    name = models.CharField(max_length=45, unique=True)
    description = models.CharField(max_length=100, unique=True)  # Increased length for better descriptions
    date = models.DateField(auto_now_add=True)

   

  

    
class Section(models.Model):
    name = models.CharField(max_length=45, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.IntegerField(unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Shift(models.Model):
    name = models.CharField(max_length=45, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class GuideTeacher(models.Model):
    name = models.OneToOneField('teacher.PersonalInfo', on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class ClassRegistration(models.Model):
    name = models.CharField(max_length=10, unique=True)
    department_select = (
        ('general', 'General'),
        ('science', 'Science'),
        ('business', 'Business'),
        ('humanities', 'Humanities')
    )
    department = models.CharField(choices=department_select, max_length=15)
    class_name = models.ForeignKey(ClassInfo, on_delete=models.CASCADE, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, null=True)
    guide_teacher = models.OneToOneField(GuideTeacher, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['class_name', 'section', 'shift', 'guide_teacher']

    def __str__(self):
        return self.name
    
from django.db import models

class calendarevents(models.Model):
    FACULTY_CHOICES = (
        ('engineering', 'Faculty of Engineering and Technology'),
        ('arts_humanities', 'Faculty of Arts, Humanities and Social Sciences'),
        ('basic_applied_sciences', 'Faculty of Basic and Applied Sciences'),
        ('commerce', 'Faculty of Commerce'),
        ('management', 'Faculty of Management Studies'),
        ('creativity_design', 'Faculty of Creativity and Design'),
    )
    
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    description = models.TextField()
    faculty = models.CharField(max_length=50, choices=FACULTY_CHOICES)
    venue = models.CharField(max_length=255)
    coordinator = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    pdf = models.FileField(upload_to='event_pdfs/', blank=True, null=True)
    
    def __str__(self):
        return self.event_name

#class calanderevents(models.Model):]
from django.db import models

class EventCalendar(models.Model):
    
    FACULTY_CHOICES = (
        ('engineering', 'Faculty of Engineering and Technology'),
        ('arts_humanities', 'Faculty of Arts, Humanities and Social Sciences'),
        ('basic_applied_sciences', 'Faculty of Basic and Applied Sciences'),
        ('commerce', 'Faculty of Commerce'),
        ('management', 'Faculty of Management Studies'),
        ('creativity_design', 'Faculty of Creativity and Design'),
    )
    
    event_name = models.CharField(max_length=255)
    event_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    faculty = models.CharField(max_length=50, choices=FACULTY_CHOICES)
    venue = models.CharField(max_length=255)
    coordinator = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    pdf = models.FileField(upload_to='event_pdfs/', blank=True, null=True)

    class Meta:
        ordering = ['event_date']  # Orders events by date
    class Media:
        js = ('https://code.jquery.com/ui/1.12.1/jquery-ui.js',)
        css = {'all': ('https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css',)}
    def __str__(self):
        return self.event_name



class jainevent(models.Model):
    
    FACULTY_CHOICES = (
        ('Faculty of Engineering and Technology', 'Faculty of Engineering and Technology'),
        ('Faculty of Arts, Humanities and Social Sciences', 'Faculty of Arts, Humanities and Social Sciences'),
        ('Faculty of Basic and Applied Sciences', 'Faculty of Basic and Applied Sciences'),
        ('Faculty of Commerce', 'Faculty of Commerce'),
        ('Faculty of Management Studies', 'Faculty of Management Studies'),
        ('Faculty of Creativity and Design', 'Faculty of Creativity and Design'),
    )
    
    event_name = models.CharField(max_length=255)
    event_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    faculty = models.CharField(max_length=50, choices=FACULTY_CHOICES)
    venue = models.CharField(max_length=255)
    coordinator = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    pdf = models.FileField(upload_to='event_pdfs/', blank=True, null=True)

    class Meta:
        ordering = ['event_date']  # Orders events by date
    class Media:
        js = ('https://code.jquery.com/ui/1.12.1/jquery-ui.js',)
        css = {'all': ('https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css',)}
    def __str__(self):
        return self.event_name



from django.db import models

class ComputerScienceandEngineering(models.Model):
    # Fixed value for school
    SCHOOL_FIXED = 'School of Computer Science and Engineering'
    
    # Fixed value for department
    DEPARTMENT_FIXED = 'Department of Computer Science and Engineering'

    LOCATION_CHOICES = (
        ('bangalore', 'Bangalore'),
        ('kochi', 'Kochi'),
    )

    GRADUATION_CHOICES = (
        ('ug', 'Undergraduate'),
        ('pg', 'Postgraduate'),
    )

    DEGREE_CHOICES = (
        ('btech', 'B.Tech'),
        ('mtech', 'M.Tech'),
    )

    school = models.CharField(max_length=100, default=SCHOOL_FIXED, editable=False)
    department = models.CharField(max_length=100, default=DEPARTMENT_FIXED, editable=False)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    graduation = models.CharField(max_length=100, choices=GRADUATION_CHOICES)
    degree = models.CharField(max_length=100, choices=DEGREE_CHOICES)
    
    director_name = models.CharField(max_length=100, blank=True, null=True)
    director_email = models.EmailField(blank=True, null=True)
    deputy_director_name = models.CharField(max_length=100, blank=True, null=True)
    deputy_director_email = models.EmailField(blank=True, null=True)
    hod_name = models.CharField(max_length=100, blank=True, null=True)
    hod_email = models.EmailField(blank=True, null=True)
    
    # Many-to-Many Relationship for Specializations
    specializations = models.ManyToManyField('Specialization', blank=True)
    
    employee_count = models.IntegerField(blank=True, null=True)
    student_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.department} - {self.get_location_display()}"

from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=255, unique=True)  
    description = models.TextField(blank=True, null=True)
    pdf = models.FileField(upload_to='specialization_pdfs/', blank=True, null=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='modules')
    semester = models.IntegerField()
    modulelist = models.CharField(max_length=255)  # Name of the module

    def __str__(self):
        return f"{self.modulelist} (Sem {self.semester})"

class ModuleYearPDF(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='year_pdfs')
    year = models.IntegerField()
    pdf = models.FileField(upload_to='modules_pdfs/', blank=True, null=True)
    submitted_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.module.modulelist} - {self.year}"






