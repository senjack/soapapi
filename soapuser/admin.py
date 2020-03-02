from django.contrib import admin

from .models import Application
from .models import Competence
from .models import Interview_category
from .models import Category_structure
from .models import structure_indicator
from .models import Interview_set
from .models import Interview_selection
from. models import Room
from .models import Batch

# Register your models here.
admin.site.register(Application)
admin.site.register(Competence)
admin.site.register(Interview_category)
admin.site.register(structure_indicator)
admin.site.register(Interview_set)
admin.site.register(Interview_selection)
admin.site.register(Room)
admin.site.register(Batch)








