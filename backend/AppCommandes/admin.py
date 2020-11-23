from django.contrib import admin
from .models import *

admin.site.register(Commande)
admin.site.register(HistoryAction)
admin.site.register(HistoryLogin)
admin.site.register(SupportApp)
