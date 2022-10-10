from django.contrib import admin

from app.internal.admin.admin_user import AdminUserAdmin

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"

from .models import Person
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	pass

from .models import City
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	pass

from .models import Place
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
	pass

from .models import For_Bot
@admin.register(For_Bot)
class For_BotAdmin(admin.ModelAdmin):
	pass