from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import EmailForm
from django.contrib import messages

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            app_password = form.cleaned_data['app_password']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            attachment = request.FILES.get('attachment')
            to_emails = form.cleaned_data['to_emails']
            if len(to_emails)==0:
                to_emails=form.cleaned_data['csv_file']

            # Configure email backend
            settings.EMAIL_HOST_USER = from_email
            settings.EMAIL_HOST_PASSWORD = app_password

            # Create EmailMessage
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=from_email,
                to=to_emails,
            )

            # Attach file if provided
            if attachment:
                email.attach(attachment.name, attachment.read(), attachment.content_type)

            # Send email
            try:
                if len(to_emails)>0:
                    email.send()
                    messages.success(request, "Email sent successfully!")
                else:
                    messages.error(request,"To email list is empty.")
            except Exception as e:
                messages.error(request, f"Failed to send email: {str(e)}")

            return redirect('send_email')
    else:
        form = EmailForm()

    return render(request, 'email_app/send_email.html', {'form': form})