from django.contrib import admin
from .models import Challenge, TestCase
from django.utils.html import format_html
import json
from django.http import HttpResponse


# Inline admin to manage test cases directly within challenge page
class TestCaseInline(admin.TabularInline):
    model = TestCase
    extra = 1  # show 1 blank test case by default
    fields = ['input', 'expected_output', 'is_hidden']
    readonly_fields = ['preview_input', 'preview_output']

    def preview_input(self, obj):
        return format_html(f"<pre style='background:#f8f9fa; padding:5px'>{obj.input}</pre>")

    def preview_output(self, obj):
        return format_html(f"<pre style='background:#f8f9fa; padding:5px'>{obj.expected_output}</pre>")

    preview_input.short_description = "Input Preview"
    preview_output.short_description = "Expected Output Preview"



# Custom admin for Challenge
@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at']
    list_filter = ['created_by', 'created_at']
    search_fields = ['title', 'description']
    inlines = [TestCaseInline]  # Allow adding test cases inline
    readonly_fields = ['created_at']

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # New challenge
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    inlines = [TestCaseInline]
    actions = ['export_as_json']

    def export_as_json(self, request, queryset):
        data = []
        for challenge in queryset:
            item = {
                'title': challenge.title,
                'description': challenge.description,
                'time_limit': challenge.time_limit,
                'test_cases': list(challenge.test_cases.values('input', 'expected_output', 'is_hidden')),
            }
            data.append(item)

        response = HttpResponse(json.dumps(data, indent=2), content_type="application/json")
        response['Content-Disposition'] = 'attachment; filename=challenges.json'
        return response

    export_as_json.short_description = "Export Selected Challenges to JSON"

# Register TestCase separately too (if needed)
@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['challenge', 'is_hidden']
    list_filter = ['is_hidden']
    search_fields = ['challenge__title']


admin.site.site_header="Admin Panel for Silver Club"