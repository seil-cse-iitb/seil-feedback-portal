from django.contrib import admin

from synerg_lab.models import Question


class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    fields = ['id','question_text', 'answer_type']
    list_display = ('id', 'question_text','answer_type')
    list_display_links = ['question_text','answer_type']
    list_filter = ['id']
    actions_on_bottom = True
    readonly_fields = ('id',)


admin.site.register(Question,QuestionAdmin)

#
# # Register your models here.
#
# class QuestionDemoAdmin(admin.ModelAdmin):
#     date_hierarchy = 'created_on'
#     fields = ['id','text', 'answer_type']
#     list_display = ('id', 'text','answer_type')
#     list_display_links = ['text','answer_type']
#     list_filter = ['id']
#     actions_on_bottom = True
#     readonly_fields = ('id',)
#
#
# admin.site.register(QuestionDemo, QuestionDemoAdmin)
