from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('MonAdmin.views',
    # Examples:
    # url(r'^$', 'projetfinal_python.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^admin/doc', include('django.contrib.admindocs.urls')),
   # url(r'^admin/', include('MonAdmin.urls')),

     # ...
   # url(r'^search-form/$', views.search_form),
   # url(r'^search/$', views.search),
    # ...

     # ...
   # url(r'^contact-form/$', views.contact_form),
    # ...

    url(r'^Ajouter/$', 'Ajout'),
    url(r'^Sauvegarder/$','Sauvegarde'),


)


urlpatterns += patterns ('weblog.views',

    (r'^tag/(\w+)/$', 'tag'),

)

