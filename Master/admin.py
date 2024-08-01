from Master.models import twelfth_std_percentage_requirement , bachelor_requirement , masters_requirement , \
    tenth_std_percentage_requirement , \
    ielts_Exam , PTE_Exam , Toefl_Exam , Duolingo_Exam , Gre_Exam , Gmat_Exam , Available_Services , \
    Detail_Enquiry_Status , Enquiry_Source , Payment_Type , \
    Payment_Status , Payment_Mode
from django.contrib import admin
from import_export.admin import ImportExportMixin

# Register your models here.
from .models import country , course_levels , intake , current_education , documents_required , \
    enquiry_status , application_status , Course , university , assessment_status , Edu_Level , Work_Experience , \
    Rejection_Reason , AdmissionStatus , SubStatus , VisaStatus , VisaSubStatus, campus
from .resources import CourseResource , UniversityResource
from django.contrib import admin
from .models import university, tenth_std_percentage_requirement, twelfth_std_percentage_requirement, bachelor_requirement, masters_requirement, Toefl_Exam, ielts_Exam, PTE_Exam, Duolingo_Exam, Gre_Exam, Gmat_Exam
from .resources import UniversityResource
from django.contrib import admin
import csv
from django.http import HttpResponse
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from .models import university, country, course_levels
# Register your models here.


# class CourseListAdmin(ImportExportMixin , admin.ModelAdmin):
#     resource_class = CourseResource

#     list_display = (
#         'id' , 'university' , 'course_name' , 'course_levels' , 'display_intakes' ,
#         'tenth_std_percentage_requirement' , 'twelfth_std_percentage_requirement' ,
#         'bachelor_requirement' , 'masters_requirement' , 'Toefl_Exam' , 'ielts_Exam' ,
#         'PTE_Exam' , 'Duolingo_Exam' , 'Gre_Exam' , 'Gmat_Exam' , 'Remark' , 'Active'
#     )

#     list_filter = (
#         'university' , 'course_name' , 'course_levels' , 'intake' , 'documents_required' ,
#         'tenth_std_percentage_requirement' , 'twelfth_std_percentage_requirement' ,
#         'bachelor_requirement' , 'masters_requirement' , 'Toefl_Exam' , 'ielts_Exam' ,
#         'PTE_Exam' , 'Duolingo_Exam' , 'Gre_Exam' , 'Gmat_Exam' , 'Active'
#     )

#     fieldsets = (
#         ('Course Details' , {
#             'fields': ('university' ,  'Univ_Campus' ,'course_name' , 'course_levels' , 'intake' , 'documents_required' , 'Active')
#         }) ,
#         ('Course Requirements' , {
#             'fields': (
#                 'tenth_std_percentage_requirement' , 'twelfth_std_percentage_requirement' ,
#                 'bachelor_requirement' , 'masters_requirement' , 'Toefl_Exam' , 'ielts_Exam' ,
#                 'PTE_Exam' , 'Duolingo_Exam' , 'Gre_Exam' , 'Gmat_Exam'
#             )
#         }) ,
#         ('Notes' , {
#             'fields': ('Remark' ,)
#         }) ,
#     )

#     list_display_links = ('id' , 'university' ,)
#     list_per_page = 20
#     search_fields = ('course_name' , 'university__name' , 'country__country_name')

#     def display_intakes(self , obj):
#         """
#         Returns a comma-separated list of intake months and years from the ManyToManyField.
#         """
#         return ", ".join(
#             [f"{intake.intake_Name} {intake.intake_month} {intake.intake_year}" for intake in obj.intake.all()])

#     display_intakes.short_description = 'Intakes' 


class CourseResource(resources.ModelResource):
    country = fields.Field(
        column_name='country',
        attribute='country',
        widget=ForeignKeyWidget(country, 'country_name')
    )
    level = fields.Field(
        column_name='level',
        attribute='level',
        widget=ForeignKeyWidget(course_levels, 'level_name')
    )
    tenth_std_percentage_requirement = fields.Field(
        column_name='tenth_std_percentage_requirement',
        attribute='tenth_std_percentage_requirement',
        widget=ForeignKeyWidget(tenth_std_percentage_requirement, 'requirement')
    )
    twelfth_std_percentage_requirement = fields.Field(
        column_name='twelfth_std_percentage_requirement',
        attribute='twelfth_std_percentage_requirement',
        widget=ForeignKeyWidget(twelfth_std_percentage_requirement, 'requirement')
    )
    bachelor_requirement = fields.Field(
        column_name='bachelor_requirement',
        attribute='bachelor_requirement',
        widget=ForeignKeyWidget(bachelor_requirement, 'requirement')
    )
    masters_requirement = fields.Field(
        column_name='masters_requirement',
        attribute='masters_requirement',
        widget=ForeignKeyWidget(masters_requirement, 'requirement')
    )
    Toefl_Exam = fields.Field(
        column_name='Toefl_Exam',
        attribute='Toefl_Exam',
        widget=ForeignKeyWidget(Toefl_Exam, 'Overall')
    )
    ielts_Exam = fields.Field(
        column_name='ielts_Exam',
        attribute='ielts_Exam',
        widget=ForeignKeyWidget(ielts_Exam, 'Overall')
    )
    PTE_Exam = fields.Field(
        column_name='PTE_Exam',
        attribute='PTE_Exam',
        widget=ForeignKeyWidget(PTE_Exam, 'Overall')
    )
    Duolingo_Exam = fields.Field(
        column_name='Duolingo_Exam',
        attribute='Duolingo_Exam',
        widget=ForeignKeyWidget(Duolingo_Exam, 'Overall')
    )
    Gre_Exam = fields.Field(
        column_name='Gre_Exam',
        attribute='Gre_Exam',
        widget=ForeignKeyWidget(Gre_Exam, 'Overall')
    )
    Gmat_Exam = fields.Field(
        column_name='Gmat_Exam',
        attribute='Gmat_Exam',
        widget=ForeignKeyWidget(Gmat_Exam, 'Overall')
    )
    Univ_Campus = fields.Field(
        column_name='Univ_Campus',
        attribute='Univ_Campus',
        widget=ManyToManyWidget(campus, field='campus_name', separator=', ')
    )

    class Meta:
        model = Course
        fields = (
            'id', 'course_name', 'country', 'university', 'course_levels', 'intake', 'website_url', 'specialisation_tag',
            'documents_required', 'tenth_std_percentage_requirement', 'twelfth_std_percentage_requirement', 'bachelor_requirement',
            'masters_requirement', 'Toefl_Exam', 'ielts_Exam', 'PTE_Exam', 'Duolingo_Exam', 'Gre_Exam', 'Gmat_Exam', 
            'other_exam', 'Application_deadline', 'Application_fee', 'Application_fee_currency', 'Yearly_Tuition_fee', 
            'Backlogs_allowed', 'Remark', 'Active', 'Univ_Campus'
        )
        export_order = fields

# Admin class setup remains the same
class CourseAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CourseResource
    list_display = ('id', 'course_name', 'university', 'country', 'Active')
    list_filter = ('country', 'university', 'course_levels', 'Active')
    search_fields = ('course_name', 'university__univ_name', 'country__country_name')
    fieldsets = (
        ('Basic Information', {
            'fields': ('course_name', 'country', 'university', 'course_levels', 'website_url', 'specialisation_tag')
        }),
        ('Requirements', {
            'fields': (
                'tenth_std_percentage_requirement', 'twelfth_std_percentage_requirement', 
                'bachelor_requirement', 'masters_requirement', 'Toefl_Exam', 'ielts_Exam', 
                'PTE_Exam', 'Duolingo_Exam', 'Gre_Exam', 'Gmat_Exam', 'other_exam'
            )
        }),
        ('Application Details', {
            'fields': ('Application_deadline', 'Application_fee', 'Application_fee_currency', 'Yearly_Tuition_fee', 
                       'Backlogs_allowed')
        }),
        ('Additional Information', {
            'fields': ('Remark', 'Active', 'Univ_Campus', 'documents_required', 'intake')
        }),
    )
    list_display_links = ('id', 'course_name')
    list_per_page = 20

admin.site.register(Course, CourseAdmin)


# class UniversityAdmin(ImportExportMixin , admin.ModelAdmin):
#     resource_class = UniversityResource

#     list_display = (
#         'id' , 'univ_name' , 'country' , 'deadline' , 'moi_accepted' , 'Application_fee' , 'Active'
#     )

#     list_filter = (
#         'country' , 'levels' , 'moi_accepted' , 'Active'
#     )

#     search_fields = (
#         'univ_name' , 'country__country_name' , 'levels__levels' , 'univ_email'
#     )

#     fieldsets = (
#         ('Basic Information' , {
#             'fields': ('univ_name' , 'country' , 'levels' , 'univ_desc' , 'univ_logo' , 'newsletter')
#         }) ,
#         ('Application Details' , {
#             'fields': ('deadline' , 'moi_accepted' , 'Application_form' , 'Application_form_link' , 'Application_fee' ,
#                        'Admission_Requirements' , 'Backlogs_allowed')
#         }) ,
#         ('Contact Information' , {
#             'fields': ('univ_phone' , 'univ_email' , 'univ_website')
#         }) ,
#         ('Requirements' , {
#             'fields': (
#                 'tenth_std_percentage_requirement' , 'twelfth_std_percentage_requirement' ,
#                 'bachelor_requirement' , 'masters_requirement' , 'Toefl_Exam' , 'ielts_Exam' ,
#                 'PTE_Exam' , 'Duolingo_Exam' , 'Gre_Exam' , 'Gmat_Exam'
#             )
#         }) ,
#         ('Additional Information' , {
#             'fields': ('Remark' , 'Active' , 'assigned_users')
#         }) ,
#     )

#     list_display_links = ('id' , 'univ_name')
#     list_per_page = 20



class UniversityResource(resources.ModelResource):
    country = fields.Field(
        column_name='country',
        attribute='country',
        widget=ForeignKeyWidget(country, 'country_name')
    )
    level = fields.Field(
        column_name='level',
        attribute='level',
        widget=ForeignKeyWidget(course_levels, 'level_name')
    )
    tenth_std_percentage_requirement = fields.Field(
        column_name='tenth_std_percentage_requirement',
        attribute='tenth_std_percentage_requirement',
        widget=ForeignKeyWidget(tenth_std_percentage_requirement, 'requirement')
    )
    twelfth_std_percentage_requirement = fields.Field(
        column_name='twelfth_std_percentage_requirement',
        attribute='twelfth_std_percentage_requirement',
        widget=ForeignKeyWidget(twelfth_std_percentage_requirement, 'requirement')
    )
    bachelor_requirement = fields.Field(
        column_name='bachelor_requirement',
        attribute='bachelor_requirement',
        widget=ForeignKeyWidget(bachelor_requirement, 'requirement')
    )
    masters_requirement = fields.Field(
        column_name='masters_requirement',
        attribute='masters_requirement',
        widget=ForeignKeyWidget(masters_requirement, 'requirement')
    )
    Toefl_Exam = fields.Field(
        column_name='Toefl_Exam',
        attribute='Toefl_Exam',
        widget=ForeignKeyWidget(Toefl_Exam, 'Overall')
    )
    ielts_Exam = fields.Field(
        column_name='ielts_Exam',
        attribute='ielts_Exam',
        widget=ForeignKeyWidget(ielts_Exam, 'Overall')
    )
    PTE_Exam = fields.Field(
        column_name='PTE_Exam',
        attribute='PTE_Exam',
        widget=ForeignKeyWidget(PTE_Exam, 'Overall')
    )
    Duolingo_Exam = fields.Field(
        column_name='Duolingo_Exam',
        attribute='Duolingo_Exam',
        widget=ForeignKeyWidget(Duolingo_Exam, 'Overall')
    )
    Gre_Exam = fields.Field(
        column_name='Gre_Exam',
        attribute='Gre_Exam',
        widget=ForeignKeyWidget(Gre_Exam, 'Overall')
    )
    Gmat_Exam = fields.Field(
        column_name='Gmat_Exam',
        attribute='Gmat_Exam',
        widget=ForeignKeyWidget(Gmat_Exam, 'Overall')
    )
    # assigned_users = fields.Field(
    #     column_name='assigned_users',
    #     attribute='assigned_users',
    #     widget=ForeignKeyWidget(User, 'username')
    # )
 

    class Meta:
        model = university
        fields = (
            'id', 'univ_name', 'country', 'level', 'univ_desc', 'univ_logo', 'newsletter', 
            'deadline', 'moi_accepted', 'Application_form', 'Application_form_link', 
            'Application_fee', 'Admission_Requirements', 'Backlogs_allowed', 'univ_phone', 
            'univ_email', 'univ_website', 'tenth_std_percentage_requirement', 
            'twelfth_std_percentage_requirement', 'bachelor_requirement', 'masters_requirement', 
            'Toefl_Exam', 'ielts_Exam', 'PTE_Exam', 'Duolingo_Exam', 'Gre_Exam', 'Gmat_Exam', 
            'Remark', 'Active', 'assigned_users'
        )
        export_order = fields

class UniversityAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = UniversityResource
    list_display = ('id', 'univ_name', 'country', 'deadline', 'moi_accepted', 'Application_fee', 'Active')
    list_filter = ('country', 'level', 'moi_accepted', 'Active')
    search_fields = ('univ_name', 'country__country_name', 'levels__level_name', 'univ_email')
    fieldsets = (
        ('Basic Information', {
            'fields': ('univ_name', 'country', 'level', 'univ_desc', 'univ_logo', 'newsletter')
        }),
        ('Application Details', {
            'fields': ('deadline', 'moi_accepted', 'Application_form', 'Application_form_link', 'Application_fee', 
                       'Admission_Requirements', 'Backlogs_allowed')
        }),
        ('Contact Information', {
            'fields': ('univ_phone', 'univ_email', 'univ_website')
        }),
        ('Requirements', {
            'fields': (
                'tenth_std_percentage_requirement', 'twelfth_std_percentage_requirement', 
                'bachelor_requirement', 'masters_requirement', 'Toefl_Exam', 'ielts_Exam', 
                'PTE_Exam', 'Duolingo_Exam', 'Gre_Exam', 'Gmat_Exam'
            )
        }),
        ('Additional Information', {
            'fields': ('Remark', 'Active', 'assigned_users')
        }),
    )
    list_display_links = ('id', 'univ_name')
    list_per_page = 20

admin.site.register(university, UniversityAdmin)






class SubStatusInline(admin.TabularInline):
    model = SubStatus
    extra = 1


class AdmissionStatusAdmin(admin.ModelAdmin):
    inlines = [SubStatusInline]
    list_display = ('status_name' ,)


class VisaSubStatusInline(admin.TabularInline):
    model = VisaSubStatus
    extra = 1


class VisaStatusAdmin(admin.ModelAdmin):
    inlines = [VisaSubStatusInline]
    list_display = ('status_name' ,)


class CountryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None , {
            'fields': ('country_name' , 'currency')
        }) ,
        ('Admission Process' , {
            'fields': ('admission_process_notes' , 'admission_process_attachment')
        }) ,
        ('Visa Process' , {
            'fields': ('visa_process_notes' , 'visa_process_attachment')
        }) ,
        ('Attachments' , {
            'fields': ('news_letter' , 'video_attachment' , 'country_brochure')
        }) ,
        ('Statuses' , {
            'fields': ('admission_status' , 'visa_status')
        }) ,
    )

    list_display = ('country_name' , 'currency')
    search_fields = ('country_name' , 'currency')
    list_filter = ('admission_status' , 'visa_status')
    filter_horizontal = ('admission_status' , 'visa_status')


admin.site.register(course_levels)
admin.site.register(intake)
admin.site.register(current_education)
admin.site.register(documents_required)
admin.site.register(enquiry_status)
admin.site.register(application_status)
# admin.site.register(Course , CourseListAdmin)
# admin.site.register(university , UniversityAdmin)
admin.site.register(assessment_status)
admin.site.register(Edu_Level)
admin.site.register(Work_Experience)
admin.site.register(ielts_Exam)
admin.site.register(PTE_Exam)
admin.site.register(Toefl_Exam)
admin.site.register(Duolingo_Exam)
admin.site.register(Gre_Exam)
admin.site.register(Gmat_Exam)
admin.site.register(Rejection_Reason)
admin.site.register(tenth_std_percentage_requirement)
admin.site.register(twelfth_std_percentage_requirement)
admin.site.register(bachelor_requirement)
admin.site.register(masters_requirement)
admin.site.register(Available_Services)
admin.site.register(Detail_Enquiry_Status)
admin.site.register(Enquiry_Source)
admin.site.register(Payment_Type)
admin.site.register(Payment_Status)
admin.site.register(Payment_Mode)
admin.site.register(AdmissionStatus , AdmissionStatusAdmin)
admin.site.register(SubStatus)
admin.site.register(VisaStatus , VisaStatusAdmin)
admin.site.register(VisaSubStatus)
admin.site.register(country , CountryAdmin)
admin.site.register(campus)

# Register your models here.
