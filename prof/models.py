from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, blank=True, null=True)
    username = models.CharField(_('username'), max_length=30, unique=True)
    password = models.CharField(_('password'), max_length=128)
    date_joined = models.DateTimeField(default=timezone.now, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    phone_num = models.CharField(max_length=255, null=True,blank=True)
    photo = models.ImageField(null=True, blank=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.email}'

class PasswordResetToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'Reset Token for {self.user.username}'
    

class EmailVerificationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'Phone Verification Code for {self.user.username}'


class Universities(models.Model):
    name = models.CharField(max_length=355)
    logo = models.ImageField(null=True,blank=True)
    country = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    tuition = models.CharField(max_length=355,null=True,blank=True)
    percentage_of_income = models.CharField(max_length=5,null=True,blank=True)
    max = models.CharField(max_length=400,null=True,blank=True)
    full_grant = models.CharField(max_length=400,null=True,blank=True)
    deadline_1 = models.CharField(max_length=255,null=True, blank=True)
    deadline_2 = models.CharField(max_length=255,null=True, blank=True)
    TOEFL_IELTS = models.CharField(max_length=255,null=True,blank=True)
    SAT = models.CharField(max_length=255,null=True,blank=True)
    essay = models.CharField(max_length=255,null=True,blank=True)
    recommendation_letter = models.CharField(max_length=255,null=True,blank=True)
    cost_of_request = models.CharField(max_length=255,null=True,blank=True)
    link_form = models.CharField(max_length=1255,null=True,blank=True)
    website = models.CharField(max_length=400,null=True,blank=True)
    financial_aid_website = models.CharField(max_length=400,null=True,blank=True)
    rating_by_country = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 100)],null=True,blank=True)
    world_ranking = models.IntegerField(null=True,blank=True)
    professions = models.CharField(max_length=1500,null=True,blank=True)
    additional_comments = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
    

class Proffessions(models.Model):
    name = models.CharField(max_length=355)

    def __str__(self):
        return f'{self.name}'
    
class Internships(models.Model):
    title = models.CharField(max_length=1355)
    profession = models.ForeignKey('Proffessions', on_delete=models.SET_NULL, null=True, blank=True)
    organization_logo = models.ImageField(null=True,blank=True)
    organization = models.CharField(max_length=500,null=True,blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    paid_internship = models.BooleanField(null=True,blank=True)
    salary = models.CharField(max_length=255,null=True,blank=True)
    deadline = models.CharField(max_length=255,null=True,blank=True)
    link_to_apply = models.CharField(max_length=1155,null=True,blank=True)

    def __str__(self):
        return f'{self.title}'
    

class News(models.Model):
    title = models.CharField(max_length=1355)
    photo1 = models.ImageField(null=True,blank=True)
    photo2 = models.ImageField(null=True,blank=True)
    photo3 = models.ImageField(null=True,blank=True)
    description = models.TextField()
    date = models.DateTimeField()


    def __str__(self):
        return f'{self.title}'