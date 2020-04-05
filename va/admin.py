from django.contrib import admin
from .models import *

class SubpartInline(admin.TabularInline):
	model = Subpart

class QuestionAdmin(admin.ModelAdmin):
	inlines = [
		SubpartInline,
	]
admin.site.register(Ques, QuestionAdmin)




class SubpartAnsInline(admin.TabularInline):
	model = SubpartAns

class AnsAdmin(admin.ModelAdmin):
	inlines = [
		SubpartAnsInline,
	]
admin.site.register(Ans, AnsAdmin)

class AnsInline(admin.TabularInline):
	model = Ans

class AnsBunchAdmin(admin.ModelAdmin):
	inlines = [
		AnsInline,
	]

# admin.site.register(Ans)
admin.site.register(AnsBunch, AnsBunchAdmin)