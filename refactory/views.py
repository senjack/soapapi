from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets

from .serializers import *
from .models import Cohort
from .models import Catalyst
from .models import Bootcamp
from .models import Contact
from .models import EducationBackground
from .models import SkillSet
from .models import ApplicationVideo,Interview,Project

# Create your views here.

class CohortViewSet (viewsets.ModelViewSet):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer


class CatalystViewSet (viewsets.ModelViewSet):
    queryset = Catalyst.objects.all()
    serializer_class = CatalystSerializer


class BootcampViewSet (viewsets.ModelViewSet):
    queryset = Bootcamp.objects.all()
    serializer_class = BootcampSerializer


class ContactViewSet (viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class EducationBackgroundViewSet (viewsets.ModelViewSet):
    queryset = EducationBackground.objects.all()
    serializer_class = EducationBackgroundSerializer


class SkillSetViewSet (viewsets.ModelViewSet):
    queryset = SkillSet.objects.all()
    serializer_class = SkillSetSerializer


class ApplicationVideoViewSet (viewsets.ModelViewSet):
    queryset = ApplicationVideo.objects.all()
    serializer_class = ApplicationVideoSerializer


class InterviewViewSet (viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

class ProjectView(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class= ProjectSerializer