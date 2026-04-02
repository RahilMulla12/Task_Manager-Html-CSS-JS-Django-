from django.contrib import admin
from .models import Query,QueryResponse, User

# Register your models here.
admin.site.register(QueryResponse)
admin.site.register(Query)
admin.site.register(User)

