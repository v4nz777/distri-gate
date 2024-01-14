from django.contrib import admin
from users.models import User,Address,UsedToken


admin.site.register(User)
admin.site.register(Address)
admin.site.register(UsedToken)


