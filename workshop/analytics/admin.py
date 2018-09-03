from django.contrib import admin
from .models import Workshop, Track, Sponsor, Facilitator, Participant
# from django.apps import apps
# from django.contrib.auth.models import User
# from django.contrib.admin import AdminSite
from django.urls import path
import csv
import io
import re
from django.forms import forms
from django.shortcuts import redirect, render


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'start_date', 'end_date',
                    'get_facilitators')
    list_filter = ('venue', 'host', 'sponsors', 'facilitators',
                   'participants')
    filter_horizontal = ('facilitators', 'participants', 'sponsors')
    search_fields = ('name', 'venue')

    def get_facilitators(self, obj):
        return " \n ".join([str(f) for f in obj.facilitators.all()])

    get_facilitators.short_description = "Facilitators"


# TODO find out how to show workshops for facilitator|sponsor|participant


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'email',
                    'institution', 'country')  # 'workshop_attended')
    list_filter = ('gender', 'institution')  # 'workshop_attended',
    search_fields = ('first_name', 'last_name', 'country')

    # save_as = True
    # save_on_top = True
    # change_list_template = 'change_list_graph.html'

    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(
    #         request,
    #         extra_context=extra_context,
    #     )
    #     response.context_data['page'] = "attendee"
    #     return response
    change_list_template = "analytics/analytics_change_list.html"

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string, delimiter=',')
            # reader = csv.reader(open(csv_file), delimiter=',')
            reader_list = list(reader)

            for i in range(1, len(reader_list)):
                row = reader_list[i]

                post = Participant()

                both_names = re.split(r' ', row[0], maxsplit=1)
                post.first_name = both_names[0]
                post.last_name = both_names[1]

                post.institution = row[2]
                post.email = row[1]
                post.country = row[4]
                post.gender = row[3]
                post.save()

            self.message_user(request,
                              "Your csv file has been imported successfully")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('import-csv/', self.import_csv), ]
        return my_urls + urls


class FacilitatorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'email',
                    'institution', 'country')  # 'workshop_taught')
    list_filter = ('institution', 'gender')  # 'workshop_taught',
    search_fields = ('first_name', 'last_name', 'country')

    # save_as = True
    # save_on_top = True
    # change_list_template = 'change_list_graph.html'
    #
    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(
    #         request,
    #         extra_context=extra_context,
    #     )
    #     response.context_data['page'] = "instructor"
    #     return response

    change_list_template = "analytics/analytics_change_list.html"

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string, delimiter=',')
            # reader = csv.reader(open(csv_file), delimiter=',')

            reader_list = list(reader)

            for i in range(1, len(reader_list)):
                row = reader_list[i]

                post = Facilitator()

                both_names = re.split(r' ', row[0], maxsplit=1)
                post.first_name = both_names[0]
                post.last_name = both_names[1]

                post.institution = row[2]
                post.email = row[1]
                post.country = row[4]
                post.gender = row[3]
                post.save()

            self.message_user(request,
                              "Your csv file has been imported successfully")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('import-csv/', self.import_csv), ]
        return my_urls + urls


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_display = ('name', 'workshop_sponsored')
    # list_filter = ('name', 'workshop_sponsored')
    #
    # change_list_template = 'change_list_graph.html'
    #
    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(
    #         request,
    #         extra_context=extra_context,
    #     )
    #     response.context_data['page'] = "sponsor"
    #     return response


class TrackAdmin(admin.ModelAdmin):
    list_display = ('name',)


renu_header_str = "RENU Workshops"

admin.site.site_header = renu_header_str
admin.site.site_title = renu_header_str
admin.site.index_title = renu_header_str
admin.site.site_url = "https://workshops.renu.ac.ug"

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Facilitator, FacilitatorAdmin)
# admin.site.register(Person, PersonAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Participant, ParticipantAdmin)
