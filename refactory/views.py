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
from .models import ApplicationVideo,Interview,Project,Certificate

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

class CertificateView(viewsets.ModelViewSet):
    queryset=Certificate.objects.all()
    serializer_class= CertificateSerializer

class RefereeView(viewsets.ModelViewSet):
    queryset=Referee.objects.all()
    serializer_class= RefereeSerializer

class AdvertisementChannelSetView(viewsets.ModelViewSet):
    queryset=AdvertisementChannelSet.objects.all()
    serializer_class= AdvertisementChannelSetSerializer

class AdvertisementSubChannelSetView(viewsets.ModelViewSet):
    queryset=AdvertisementSubChannelSet.objects.all()
    serializer_class= AdvertisementSubChannelSetSerializer

class ApplicationView(viewsets.ModelViewSet):
    queryset=Application.objects.all()
    serializer_class= ApplicationSerializer

class CatalystApplicationView(viewsets.ModelViewSet):
    queryset=CatalystApplication.objects.all()
    serializer_class= CatalystApplicationSerializer

class BootcampApplicationView(viewsets.ModelViewSet):
    queryset=BootcampApplication.objects.all()
    serializer_class= BootcampApplicationSerializer

class CompetenceView(viewsets.ModelViewSet):
    queryset=Competence.objects.all()
    serializer_class= CompetenceSerializer

class RoomView(viewsets.ModelViewSet):
    queryset=Room.objects.all()
    serializer_class= RoomSerializer

class BatchView(viewsets.ModelViewSet):
    queryset=Batch.objects.all()
    serializer_class= BatchSerializer

class InterviewCategoryView(viewsets.ModelViewSet):
    queryset=InterviewCategory.objects.all()
    serializer_class= InterviewCategorySerializer

class InterviewSetView(viewsets.ModelViewSet):
    queryset=InterviewSet.objects.all()
    serializer_class= InterviewSetSerializer

class InterviewScheduleView(viewsets.ModelViewSet):
    queryset=InterviewSchedule.objects.all()
    serializer_class= InterviewScheduleSerializer

class InterviewView(viewsets.ModelViewSet):
    queryset=Interview.objects.all()
    serializer_class= InterviewSerializer

class CategoryStructureView(viewsets.ModelViewSet):
    queryset=CategoryStructure.objects.all()
    serializer_class= CategoryStructureSerializer

class StructureIndicatorView(viewsets.ModelViewSet):
    queryset=StructureIndicator.objects.all()
    serializer_class= StructureIndicatorSerializer

class PanelistView(viewsets.ModelViewSet):
    queryset=Panelist.objects.all()
    serializer_class= PanelistSerializer

class PartnerView(viewsets.ModelViewSet):
    queryset=Partner.objects.all()
    serializer_class= PartnerSerializer

class AdmissionView(viewsets.ModelViewSet):
    queryset=Admission.objects.all()
    serializer_class= AdmissionSerializer
