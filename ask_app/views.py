from django.shortcuts import render

# Create your views here.
def footer(request):
    return render(request, 'footer.html') 

def header(request):
    return render(request, 'header.html')

def contact(request):
    return render(request, 'contactus.html')


def skill(request):
    return render(request, 'skills.html')


def gallery(request):
    return render(request, 'gallery.html')

def project(request):
    return render(request, 'projects.html')

def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html') 

def intro(request):
    return render(request, 'intro.html')

def privacy(request):
    return render(request, 'privacy.html')




from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

def contactus(request):
    print("Contact Us View Called")
    if request.method == "POST":
        print("Processing Contact Form Submission")
        name = request.POST.get("fullname", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        subject = request.POST.get("subject", "").strip() or "New Contact Inquiry"
        message = request.POST.get("message", "").strip()

        if name and email and message:
            # Prepare email content
            full_message = (
                f"New contact form submission:\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Subject: {subject}\n"
                f"Message:\n{message}"
            )
 
            # Send to platform admin (change email in settings if needed)
            admin_email = getattr(settings, "PLATFORM_EMAIL", settings.DEFAULT_FROM_EMAIL)

            send_mail(
                subject=f"Contact Form - {subject}",
                message=full_message,
                from_email=settings.PLATFORM_EMAIL,
                recipient_list=[admin_email],
                fail_silently=False,
            )

            return render(request, "contactus.html", {
                "success": "Thank you! Your message has been sent.",
            })
        else:
            return render(request, "contactus.html", {
                "error": "All fields are required. Please fill out the form completely."
            })

    return render(request, "contactus.html")

def update(request):
    return render(request, 'update.html')