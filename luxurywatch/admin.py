from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Banner, Slider
from django.contrib.auth.models import Group, User


admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_preview', 'phone',  'edit_button', 'delete_button')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="80" />', obj.image.url)
        return ""
    image_preview.short_description = 'Rasm'
    def edit_button(self, obj):
        return format_html(
            '<a class="button" href="/admin/luxurywatch/product/{}/change/">Tahrirlash</a>', obj.id
        )
    edit_button.short_description = 'Tahrirlash'
    def delete_button(self, obj):
        return format_html(
            '<a class="button" style="color:white; background-color:red;" href="/admin/luxurywatch/product/{}/delete/">O‘chirish</a>',
            obj.id
        )
    delete_button.short_description = 'O‘chirish'
    class Media:
        css = {
            'all': ('admin/custom_admin.css',)  # CSS faylni ishlatish
        }


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_preview', 'edit_button', 'delete_button')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return ""
    image_preview.short_description = 'Rasm'
    def edit_button(self, obj):
        return format_html(
            '<a class="button" href="/admin/luxurywatch/banner/{}/change/">Tahrirlash</a>', obj.id
        )
    edit_button.short_description = 'Tahrirlash'
    def delete_button(self, obj):
        return format_html(
            '<a class="button" style="color:white; background-color:red;" href="/admin/luxurywatch/banner/{}/delete/">O‘chirish</a>',
            obj.id
        )
    delete_button.short_description = 'O‘chirish'
    class Media:
        css = {
            'all': ('admin/custom_admin.css',)  # CSS faylni ishlatish
        }

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_preview', 'price', 'edit_button', 'delete_button')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="80" />', obj.image.url)
        return ""
    image_preview.short_description = 'Rasm'
    def edit_button(self, obj):
        return format_html(
            '<a class="button" href="/admin/luxurywatch/slider/{}/change/">Tahrirlash</a>', obj.id
        )
    edit_button.short_description = 'Tahrirlash'
    def delete_button(self, obj):
        return format_html(
            '<a class="button" style="color:white; background-color:red;" href="/admin/luxurywatch/slider/{}/delete/">O‘chirish</a>',
            obj.id
        )
    delete_button.short_description = 'O‘chirish'
    class Media:
        css = {
            'all': ('admin/custom_admin.css',)  # CSS faylni ishlatish
        }
# admin.site.register(Slider)