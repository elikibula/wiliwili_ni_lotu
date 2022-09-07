from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from datahub.models import DatahubLewenilotu, DatahubMatasiga, DatahubValenilotu, DatahubVeikaeyaco, DatahubVeitokani


@admin.register(DatahubLewenilotu)
class DatahubLewenilotuAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('yaca_ni_vavakoso', 'yaca_ni_vuvale','nona_valenilotu')
    search_fields = ("yaca_ni_vavakoso",)
    list_filter = ('nona_valenilotu','nona_matasiga', 'nona_veitokani')


@admin.register(DatahubMatasiga)
class DatahubMatasigaAdmin(admin.ModelAdmin):
    list_display = ('matasiga', 'liuliu_ni_matasiga', 'valenilotu')
    search_fields = ("matasiga",)
    list_filter = ('valenilotu',)

    pass


@admin.register(DatahubVeitokani)
class DatahubVeitokaniAdmin(admin.ModelAdmin):
    list_display = ('veitokani', 'liuliu_ni_veitokani', 'valenilotu')
    search_fields = ("veitokani",)
    list_filter = ('valenilotu',)
    pass


@admin.register(DatahubValenilotu)
class DatahubValenilotuAdmin(admin.ModelAdmin):
    list_display = ('valenilotu', 'yaca_ni_vakatawa')

    pass

@admin.register(DatahubVeikaeyaco)
class DatahubVeikaeyacoAdmin(admin.ModelAdmin):
    list_display = ('veika_e_yaco', 'valenilotu', 'created_at')
