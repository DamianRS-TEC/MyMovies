from django.contrib import admin

from mymovies.models import Movie, Genre, Job, Person, MovieCredit, MovieReview 

class MovieCreditInline(admin.StackedInline):
    model = MovieCredit

class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('credits', )
    inlines = (MovieCreditInline)

class MovieCreditAdmin(admin.ModelAdmin):
    search_fields = ['']

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Job)
admin.site.register(Person)
admin.site.register(MovieCredit)
admin.site.register(MovieReview)
