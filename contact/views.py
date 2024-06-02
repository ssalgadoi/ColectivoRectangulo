from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, '¡El mensaje se ha enviado correctamente!')
            return redirect(reverse('contacto'))
        else:
            messages.error(request, '¡El mensaje no ha podido ser enviado. Por favor, intente más tarde.')
            return redirect(reverse('contacto'))
    
    return render(request, 'contact/contacto.html', {'form': contact_form})