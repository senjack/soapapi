from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets

from .serializers import CohortSerializer
from .models import Cohort
from .serializers import CatalystSerializer
from .models import Catalyst
from .serializers import BootcampSerializer
from .models  import Bootcamp
from .serializers import ContactSerializer
from .models import Contact
from .serializers import EducationBackgroundSerializer
from .models import EducationBackground
from .serializers import SkillSetSerializer
from .models import SkillSet
from .serializers import HonorSerializer
from .models import Honor
from .serializers import ApplicationVideoSerializer
from .models import ApplicationVideo
from .serializers import InterviewSerializer
from .serializers import Interview



#Create your views here.

class CohortViewSet (viewsets.ModelViewSet) :
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer

class CatalystViewSet (viewsets.ModelViewSet) :
    queryset = Catalyst.objects.all()
    serializer_class = CatalystSerializer

class BootcampViewSet (viewsets.ModelViewSet) :
    queryset = Bootcamp.objects.all()
    serializer_class = BootcampSerializer

class ContactViewSet (viewsets.ModelViewSet) :
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class EducationBackgroundViewSet (viewsets.ModelViewSet) :
    queryset = EducationBackground.objects.all()
    serializer_class = EducationBackgroundSerializer

class SkillSetViewSet (viewsets.ModelViewSet):
    queryset = SkillSet.objects.all()
    serializer_class = SkillSetSerializer

class HonorViewSet (viewsets.ModelViewSet):
    queryset = Honor.objects.all()
    serializer_class = HonorSerializer

class ApplicationVideoViewSet (viewsets.ModelViewSet):
    queryset = ApplicationVideo.objects.all()
    serializer_class = ApplicationVideoSerializer

class InterviewViewSet (viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

