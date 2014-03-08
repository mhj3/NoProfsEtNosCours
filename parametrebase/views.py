from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from parametrebase.models import Cours

def hello(request):
    return HttpResponse("Hello World")

#BAD
def current_url_view_bad(request):
    return HttpResponse("Welcome to the page at %s" % request.path)


#GOOD
def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s" % request.path)

#BAD
def ua_diaplay_bad(request):
    ua = request.META['HTTP_USER_AGENT'] #Might raise KeyError
    return HttpResponse("Your browser is %s" % ua)

#GOOD (VERSION 1)
def ua_display_good1(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Your browser is %s" % ua)
#GOOD (VERSION 2)
def ua_display_good2(request):
    ua = request.META.get('HTTP_USER_AGENT','unknown')
    return HttpResponse ("Your browser is %s" % ua)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html =[]
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search_form(request):
    return render (request, 'Principal\Pages\search_form.html')

def contact_form(request):
    return render (request, 'Principal\Pages\contact_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term')
        elif len(q) >30:
            errors.append('Please enter at most 20 characters.')
        else:
            cour = Cours.object.filter(title__icontains=q)
            return render(request, 'search_results.html', {'cours': Cours, 'query':q})
    return render(request, 'Principal\Pages\search_form.html',{'errors':errors })
#BAD
def bad_search(request):
    #The following line will raise KeyError if 'q' hasn't been submitted!
    message = 'You serached for: %r' % request.GET['q']
    return HttpResponse(message)
