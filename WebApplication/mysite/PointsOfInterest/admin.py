from django.contrib import admin
from PointsOfInterest.models import User
from PointsOfInterest.models import Friend
from PointsOfInterest.models import Photo


from PointsOfInterest.models import CategoryOfPoi
from PointsOfInterest.models import PointOfInterest

admin.site.register(User)
admin.site.register(Friend)
admin.site.register(CategoryOfPoi)
admin.site.register(Photo)
admin.site.register(PointOfInterest)
# Register your models here.
