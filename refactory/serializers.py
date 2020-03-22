from rest_framework import serializers

from .models import Cohort
from .models import Catalyst
from .models import Bootcamp
from .models import Contact
from .models import EducationBackground
from .models import SkillSet
from .models import ApplicationVideo
from .models import Interview,Project,Certificate,Referee,AdvertisementChannelSet,AdvertisementSubChannelSet,Application,CatalystApplication,BootcampApplication,Competence,Room,Batch,InterviewCategory,InterviewSet,InterviewSelection,InterviewSchedule,Interview,CategoryStructure,StructureIndicator,Panelist,Partner,Admission



class CohortSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cohort
        fields = ('cohort_id', 'name_name', 'registration_date', 'start_date',
                  'end_date', 'cohort_number', 'description', 'running')


class CatalystSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catalyst
        fields = ('catalyst_id', 'name_name', 'registration_date', 'start_date',
                  'end_date', 'catalyst_number', 'description', 'running')


class BootcampSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bootcamp
        fields = ('bootcamp_id', 'name_name', 'registration_date', 'start_date',
                  'end_date', 'bootcamp_number', 'description', 'running')


class ContactSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('applicant_id', 'linkedin_link',
                  'twitter_link', 'facebook_link')


class EducationBackgroundSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EducationBackground
        fields = ('applicant_id', 'school', 'degree', 'Field_of_study',
                  'grade', 'From', 'to', 'Extra_activity')


class SkillSetSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model=SkillSet
        fields = ('skill_id', 'skill_name', 'description')


class ApplicationVideoSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model=ApplicationVideo
        fields = ('application_id', 'videolink')


class InterviewSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interview
        fields = ('schedule_id', 'interview_id', 'start_date', 'end_date')

class CertificateSerializer (serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

class ProjectSerializer (serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class RefereeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = '__all__'

class AdvertisementChannelSetSerializer (serializers.ModelSerializer):
    class Meta:
        model = AdvertisementChannelSet
        fields = '__all__'

class AdvertisementSubChannelSetSerializer (serializers.ModelSerializer):
    class Meta:
        model = AdvertisementSubChannelSet
        fields = '__all__'

class ApplicationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class CatalystApplicationSerializer (serializers.ModelSerializer):
    class Meta:
        model = CatalystApplication
        fields = '__all__'

class BootcampApplicationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class CompetenceSerializer (serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'

class RoomSerializer (serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BatchSerializer (serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

class InterviewCategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = InterviewCategory
        fields = '__all__'

class InterviewSetSerializer (serializers.ModelSerializer):
    class Meta:
        model = InterviewSet
        fields = '__all__'

class InterviewSelectionSerializer (serializers.ModelSerializer):
    class Meta:
        model = InterviewSelection
        fields = '__all__'

class InterviewScheduleSerializer (serializers.ModelSerializer):
    class Meta:
        model = InterviewSchedule
        fields = '__all__'

class InterviewSerializer (serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'

class CategoryStructureSerializer (serializers.ModelSerializer):
    class Meta:
        model = CategoryStructure
        fields = '__all__'

class StructureIndicatorSerializer (serializers.ModelSerializer):
    class Meta:
        model = StructureIndicator
        fields = '__all__'

class PanelistSerializer (serializers.ModelSerializer):
    class Meta:
        model = Panelist
        fields = '__all__'

class PartnerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

class AdmissionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'
