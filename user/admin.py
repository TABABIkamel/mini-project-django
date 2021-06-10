from django.contrib import admin

# Register your models here.
from user.models import Formation
class FormationAdmin(admin.ModelAdmin):
    list_display =('titer','categ','etat')
    search_fields = ['titer']
    list_filter = ('titer', 'categ')
    fieldsets = (
        ('A propos', {
            'fields': (('titer','logo', 'categ',))
        }),
        ('Etat', {'fields': ('etat',)}),

    )

admin.site.register(Formation,FormationAdmin)