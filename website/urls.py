from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
                       url(r'^projects/(.+)/$', 'personal.views.project_details'),
                       url(r'^projects/$', 'personal.views.projects'),

                       url(r'^publications/(.+)/$', 'personal.views.publication_details'),
                       url(r'^publications/$', 'personal.views.publications'),

                       url(r'^experiments/(.+)/$', 'personal.views.experiment_details'),
                       url(r'^experiments/$', 'personal.views.experiments'),

                       url(r'^compositions/(.+)/$', 'personal.views.composition_details'),
                       url(r'^compositions/$', 'personal.views.compositions'),
                       
                       url(r'^performances/(.+)/$', 'personal.views.performance_details'),
                       url(r'^performances/$', 'personal.views.performances'),

                       url(r'^installations/(.+)/$', 'personal.views.installation_details'),
                       url(r'^installations/$', 'personal.views.installations'),
                       
                       
                       url(r'^music/$', 'personal.views.music'),

                       
                       url(r'^classes/$', 'personal.views.classes'),
                       url(r'^about/$', 'personal.views.about'),
                       url(r'^resume/$', 'personal.views.resume'),
                       url(r'^contact/$', 'personal.views.contact'),
                       url(r'^links/$', 'personal.views.links'),
                       
                       url(r'^$', 'personal.views.home'),
    

)