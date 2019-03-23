from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

GENDER_CHOICES = (
    ('male','Male'),
    ('female', 'Female'),
)

COURSE_CHOICES = (
    ('BEduc','BEduc'),
    ('LAW','LAW'),
    ('BSTAT','BSTAT'),
)

CAMPUS = (
    ('Main campus','Main campus'),
    ('Kampala campus','Kampala campus'),
)

PROGRAMME = (
    ('Weekend','Weekend'),
    ('Evening','Evening'),
    ('Inservice','Inservice'),
)

class Profile(models.Model):
    # background tasks
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # student bio-data
    name = models.CharField(max_length=100,null=True, blank=True, help_text="eg. First Last")
    slug = models.SlugField()
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    phone_number = models.IntegerField(blank=True, null=True, help_text="0700000000")
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    birth_certificate = models.FileField(null=True, blank=True, upload_to='birthCerts/%Y/%m')
    id_scan = models.FileField(null=True, blank=True, upload_to='ids/%Y/%m')

    # next-of-kin info
    next_of_kin_name = models.CharField(max_length=100,null=True, blank=True)
    next_of_kin_tel_number = models.CharField(max_length=100, null=True, blank=True)

    # primary school info
    primary_school = models.CharField(max_length=100, null=True, blank=True)
    aggregates = models.IntegerField()
    PLE_Certificate = models.FileField(null=True, blank=True, upload_to='PLE-certs/%Y/%m')

    # Olevel school info
    olevel_school = models.CharField(max_length=100, null=True, blank=True)
    aggregates = models.IntegerField(null=True, blank=True)
    olevel_Certificate = models.FileField(null=True, blank=True, upload_to='olevel-certs/%Y/%m')

    # Alevel school info
    alevel_school = models.CharField(max_length=100, null=True, blank=True)
    aggregates = models.IntegerField(null=True, blank=True)
    alevel_Certificate = models.FileField(null=True, blank=True, upload_to='alevel-certs/%Y/%m')

    def __str__(self):
        return self.name

class Apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course')
    time_stamp = models.DateField(auto_now_add=True, null=True, blank=True)
    academic_year = models.CharField(max_length=122, help_text='eg. 2019')
    course_being_applied_for = models.CharField(max_length=122, help_text='BBA, PGDE, etc')
    campus = models.CharField(max_length=122, choices=CAMPUS)
    programme = models.CharField(max_length=122, choices=PROGRAMME)
    resident = models.BooleanField(default=False, help_text='All fresh stuents of the Main Campus MUST stay in the university halls')
    qualifies = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)+'-'+str(self.course_being_applied_for)