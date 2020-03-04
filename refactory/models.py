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
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    primary_Contact = models.CharField(max_length=255, blank=True, null=True)
    secondary_Contact = models.CharField(max_length=255, blank=True, null=True)
    # user_photo= models.CharField(max_length=255,blank=True,null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = RefactoryUserManager()

    def __str__(self):
        return self.email


class Administrator(models.Model):
    # administrator_id = models.CharField("RFCT/ADM/001",primary_key=True)
    user = models.OneToOneField(RefactoryUser, on_delete=models.CASCADE)
    admin_id = models.AutoField(primary_key=True)
    admin_Photo = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.email

    ordering = ('email')


class Staff(models.Model):
    user = models.OneToOneField(RefactoryUser, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(
        Administrator, related_name='+', blank=True, on_delete=models.CASCADE, null=True)
    staff_id = models.AutoField(primary_key=True)
    staff_Photo = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.email


class Applicant(models.Model):
    user = models.OneToOneField(RefactoryUser, on_delete=models.CASCADE)
    applicant_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    applicant_Photo = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    dateofBirth = models.DateField(blank=True, null=True)
    town_Residential = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.email


class Role(models.Model):
    role_id = models.CharField(max_length=20, primary_key=True)
    role_name = models.CharField(max_length=20)
    role_description = models.TextField(max_length=20)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.role_name


class AdministratorRole(models.Model):

    administrator_id = models.ForeignKey(
        Administrator, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.role_id.role_name


class PartnerRole(models.Model):

    # partner_id=models.ForeignKey(Administrator,on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.role_name


class StaffRole(models.Model):

    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.role_id.role


class Accessibility(models.Model):

    accessibility_id = models.CharField(max_length=20, primary_key=True)
    accessibility_name = models.CharField(max_length=20)
    accessibility_description = models.TextField(max_length=255)
    accessibility_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.accessibility_name


class AdministratorAccessibility(models.Model):

    administrator_id = models.ForeignKey(
        Administrator, on_delete=models.CASCADE)
    accessibility_id = models.ForeignKey(
        Accessibility, on_delete=models.CASCADE)

    def __str__(self):
        return self.accessibility_id.accessibility_name


class PartnerAccessibility(models.Model):

    # partner_id=models.ForeignKey(Partner,on_delete=models.CASCADE)
    accessibility_id = models.ForeignKey(
        Accessibility, on_delete=models.CASCADE)

    def __str__(self):
        return self.accessibility_id.accessibility_name


class StaffAccessibility(models.Model):

    Staff_id = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    accessibility_id = models.ForeignKey(
        Accessibility, on_delete=models.CASCADE)

    def __str__(self):
        return self.accessibility_id.accessibility_name


class ApplicantAccessibility(models.Model):

    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    accessibility_id = models.ForeignKey(
        Accessibility, on_delete=models.CASCADE)

    def __str__(self):
        return self.accessibility_id.accessibility_name


class Cohort(models.Model):
    cohort_id = models.CharField(max_length=255, primary_key=True)
    cohort_name = models.CharField(max_length=255)
    registration_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    cohort_number = models.IntegerField()
    description = models.TextField(max_length=255)
    running = models.BooleanField(default=True)

    def __str__(self):
        return self.cohort_name


class Program(models.Model):
    program_id = models.CharField(max_length=255, primary_key=True)
    program_name = models.CharField(max_length=255)

    def __str__(self):
        return self.program_name


class Catalyst(models.Model):
    catalyst_id = models.CharField(max_length=255, primary_key=True)
    catalyst_name = models.CharField(max_length=255)
    registration_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    catalyst_number = models.IntegerField()
    description = models.TextField(max_length=255)
    running = models.BooleanField(default=True)

    def __str__(self):
        return self.catalyst_name


class Bootcamp(models.Model):
    bootcamp_id = models.CharField(max_length=255, primary_key=True)
    bootcamp_name = models.CharField(max_length=255)
    registration_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    bootcamp_number = models.IntegerField()
    description = models.TextField(max_length=255)
    running = models.BooleanField(default=True)

    def __str__(self):
        return self.name_name


class Contact(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    linkedin_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    facebook_link = models.URLField(max_length=255)

    def __str__(self):
        return self.applicant_id.email


class EducationBackground(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
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
                     )
    grade = models.CharField(
        max_length=255, default='1', choices=GRADE_CHOICES)
    From = models.DateTimeField(default=timezone.now)
    to = models.DateTimeField(default=timezone.now)
    Extra_activity = models.TextField(max_length=255)

    def __str__(self):
        return self.applicant_id.email


class SkillSet(models.Model):
    skill_id = models.CharField(max_length=255, primary_key=True)
    skill_name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.skill_name


class Skill(models.Model):

    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(SkillSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_id.skill_name


class Project(models.Model):

    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=20)
    association = models.CharField(max_length=255)
    project_url = models.URLField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.project_name


class Publication(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    publication_title = models.CharField(max_length=20)
    publisher = models.CharField(max_length=255)
    publication_url = models.URLField()
    publication_date = models.DateField(default=timezone.now)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.publication_title


class Certificate(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    certificate_title = models.CharField(max_length=20)
    License = models.CharField(max_length=255)
    certificate_url = models.URLField()
    certificate_date = models.DateField(default=timezone.now)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.certificate_title


class Course(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=20)
    course_id = models.CharField(max_length=255)
    association = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.course_name


class Honor(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    honor_title = models.CharField(max_length=255)
    association = models.CharField(max_length=255)
    Issuer = models.CharField(max_length=255)
    date_of_honor = models.DateField(default=timezone.now)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.applicant_id.email


class Referee(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telephone = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class AdvertisementChannelSet(models.Model):
    channel_id = models.CharField(max_length=30, primary_key=True)
    channel_name = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.channel_name


class AdvertisementChannel(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    channel_id = models.ForeignKey(
        AdvertisementChannelSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.channel_id.channel_name


class ApplicationVideo(models.Model):
    # application_id = models.ForeignKey(Applicant, on_delete=models.CASCADE )
    videolink = models.URLField(max_length=255)

    def __str__(self):
        return self.applicant_id.email


class Panelist(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    # batch_id=models.ForeignKey(Batch,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.batch_id.channel_name


class InterviewSchedule(models.Model):
    # selection_id=models.OneToOneField(InterviewSelection,on_delete=models.CASCADE)
    # batch_id=models.ForeignKey(Batch,on_delete=models.CASCADE)
    schedule_id = models.CharField(max_length=255, primary_key=True)
    creation_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.selection_id


class Interview(models.Model):
    # schedule_id	= models.OneToOneField(InterviewSchedule, on_delete=models.CASCADE)
    interview_id = models.CharField(max_length=255, primary_key=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)


class InterviewScore(models.Model):
    interview_id = models.ForeignKey(Interview, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    indicator_id = models.CharField(max_length=255, primary_key=True)
    score = models.IntegerField()
    comment = models.TextField(max_length=255)

    def __str__(self):
        return self.interview_id


class InterviewCategory(models.Model):
    category_id = models.CharField(max_length=254, primary_key=True)
    category_name = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return self.category_name


class CategoryStructure(models.Model):
    category_id = models.ForeignKey(
        InterviewCategory, on_delete=models.CASCADE)
    structure_id = models.CharField(primary_key=True, max_length=254)
    structure_name = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return self.structure_name


class StructureIndicator(models.Model):
    indicator_id = models.CharField(max_length=254, primary_key=True)
    structure_id = models.ForeignKey(
        CategoryStructure, on_delete=models.CASCADE)
    indicator_name = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return self.indicator_name


class Admission(models.Model):
    # application_id=models.ForeignKey(Application,on_delete=models.CASCADE)
    admission_id = models.CharField(max_length=255, primary_key=True)
    admission_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.application_id

    # @property
    # def token(self):
    #     """
    #     Allows us to get a user's token by calling `user.token` instead of
    #     `user.generate_jwt_token().

    #     The `@property` decorator above makes this possible. `token` is called
    #     a "dynamic property".
    #     """
    #     return self._generate_jwt_token()

    # def _generate_jwt_token(self):
    #     """
    #     Generates a JSON Web Token that stores this user's ID and has an expiry
    #     date set to 60 days into the future.
    #     """
    #     dt = datetime.now() + timedelta(days=60)

    #     token = jwt.encode({
    #         'id': self.pk,
    #         'exp': int(dt.strftime('%s'))
    #     }, settings.SECRET_KEY, algorithm='HS256')

    #     return token.decode('utf-8')
