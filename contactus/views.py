from django.shortcuts import render

# Create your views here.
from contactus.forms import ContactusForm
from contactus.models import Contactus


def contactus_view(request):
    contact_form = ContactusForm(request.POST or None)
    if contact_form.is_valid():
        name = contact_form.cleaned_data['name']
        email = contact_form.cleaned_data['email']
        subject = contact_form.cleaned_data['subject']
        message = contact_form.cleaned_data['message']
        Contactus.objects.create(name=name, email=email, subject=subject, message=message)
        contact_form = ContactusForm()
    context={
        'contact': contact_form
    }
    return render(request, 'contactus/contactus_page.html', context)
