from django.contrib import admin

# Register your models here.
from .models import Dojo
from .models import Ninja

admin.site.register(Dojo)
admin.site.register(Ninja)

# from django.contrib import admin
# from myproject.myapp.models import Author

# admin.site.register(Author)
