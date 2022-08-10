from django.contrib import admin
from .models import Booking, Post
from admin_totals.admin import ModelAdminTotals
from django.db.models import Sum

# admin.site.register(Booking)
admin.site.register(Post)
@admin.register(Booking)


class BookingAdmin(ModelAdminTotals):
    list_display = (
        "booking_number",
        "adult_meat",
        "adult_vegetarian",
        "children",
        )
    list_totals = [("adult_meat", Sum), ("adult_vegetarian", Sum), ("children", Sum)]
