# views.py
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.conf import settings
from .forms import SentForm
from .models import SentModel
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

# Function to send email with predefined content
def send_predefined_email(recipient_email):
    """
    Send a predefined HTML email to a recipient
    """
    # Default subject
    subject = "Your Predefined Subject Here"  # Change this to your desired subject
    
    try:
        # Render the HTML template with any context variables you need
        html_content = render_to_string('mail/fuckyou.html', {
            'recipient_email': recipient_email,
            # Add any other variables your template needs
        })
        
        # Create the email
        email = EmailMultiAlternatives(
            subject,
            "This is a text version of your email. Please enable HTML to view the full content.",
            settings.EMAIL_HOST_USER,
            [recipient_email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Main view
class SendEmailView(FormView):
    template_name = 'other/sent_mail_form.html'
    form_class = SentForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        # Save the form data to DB
        email_instance = form.save()
        
        # Get the email address
        recipient_email = email_instance.sent_address
        
        # Send the predefined email
        success = send_predefined_email(recipient_email)
        
        if success:
            messages.success(self.request, f"Email successfully sent to {recipient_email}!")
        else:
            messages.error(self.request, f"Failed to send email to {recipient_email}. Please check your settings.")
        
        return super().form_valid(form)