from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from soapapi.custom import RandomFileName
import uuid


class RefactoryUserManager(BaseUserManager):

    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class RefactoryUser(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(primary_key=True, max_length=254,default="u" + '{:%y%m%ds%we%H%M%Sr%f}'.format(datetime.today()))
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=20,blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=1, blank=True, null=True)
    # profile_photo= models.CharField(max_length=255,blank=True,null=True)
    primary_Contact = models.CharField(max_length=20, blank=True, null=True)
    secondary_Contact = models.CharField(max_length=20, blank=True, null=True)

    title_choices = [
        ("Mr.", "Mr."),
        ("Mrs.", "Mrs."),
        ("Miss.", "Miss."),
        ("Sir.", "Sir."),
        ("Dr.", "Dr."),
        ("Prof.", "Prof."),
        ("Eng.", "Eng."),
        ("Rev.", "Rev."),
        ("Hon.", "Hon."),
    ]
    title = models.CharField(max_length=6, choices=title_choices, blank=True)

    gender_choices = [
        ("M", "Male"),
        ("F", "Female")
    ]
    gender = models.CharField(max_length=6, choices=gender_choices)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.   id = "u" + '{:%y%m%ds%we%H%M%Sr%f}'.format(datetime.today())
        super(RefactoryUser, self).save(*args, **kwargs)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = RefactoryUserManager()

    def __str__(self):
        return self.email

    class Meta:
        # db_table = "User"
        ordering = ['date_joined']
    # End class Meta


class Administrator(models.Model):
    administrator_id = models.CharField(
        max_length=17, default="ADM-XX", primary_key=True)
    user = models.OneToOneField(RefactoryUser, on_delete=models.CASCADE)
    id = models.IntegerField(default=1)
    # profile_Photo = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):

        if self._state.adding:
            last_id = Administrator.objects.all().aggregate(
                largest=models.Max('id'))['largest']
            if last_id is None:
                self.id = 1
            else:
                self.id = last_id + 1
            self.administrator_id = "ADM-" + '{:02}'.format(self.id)
        super(Administrator, self).save(*args, **kwargs)

    def __str__(self):
        _str = self.administrator_id
        if(self.user.first_name or self.user.last_name):
            _str += " : "
            if(self.user.first_name):
                _str += self.user.first_name
            if(self.user.last_name):
                _str += " " + self.user.last_name
        if(self.user.email):
            _str += " (" + self.user.email + ")"
        return _str 

    class Meta:
        ordering = ['administrator_id']
    # End class Meta


class Partner(models.Model):
    administrator_id = models.ForeignKey(
        Administrator, on_delete=models.CASCADE)  # Needs Discussion
    partner_id = models.CharField(
        max_length=17, default="PTN-XXX", primary_key=True)
    id = models.IntegerField(default=1)
    partner_name = models.CharField(max_length=254, unique=True)
    partner_logo = models.FileField(upload_to=RandomFileName('images/partner/logos'),blank=True, null=True)
    featured_photo = models.FileField(upload_to=RandomFileName('images/partner/featured_photos'),blank=True, null=True)
    partner_cover_photo = models.FileField(upload_to=RandomFileName('images/partner/cover_photos'),blank=True, null=True)
    partner_description = models.TextField(max_length=500,blank=True, null=True )
    partnership_types = [
        ("Industrial", "Industrial"),
        ("Project", "Project")
    ]
    partnership_type = models.CharField(max_length=15, choices=partnership_types)

    def save(self, *args, **kwargs):

        if self._state.adding:
            last_id = Partner.objects.all().aggregate(
                largest=models.Max('id'))['largest']
            if last_id is None:
                self.id = 1
            else:
                self.id = last_id + 1
            self.partner_id = "PTN-" + '{:03}'.format(self.id)
        super(Partner, self).save(*args, **kwargs)

    def __str__(self):
        _str = self.partner_id
        if(self.partner_name):
            _str += " : "
            _str += self.partner_name
        return _str 

    class Meta:
        ordering = ['partner_id']
    # End class Meta


class Staff(models.Model):
    user = models.OneToOneField(RefactoryUser, on_delete=models.CASCADE)
    partner_id=models.ForeignKey(Partner,on_delete=models.CASCADE)
    id = models.ForeignKey(
        Administrator, related_name='+', blank=True, on_delete=models.CASCADE, null=True)
    staff_id = models.CharField(
        max_length=20, default="STF-XXX", primary_key=True)
    id = models.IntegerField(default=1)
    profile_Photo = models.FileField(upload_to=RandomFileName('images/user/staff/profile_photos'),blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id = Staff.objects.all().aggregate(
                largest=models.Max('id'))['largest']
            if last_id is None:
                self.id = 1
            else:
                self.id = last_id + 1
            self.staff_id = "STF-" + '{:03}'.format(self.id)
        super(Staff, self).save(*args, **kwargs)

    def __str__(self):
        _str = self.staff_id
        if(self.user.first_name or self.user.last_name):
            _str += " : "
            if(self.user.first_name):
                _str += self.user.first_name
            if(self.user.last_name):
                _str += " " + self.user.last_name
        if(self.user.email):
            _str += " (" + self.user.email + ")"
        return _str 

    class Meta:
        verbose_name_plural = "Staff"
        ordering = ['staff_id']        
    # End class Meta


class Applicant(models.Model):
    user = models.OneToOneField(RefactoryUser, on_delete=models.CASCADE)
    applicant_id = models.CharField(max_length=254, primary_key=True,default="REF-APT-" + '{:%y/%m/%d%H%M%S}'.format(datetime.today()))
    profile_Photo = models.FileField(upload_to=RandomFileName('images/user/applicant/profile_photos'),blank=True, null=True)
    dateofBirth = models.DateField(blank=True, null=True)
    town_Residential = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):

        if self._state.adding:
            self.applicant_id = "REF-APT-" + '{:%y/%m/%d%H%M%S}'.format(datetime.today()) #%w%f 
        super(Applicant, self).save(*args, **kwargs)

    def __str__(self):
        _str = self.applicant_id
        if(self.user.first_name or self.user.last_name):
            _str += " : "
            if(self.user.first_name):
                _str += self.user.first_name
            if(self.user.last_name):
                _str += " " + self.user.last_name
        if(self.user.email):
            _str += " (" + self.user.email + ")"
        return _str 

    class Meta:
        ordering = ['applicant_id']        
    # End class Meta


class Role(models.Model):
    id = models.IntegerField(default=1)
    role_id = models.CharField(
        max_length=10, default="RL-XXX", primary_key=True)
    role = models.CharField(max_length=254,unique=True)
    role_description = models.TextField(max_length=100,blank=True, null=True)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        _str = self.role_id
        if(self.role):
            _str += " : " + self.role
        return _str

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id = Role.objects.all().aggregate(
                largest=models.Max('id'))['largest']
            if last_id is None:
                self.id = 1
            else:
                self.id = last_id + 1
            self.role_id = "RL-" + '{:03}'.format(self.id)
        super(Role, self).save(*args, **kwargs)

    class Meta:
        ordering = ['role_id']        
    # End class Meta


class AdministratorRole(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:a%yd%mm%di%wn%Hr%Mo%Sl%fe}'.format(datetime.today()))
    administrator_id = models.ForeignKey(
        Administrator, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission_choices = [
        ("granted", "Granted"),
        ("denied", "Denied")
    ]
    permission = models.CharField(default='denied', max_length=8, choices=permission_choices)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:a%yd%mm%di%wn%Hr%Mo%Sl%fe}'.format(datetime.today())
            record_exists = AdministratorRole.objects.filter(administrator_id = self.administrator_id).filter(role_id = self.role_id)
            if len(record_exists) <= 0:
                super(AdministratorRole, self).save(*args, **kwargs)
            else:
                # raise ValidationError({
                #     'administrator_id': ValidationError(_('Missing title.'), code='required'),
                #     'role_id': ValidationError(_('Invalid date.'), code='invalid'),
                # })                
                 pass
                #  raise ValueError("This Assignment was already made.")
                #  raise Exception("This specified role is already assigned to the specified administrator")
        else:
            super(AdministratorRole, self).save(*args, **kwargs)

    def __str__(self):
        return self.administrator_id.__str__() + " ==> " + self.role_id.__str__()

    class Meta:
        ordering = ['administrator_id']
    # End class Meta


class PartnerRole(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:p%yt%mn%d-%w-%Hr%Mo%Sl%fe}'.format(datetime.today()))
    partner_id=models.ForeignKey(Partner, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission_choices = [
        ("granted", "Granted"),
        ("denied", "Denied")
    ]
    permission = models.CharField(default='denied', max_length=8, choices=permission_choices)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:p%yt%mn%d-%w-%Hr%Mo%Sl%fe}'.format(datetime.today())
            record_exists = PartnerRole.objects.filter(partner_id = self.partner_id).filter(role_id = self.role_id)
            if len(record_exists) <= 0:
                super(PartnerRole, self).save(*args, **kwargs)
            else:
                pass
        else:
            super(PartnerRole, self).save(*args, **kwargs)

    def __str__(self):
        return self.partner_id.__str__() + " ==> " + self.role_id.__str__()

    class Meta:
        ordering = ['partner_id']        
    # End class Meta


class StaffRole(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:s%yt%ma%df%wf%Hr%Mo%Sl%fe}'.format(datetime.today()))
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission_choices = [
        ("granted", "Granted"),
        ("denied", "Denied")
    ]
    permission = models.CharField(default='denied', max_length=8, choices=permission_choices)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:s%yt%ma%df%wf%Hr%Mo%Sl%fe}'.format(datetime.today())
            record_exists = StaffRole.objects.filter(staff_id = self.staff_id).filter(role_id = self.role_id)
            if len(record_exists) <= 0:
                super(StaffRole, self).save(*args, **kwargs)
            else:
                pass
        else:
            super(StaffRole, self).save(*args, **kwargs)

    def __str__(self):
        return self.staff_id.__str__() + " ==> " + self.role_id.__str__()

    class Meta:
        ordering = ['staff_id']        
    # End class Meta


class Accessibility(models.Model):
    id = models.IntegerField(default=1)
    accessibility_id = models.CharField(
        max_length=10, default="ACC-XXX", primary_key=True)
    accessibility_name = models.CharField(max_length=20,unique=True)
    accessibility_description = models.TextField(max_length=255,blank=True, null=True )
    accessibility_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.accessibility_name

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id = Accessibility.objects.all().aggregate(
                largest=models.Max('id'))['largest']
            if last_id is None:
                self.id = 1
            else:
                self.id = last_id + 1
            self.accessibility_id = "ACC-" + '{:03}'.format(self.id)
        super(Accessibility, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Accessibility"
        ordering = ['accessibility_id']        
    # End class Meta


class AdministratorAccessibility(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:a%yd%mm%di%wn%Ha%Mcc%Ses%fs}'.format(datetime.today()))
    administrator_id = models.ForeignKey(
        Administrator, on_delete=models.CASCADE)
    accessibility_id = models.ForeignKey(
        Accessibility,  on_delete=models.CASCADE)
    access_permission_choices = [
        ("granted", "Granted"),
        ("denied", "Denied")
    ]
    access_permission = models.CharField(default='denied', max_length=8, choices=access_permission_choices)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:a%yd%mm%di%wn%Ha%Mcc%Ses%fs}'.format(datetime.today())
            record_exists = AdministratorAccessibility.objects.filter(administrator_id = self.administrator_id).filter(accessibility_id = self.accessibility_id)
            if len(record_exists) <= 0:
                super(AdministratorAccessibility, self).save(*args, **kwargs)
            else:
                pass
        else:
            super(AdministratorAccessibility, self).save(*args, **kwargs)

    def __str__(self):
        return self.administrator_id.__str__() + " ==> " + self.accessibility_id.__str__()

    class Meta:
        verbose_name_plural = "Administrator Accessibility"
        ordering = ['administrator_id']
    # End class Meta


class PartnerAccessibility(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:p%yt%mn%d-%w-%Ha%Mcc%Ses%fs}'.format(datetime.today()))
    partner_id=models.ForeignKey(Partner,  on_delete=models.CASCADE)
    accessibility_id = models.ForeignKey(
        Accessibility,  on_delete=models.CASCADE)
    access_permission_choices = [
        ("granted", "Granted"),
        ("denied", "Denied")
    ]
    access_permission = models.CharField(default='denied', max_length=8, choices=access_permission_choices)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:p%yt%mn%d-%w-%Ha%Mcc%Ses%fs}'.format(datetime.today())
            record_exists = PartnerAccessibility.objects.filter(partner_id = self.partner_id).filter(accessibility_id = self.accessibility_id)
            if len(record_exists) <= 0:
                super(PartnerAccessibility, self).save(*args, **kwargs)
            else:
                pass
        else:
            super(PartnerAccessibility, self).save(*args, **kwargs)

    def __str__(self):
        return self.partner_id.__str__() + " ==> " + self.accessibility_id.__str__()

    class Meta:
        verbose_name_plural = "Partner Accessibility"
        ordering = ['partner_id']
    # End class Meta


class StaffAccessibility(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:s%yt%ma%df%wf%Ha%Mcc%Ses%fs}'.format(datetime.today()))
    staff_id = models.ForeignKey(Staff,  on_delete=models.CASCADE)
    accessibility_id = models.ForeignKey(
        Accessibility,  on_delete=models.CASCADE)
    access_permission_choices = [
        ("granted", "Granted"),
        ("denied", "Denied")
    ]
    access_permission = models.CharField(default='denied', max_length=8, choices=access_permission_choices)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:s%yt%ma%df%wf%Ha%Mcc%Ses%fs}'.format(datetime.today())
            record_exists = StaffAccessibility.objects.filter(staff_id = self.staff_id).filter(accessibility_id = self.accessibility_id)
            if len(record_exists) <= 0:
                super(StaffAccessibility, self).save(*args, **kwargs)
            else:
                pass
        else:
            super(StaffAccessibility, self).save(*args, **kwargs)

    def __str__(self):
        return self.staff_id.__str__() + " ==> " + self.accessibility_id.__str__()

    class Meta:
        verbose_name_plural = "Staff Accessibility"
        ordering = ['staff_id']
    # End class Meta


class ApplicantAccessibility(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:a%yp%mp%dn%wt%Ha%Mcc%Ses%fs}'.format(datetime.today()))
    applicant_id = models.ForeignKey(Applicant,  on_delete=models.CASCADE)
    accessibility_id = models.ForeignKey(
        Accessibility,  on_delete=models.CASCADE)
    access_permission_choices = [
        ("granted", "Granted"),
        ("denied", "Denied")
    ]
    access_permission = models.CharField(default='denied', max_length=8, choices=access_permission_choices)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:a%yp%mp%dn%wt%Ha%Mcc%Ses%fs}'.format(datetime.today())
            record_exists = ApplicantAccessibility.objects.filter(applicant_id = self.applicant_id).filter(accessibility_id = self.accessibility_id)
            if len(record_exists) <= 0:
                super(ApplicantAccessibility, self).save(*args, **kwargs)
            else:
                pass
        else:
            super(ApplicantAccessibility, self).save(*args, **kwargs)

    def __str__(self):
        return self.applicant_id.__str__() + " ==> " + self.accessibility_id.__str__()

    class Meta:
        verbose_name_plural = "Applicant Accessibility"
        ordering = ['applicant_id']
    # End class Meta


class Cohort(models.Model):
    cohort_number = models.IntegerField(unique=True)
    cohort_id = models.CharField(max_length=7, primary_key=True)
    cohort_name = models.CharField(max_length=255,unique=True)
    registration_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=255,blank=True, null=True)
    running = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.cohort_id = "CHT" + '{:04}'.format(self.cohort_number)
        super(Cohort, self).save(*args, **kwargs)

    def __str__(self):
        return self.cohort_id + " : " + self.cohort_name

    class Meta:
        ordering = ['cohort_id']
    # End class Meta


class Catalyst(models.Model):
    catalyst_number = models.IntegerField(unique=True)
    catalyst_id = models.CharField(max_length=7, primary_key=True)
    catalyst_name = models.CharField(max_length=255,unique=True)
    registration_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=255,blank=True, null=True)
    running = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.catalyst_id = "CT" + '{:04}'.format(self.catalyst_number)
        super(Catalyst, self).save(*args, **kwargs)

    def __str__(self):
        return self.catalyst_id + " : " + self.catalyst_name

    class Meta:
        ordering = ['catalyst_id']
    # End class Meta


class Bootcamp(models.Model):
    bootcamp_number = models.IntegerField(unique=True)
    bootcamp_id = models.CharField(max_length=255, primary_key=True)
    bootcamp_name = models.CharField(max_length=255,unique=True)
    registration_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=255,blank=True, null=True)
    running = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.bootcamp_id = "BT" + '{:04}'.format(self.bootcamp_number)
        super(Bootcamp, self).save(*args, **kwargs)

    def __str__(self):
        return self.bootcamp_id + " : " + self.bootcamp_name

    class Meta:
        ordering = ['bootcamp_id']
    # End class Meta


class Contact(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default="c" + '{:%y%mo%dn%wt%H%Ma%Sc%ft}'.format(datetime.today()))
    applicant_id = models.OneToOneField(Applicant, on_delete=models.CASCADE)
    linkedin_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255,blank=True, null=True)
    facebook_link = models.URLField(max_length=255,blank=True, null=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = "c" + '{:%y%mo%dn%wt%H%Ma%Sc%ft}'.format(datetime.today())
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return self.applicant_id.__str__()


class EducationBackground(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:e%y%md%du%wc%H%Ma%St%fe}'.format(datetime.today()))
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=50,unique=True)
    DEGREE_CHOICES = ((u'BSCS', u'Computer Science'),
                      (u'LLB', u'Lawyer'),
                      (u'BSIT', u'Information Technology'),
                      )
    degree = models.CharField(
        max_length=4, default='BSCS', choices=DEGREE_CHOICES)
    Field_of_study = models.CharField(max_length=255)
    GRADE_CHOICES = ((u'1', u'1'),
                     (u'2', u'2'),
                     (u'3', u'3'),
                     (u'4', u'4'),
                     )
    grade = models.CharField(
        max_length=255, default='1', choices=GRADE_CHOICES)
    From = models.DateTimeField(default=timezone.now)
    to = models.DateTimeField(default=timezone.now)
    # Extra_activity = models.TextField(max_length=255)
 
    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:e%y%md%du%wc%H%Ma%St%fe}'.format(datetime.today())
        super(EducationBackground, self).save(*args, **kwargs)

    def __str__(self):
        return self.applicant_id.__str__() + " : " + self.school_name

    class Meta:
        ordering = ['to']
    # End class Meta


class SkillSet(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=255,unique=True)
    # description = models.TextField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.skill_id + " : " + self.skill_name

    class Meta:
        ordering = ['skill_id']
    # End class Meta


class Skill(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:s%y%mk%d%wi%H%M%Sl%fl}'.format(datetime.today()))
    applicant_id = models.ForeignKey(Applicant,  on_delete=models.CASCADE)
    skill_id = models.ForeignKey(SkillSet,  on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:s%y%mk%d%wi%H%M%Sl%fl}'.format(datetime.today())
            record_exists = Skill.objects.filter(applicant_id = self.applicant_id).filter(skill_id = self.skill_id)
            if len(record_exists) <= 0:
                super(Skill, self).save(*args, **kwargs)
            else:
                pass
        else:
            super(Skill, self).save(*args, **kwargs)

    def __str__(self):
        return self.applicant_id.__str__() + " : " + self.skill_id.__str__()

    class Meta:
        ordering = ['applicant_id']
    # End class Meta


class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:p%y%mr%do%wj%H%Me%Sc%ft}'.format(datetime.today()))
    applicant_id = models.ForeignKey(Applicant,  on_delete=models.CASCADE)
    project_name = models.CharField(max_length=20)
    organisation = models.CharField(max_length=255)
    project_url = models.URLField(blank=True, null=True)
    start_date = models.DateField(default=timezone.now,blank=True, null=True)
    end_date = models.DateTimeField(default=timezone.now,blank=True, null=True)
    description = models.TextField(max_length=255,blank=True, null=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:p%y%mr%do%wj%H%Me%Sc%ft}'.format(datetime.today())
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.applicant_id.__str__() + " : " + self.project_name

    class Meta:
        ordering = ['applicant_id']
    # End class Meta


class Certificate(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default= '{:c%y%mer%dti%wfi%H%Mca%S%fte}'.format(datetime.today()))
    applicant_id = models.ForeignKey(Applicant,  on_delete=models.CASCADE)
    certificate_title = models.CharField(max_length=50,blank=True, null=True)
    License = models.CharField(max_length=255,blank=True, null=True)
    certificate_url = models.URLField(blank=True, null=True)
    certificate_date = models.DateField(default=timezone.now,blank=True, null=True)
    description = models.TextField(max_length=300,blank=True, null=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:c%y%mer%dti%wfi%H%Mca%S%fte}'.format(datetime.today())
        super(Certificate, self).save(*args, **kwargs)

    def __str__(self):
        return self.applicant_id.__str__() + " : " + self.certificate_title

    class Meta:
        ordering = ['applicant_id']
    # End class Meta


class Referee(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default= '{:r%y%me%df%we%H%Mr%Se%fe}'.format(datetime.today()))
    applicant_id = models.ForeignKey(Applicant,  on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=50)
    organisation = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=40)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:r%y%me%df%we%H%Mr%Se%fe}'.format(datetime.today())
        super(Referee, self).save(*args, **kwargs)

    def __str__(self):
        return self.applicant_id.__str__() + " : " + self.name

    class Meta:
        ordering = ['applicant_id']
    # End class Meta


class AdvertisementChannelSet(models.Model):
    channel_id = models.AutoField(primary_key=True)
    channel_name = models.CharField(max_length=20,unique=True)
    description = models.TextField(max_length=255,default="Channel set")

    def __str__(self):
        return self.channel_name

    class Meta:
        ordering = ['channel_id']
    # End class Meta


class AdvertisementSubChannelSet(models.Model):
    sub_channel_id = models.AutoField(primary_key=True)
    channel_id = models.ForeignKey(AdvertisementChannelSet,on_delete=models.CASCADE)
    sub_channel_name = models.CharField(max_length=30)

    def __str__(self):
        return self.channel_id.__str__() + " > " + self.sub_channel_name

    class Meta:
        ordering = ['sub_channel_name']
    # End class Meta


class ApplicantChannelSelection(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:c%y%mh%da%wn%H%Mn%Se%fl}'.format(datetime.today()))
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    sub_channel_id = models.ForeignKey(
        AdvertisementSubChannelSet, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:c%y%mh%da%wn%H%Mn%Se%fl}'.format(datetime.today())
            record_exists = ApplicantChannelSelection.objects.filter(applicant_id = self.applicant_id).filter(sub_channel_id = self.sub_channel_id)
            if len(record_exists) <= 0:
                super(ApplicantChannelSelection, self).save(*args, **kwargs)
            else:
                pass
        else:
            super(ApplicantChannelSelection, self).save(*args, **kwargs)

    def __str__(self):
        return self.applicant_id.__str__() + " > " + self.sub_channel_id.__str__()

    class Meta:
        ordering = ['applicant_id']
    # End class Meta

class Application(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    application_id = models.CharField(primary_key=True, max_length=254,default = "RFCT-PGM-APP-" + '{:a%yp%m%wp%d%Hli%M%Sca%fti%y%Ho%wn}'.format(datetime.today()))
    APP_STATUS_CHOICE = (
                     (u'incomplete', u'Incomplete Application'),
                     (u'completed', u'Completed'),
                     (u'blocked', u'Blocked'),
                     )
    application_status = models.CharField(
        max_length=10, default='incomplete', choices=APP_STATUS_CHOICE)
    RECRUITMENT_STATE_CHOICE = (
                     (u'pending', u'Pending Selection'),
                     (u'selected', u'Selected for Interview'),
                     (u'scheduled', u'Scheduled for Interview'),
                     (u'interviewed', u'Interviewed'),
                     (u'admitted', u'Admitted'),
                     (u'rejected', u'Rejected'),
                     )
    recruitment_state = models.CharField(
        max_length=10, default='pending', choices=APP_STATUS_CHOICE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        rtn_str = ""
        if self.applicant_id.user.first_name:
            rtn_str = rtn_str + " " + self.applicant_id.user.first_name
        if self.applicant_id.user.last_name:        
            rtn_str = rtn_str + " " + self.applicant_id.user.last_name
        rtn_str = rtn_str + " " + self.applicant_id.user.email
        return rtn_str

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.application_id = "RFCT-PGM-APP-" + '{:a%yp%m%wp%d%Hli%M%Sca%fti%y%Ho%wn}'.format(datetime.today())
        super(Application, self).save(*args, **kwargs)

    class Meta:
        ordering = ['application_id']
    # End class Meta


class CatalystApplication(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:T%y%mT%da%wp%H%Mp%Sl%fy}'.format(datetime.today()))
    catalyst_id = models.ForeignKey(Catalyst,on_delete=models.CASCADE)
    application_id = models.OneToOneField(Application,on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:C%y%mT%da%wp%H%Mp%Sl%fy}'.format(datetime.today())
            super(CatalystApplication, self).save(*args, **kwargs)

    def __str__(self):
        return self.catalyst_id.__str__() + " : " + self.application_id.__str__()

    class Meta:
        ordering = ['catalyst_id']
    # End class Meta

class BootcampApplication(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:B%y%mT%da%wp%H%Mp%Sl%fy}'.format(datetime.today()))
    bootcamp_id = models.ForeignKey(Bootcamp,on_delete=models.CASCADE)
    application_id = models.OneToOneField(Application,on_delete=models.CASCADE)
 
    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:B%y%mT%da%wp%H%Mp%Sl%fy}'.format(datetime.today())
            super(BootcampApplication, self).save(*args, **kwargs)

    def __str__(self):
        return self.bootcamp_id.__str__() + " : " + self.application_id.__str__()

    class Meta:
        ordering = ['bootcamp_id']
    # End class Meta


class Competence(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:c%y%mom%dpe%wte%H%Mn%Sc%fe}'.format(datetime.today()))
    application_id = models.OneToOneField(Application, on_delete=models.CASCADE)
    report_link = models.URLField()

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:c%y%mom%dpe%wte%H%Mn%Sc%fe}'.format(datetime.today())
        super(Competence, self).save(*args, **kwargs)

    def __str__(self):
        return self.application_id.__str__() + " : " + self.report_link

    class Meta:
        ordering = ['application_id']
    # End class Meta


class ApplicationVideo(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:a%y%mpp%dv%wi%H%Md%Se%fo}'.format(datetime.today()))
    application_id = models.OneToOneField(Application, on_delete=models.CASCADE)
    videolink = models.URLField()

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:a%y%mpp%dv%wi%H%Md%Se%fo}'.format(datetime.today())
        super(ApplicationVideo, self).save(*args, **kwargs)

    def __str__(self):
        return self.application_id.__str__() + " : " + self.videolink

    class Meta:
        ordering = ['application_id']
    # End class Meta


class Room(models.Model):
    id = models.IntegerField(default=1)
    room_id = models.CharField(
        max_length=10, default="RM-XXX", primary_key=True)
    room_name = models.CharField(unique=True,max_length=254)
    block_level = models.CharField(max_length=254)
    description = models.TextField(max_length=500,blank=True, null=True )

    def __str__(self):
        _str = self.room_id
        if(self.room_name):
            _str += " : " + self.room_name
        return _str

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id = Room.objects.all().aggregate(
                largest=models.Max('id'))['largest']
            if last_id is None:
                self.id = 1
            else:
                self.id = last_id + 1
            self.room_id = "RM-" + '{:03}'.format(self.id)
        super(Room, self).save(*args, **kwargs)

    class Meta:
        ordering = ['room_id']        
    # End class Meta


class Batch(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    batch_id = models.CharField(primary_key=True, max_length=254,default="BCH-" + '{:%f}'.format(datetime.today()))
    batch_name = models.CharField(unique=True,max_length=254)
    creation_date = models.DateTimeField(auto_now_add=True)
    date_of_last_update = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500,blank=True, null=True)

    def __str__(self):
        rtn_str = self.batch_id
        if self.batch_name:
            rtn_str = rtn_str + " : " + self.batch_name
        if self.room_id.room_name:
            rtn_str = rtn_str + " : Room (" + self.room_id.room_name + ")"
        return rtn_str

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.batch_id = "BCH-" + '{:%f}'.format(datetime.today())
        super(Batch, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Batches"        
        ordering = ['batch_id']
    # End class Meta


class Panelist(models.Model):
    id = models.CharField(primary_key=True, max_length=254,default='{:p%y%ma%dn%wa%H%Ml%Sis%ft}'.format(datetime.today()))
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    batch_id = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = '{:p%y%ma%dn%wa%H%Ml%Sis%ft}'.format(datetime.today())
            record_exists = Panelist.objects.filter(batch_id = self.batch_id).filter(staff_id = self.staff_id)
            if len(record_exists) <= 0:
                super(Panelist, self).save(*args, **kwargs)
            else:
                pass
        else:
            super(Panelist, self).save(*args, **kwargs)

    def __str__(self):
        return self.batch_id.__str__() + " > " + self.staff_id.__str__()

    class Meta:
        ordering = ['batch_id']
    # End class Meta


class InterviewSet(models.Model):
    set_id  = models.CharField(primary_key=True, max_length=254,default="INTV-SET-" + '{:%y%m%d-%w-%H%M%S-%f}'.format(datetime.today()))
    set_name = models.CharField(unique=True,max_length=254)
    CATEGORY_CHOICES = ((u'Catalyst', u'Catalyst Interviews'),
                      (u'Bootcamp', u'Bootcamp Interviews'),
                      )
    interview_category = models.CharField(
        max_length=20, default='Catalyst', choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=500,blank=True, null=True )
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    running = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.set_id = "INTV-SET-" + '{:%y%m%d-%w-%H%M%S-%f}'.format(datetime.today())
        super(InterviewSet, self).save(*args, **kwargs)


    def __str__(self):
        return self.category_id.__str__() + " > " + self.set_name + "(" + self.set_id + ")"

    class Meta:
        ordering = ['-start_date']
    # End class Meta


class InterviewSelection(models.Model):
    application_id = models.OneToOneField(Application, null=False, on_delete=models.CASCADE)
    set_id = models.ForeignKey(InterviewSet, on_delete=models.CASCADE)
    selection_id = models.CharField(primary_key=True, max_length=254,default="SLCT-" + '{:%y%m%d-%w-%H%M%S-%f}'.format(datetime.today()))
    selection_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.selection_id = "SLCT-" + '{:%y%m%d-%w-%H%M%S-%f}'.format(datetime.today())
        super(InterviewSelection, self).save(*args, **kwargs)

    def __str__(self):
        return self.set_id.set_name + " : " +self.application_id + "(" + self.selection_id + ")"

    class Meta:
        ordering = ['-selection_date']
    # End class Meta


class InterviewSchedule(models.Model):
    selection_id = models.OneToOneField(
        InterviewSelection, on_delete=models.CASCADE)
    batch_id = models.ForeignKey(Batch, blank=True, null=True, on_delete=models.CASCADE)
    schedule_id = models.CharField(primary_key=True, max_length=254,default="SCHDL-" + '{:%y%m%d-%w-%H%M%S-%f}'.format(datetime.today()))
    creation_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.schedule_id = "SCHDL-" + '{:%y%m%d-%w-%H%M%S-%f}'.format(datetime.today())
        super(InterviewSchedule, self).save(*args, **kwargs)

    def __str__(self):
        return self.selection_id.__str__() + " > " + self.schedule_id

    class Meta:
        ordering = ['-start_date']
    # End class Meta


class CategoryStructure(models.Model):
    CATEGORY_CHOICES = ((u'catalyst', u'Catalyst Interviews'),
                      (u'bootcamp', u'Bootcamp Interviews'),
                      )
    interview_category = models.CharField(
        max_length=20, default='Catalyst', choices=CATEGORY_CHOICES)
    structure_id = models.AutoField(primary_key=True)
    structure_name = models.CharField(max_length=254,unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.structure_name


class StructureIndicator(models.Model):
    indicator_id = models.AutoField(primary_key=True)
    structure_id = models.ForeignKey(
        CategoryStructure, on_delete=models.CASCADE)
    indicator_name = models.CharField(unique=True, null=False, max_length=254)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.indicator_name


class Interview(models.Model):
    schedule_id	= models.OneToOneField(InterviewSchedule, on_delete=models.CASCADE)
    interview_id = models.CharField(primary_key=True, max_length=254,default="INTV-" + '{:%y%m%d-%w-%H%M%S-%f}'.format(datetime.today()))
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.interview_id = "INTV-" + '{:%y%m%d-%w-%H%M%S-%f}'.format(datetime.today())
        super(Interview, self).save(*args, **kwargs)

    def __str__(self):
        return self.start_date + " : " + self.schedule_id.__str__() + " (" + self.interview_id + ")" 

    class Meta:
        ordering = ['-start_date']
    # End class Meta

class InterviewScore(models.Model):
    score_id = models.CharField(primary_key=True, max_length=254,default='{:%f%m%H%d%w%y%M%S}'.format(datetime.today()))
    interview_id = models.ForeignKey(Interview, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    indicator_id = models.ForeignKey(StructureIndicator, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField(max_length=255,blank=True, null=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.score_id = '{:%f%m%H%d%w%y%M%S}'.format(datetime.today())
            record_exists = InterviewScore.objects.filter(staff_id = self.staff_id).filter(interview_id = self.interview_id).filter(indicator_id = self.indicator_id)
            if len(record_exists) <= 0:
                super(InterviewScore, self).save(*args, **kwargs)
            else:
                pass
        else:
            super(InterviewScore, self).save(*args, **kwargs)

    def __str__(self):
        return self.interview_id


class Admission(models.Model):
    admission_id = models.CharField(primary_key=True, max_length=254,default="ADMSN-" + '{:%y%m%d-%w-%H%M%S-%f}'.format(datetime.today()))
    application_id = models.OneToOneField(Application, on_delete=models.CASCADE)
    admission_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.admission_id = "ADMSN-" + '{:%y%m%d-%w-%H%M%S-%f}'.format(datetime.today())
            super(Admission, self).save(*args, **kwargs)

    def __str__(self):
        return self.application_id.__str__()

    class Meta:
        ordering = ['-admission_date']
    # End class Meta
