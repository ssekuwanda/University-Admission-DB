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

class Profile(models.Model):
    # background tasks
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # student bio-data
    name = models.CharField(max_length=100,null=True, blank=True)
    slug = models.SlugField()
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    phone_number = models.IntegerField(blank=True, null=True)
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

    # Course being applied for
    first_course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    given_first = models.BooleanField(default=False)

    second_course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    given_second = models.BooleanField(default=False)

    third_course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    given_third = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# def user_post_save_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

# post_save.connect(user_post_save_receiver, sender=User)

