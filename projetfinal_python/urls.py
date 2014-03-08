from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

from MonAdmin.views import index, Ajout, modification, SauvModif, Suppression, SauvSupp

urlpatterns = patterns('',
    # Examples:
     url(r'^/$', 'projetfinal_python.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/doc', include('django.contrib.admindocs.urls')),
    url(r'^admin/', index),

    # ...
    url(r'^ajouter/$', Ajout),
    url(r'^modifier/(\d+)/',modification),
    url(r'^sauvegarder/$',SauvModif),
    url(r'^supprimer/(\d+)/',Suppression),
    url(r'^SauvegardeSuppression/$',SauvSupp),
    # ...

)




