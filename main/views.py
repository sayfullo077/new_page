from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

def home_view(request):
    context = {
        'title': 'Sayfulloh',
        'message_sent': False,  # Initial value
    }

    if request.method == 'POST':
        name = request.POST.get("name", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()
        from_email = request.POST.get("from_email", "").strip()

        if name and subject and message and from_email:
            try:
                send_mail(
                    subject,
                    f"Name: {name}\n\nMessage: {message}\n\nFrom: {from_email}",
                    from_email,
                    [from_email, "sayfulloh.dev@gmail.com"],
                )
                context['message_sent'] = True
                messages.success(request, "Your message has been sent successfully!")  # Use Django's messages framework
                return HttpResponseRedirect(reverse('main:home'))
            except Exception as e:
                messages.error(request, f"An error occurred while sending the email. Please try again later.{e}")
        else:
            messages.error(request, "Please ensure all fields are filled correctly.")

    return render(request, 'main/index.html', context)
