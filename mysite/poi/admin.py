from django.contrib import admin
from poi.models import User
from poi.models import Photo
from poi.models import Friend
from poi.models import CategoryOfPoi
from poi.models import PointOfInterest

admin.site.register(User)
admin.site.register(CategoryOfPoi)
admin.site.register(Friend)
admin.site.register(Photo)
admin.site.register(PointOfInterest)

# Register your models here.
