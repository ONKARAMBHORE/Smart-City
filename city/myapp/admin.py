from django.contrib import admin
from django.utils.html import format_html
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
	list_display = ('title', 'user', 'category', 'status', 'created_at', 'thumbnail')
	search_fields = ('title', 'description', 'location', 'user__username', 'user__email')
	list_filter = ('status', 'category', 'created_at')
	readonly_fields = ('thumbnail',)

	def thumbnail(self, obj):
		if obj.image:
			return format_html('<img src="{}" style="max-height:60px;">', obj.image.url)
		return '-'

	thumbnail.short_description = 'Image'
