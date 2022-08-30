from django.contrib import admin

# Register your models here.

from .models import m_usernames,m_userdetails

admin.site.register(m_usernames)

admin.site.register(m_userdetails)
