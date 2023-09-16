from django.contrib import admin
from .models import User
# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "name",
        "date_created",
        "date_updated",
        "is_active",
    )
admin.site.register(User, UserModelAdmin)


from .models import ActionUser,ResourceUploader
# Register your models here.


class Admin_ActionUser(admin.ModelAdmin):
    list_display =[
        "id","title","name","description","in_stock","price_asked","contact","location","date_created","date_updated"
    ]
admin.site.register(ActionUser,Admin_ActionUser)    

class Admin_ResourceUploader(admin.ModelAdmin):
    list_display = [
        "image","profile","banner"
    ]    

admin.site.register(ResourceUploader,Admin_ResourceUploader)    
