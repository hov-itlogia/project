from django.contrib import admin

from books.models import Service

# nenc ara vor admin paneli "Service" modeli recordneri
# listum ereva @ndhamen@ 3 column u drancic menak 1
# lini clickable, te vor kdnes du mtaci
admin.site.register(Service)
