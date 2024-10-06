from django.contrib import admin
from django.utils.html import format_html

from .models import Shop, Complaint, Rating


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'number_of_complaints', 'ban', 'date_of_created', 'user', 'logo_img', "average_rating")
    search_fields = ('title', 'address', 'indicate_address', 'ban', 'number_of_complaints', 'link', 'date_of_created', 'user__username', "average_rating")
    list_filter = ('ban', 'indicate_address', 'number_of_complaints', 'date_of_created', "average_rating")
    readonly_fields = ('number_of_complaints', 'date_of_created', 'average_rating')

    def logo_img(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.logo.url) if obj.logo else None
    logo_img.short_description = 'Логотип'


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("shop", "get_user_username", "date_writing", "complaint_processed")
    search_fields = ("shop__title", "user__username", "date_writing")
    list_filter = ("date_writing", "shop__title", "user__username", "complaint_processed")
    readonly_fields = ("date_writing", )

    def get_user_username(self, obj):
        return obj.user.username
    get_user_username.short_description = 'Пользователь'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('shop', 'user', 'number_rating', 'date_writing', 'update_to')
    search_fields = ('shop', 'user', 'number_rating', 'date_writing', 'update_to')
    list_filter = ('shop', "user")
    readonly_fields = ("date_writing", "update_to")
