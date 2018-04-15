from django.contrib import admin
from .models import (
    Idea,
    Comments,
    Like

)
# Register your models here.

admin.site.register(Idea)
admin.site.register(Comments)
admin.site.register(Like)