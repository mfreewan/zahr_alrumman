from django.contrib import admin

# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from django.contrib import admin
from .models import (
    InKindDonation,
    CashDonation,
    News,
    Volunteer,
    Events,
    poster,
    Achivment,
    ExistingProjects,
    About,
    number,
    User,
)


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "phoneNumber",
    ]
    list_filter = ["is_staff", "is_active"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "NationalNumber",
                    "phoneNumber",
                    "MiddleName",
                    "RegisterDate",
                    "FamilyNumbers",
                    "NAF",
                )
            },
        ),
        ("Permissions", {"fields": ("is_active", "is_staff")}),
        # ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "NationalNumber",
                    "phoneNumber",
                    "MiddleName",
                    "RegisterDate",
                    "FamilyNumbers",
                    "NAF",
                ),
            },
        ),
    )
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)


admin.site.register(User, CustomUserAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ("Title", "Image", "Details")
    list_filter = ["date"]


# Register the Admin classes for Boo,kInstance using the decorator


class ExistingProjectsAdmin(admin.ModelAdmin):
    list_display = ("Image", "Name", "Details", "start_date")
    list_filter = ["start_date"]
    fields = ("Name", "start_date", "Details", "Image")


class VolunteersAdmin(admin.ModelAdmin):
    list_display = ("field_of_volunteers", "RegisterDate")
    fields = ("field_of_volunteers", "RegisterDate")


class InKindDonationAdmin(admin.ModelAdmin):
    pass


class CashDonationAdmin(admin.ModelAdmin):
    pass


class EventsAdmin(admin.ModelAdmin):
    pass


class posterAdmin(admin.ModelAdmin):
    pass


class AboutAdmin(admin.ModelAdmin):
    pass


class NumberOfAchivmentAdmin(admin.ModelAdmin):
    pass


class numberadmin(admin.ModelAdmin):
    pass


class VolunteerAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Volunteer, VolunteersAdmin)
admin.site.register(ExistingProjects, ExistingProjectsAdmin)
admin.site.register(InKindDonation, InKindDonationAdmin)
admin.site.register(CashDonation, CashDonationAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(poster, posterAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Achivment, NumberOfAchivmentAdmin)
admin.site.register(number, numberadmin)
admin.site.register(Volunteer, VolunteerAdmin)


# class CustomUserAdmin(UserAdmin):
#     list_display = (
#         "username",
#         "email",
#         "first_name",
#         "last_name",
#         "is_staff",
#         "is_teacher",
#         "is_naf",
#         "mailing_address",
#         "phoneNumber",
#     )

#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         ("Personal info", {"fields": ("first_name", "last_name", "email")}),
#         (
#             "Permissions",
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 )
#             },
#         ),
#         ("Important dates", {"fields": ("last_login", "date_joined")}),
#         (
#             "Additional info",
#             {
#                 "fields": (
#                     "is_naf",
#                     "is_teacher",
#                     "mailing_address",
#                     "phoneNumber",
#                     "RegisterDate",
#                     "FamilyNumbers",
#                     "NationalNumber",
#                     "nationality",
#                 )
#             },
#         ),
#     )

#     add_fieldsets = (
#         (None, {"fields": ("username", "password1", "password2")}),
#         ("Personal info", {"fields": ("first_name", "last_name", "email")}),
#         (
#             "Permissions",
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 )
#             },
#         ),
#         ("Important dates", {"fields": ("last_login", "date_joined")}),
#         (
#             "Additional info",
#             {
#                 "fields": (
#                     "is_naf",
#                     "is_teacher",
#                     "mailing_address",
#                     "phoneNumber",
#                     "RegisterDate",
#                     "FamilyNumbers",
#                     "NationalNumber",
#                     "nationality",
#                 )
#             },
#         ),
#     )


# admin.site.register(CustomUser, CustomUserAdmin)
