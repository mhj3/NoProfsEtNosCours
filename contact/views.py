from django.core.mail import send_mail
from django.Http import HttpResponseRedirect
from django.shortcuts import render
from contact.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@exemple.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/conctact/thanks/')
    else:
        form =ContactForm(
            initial={'subject': 'I love your site!'}
        )
        return render (request, 'contact_form.html', {'form':form})

