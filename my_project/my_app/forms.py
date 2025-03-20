from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import pandas as pd
import io

class EmailForm(forms.Form):
    from_email = forms.EmailField(
        label="From Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        required=True
    )
    app_password = forms.CharField(
        label="App Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your app password'}),
        required=True
    )
    subject = forms.CharField(
        label="Subject",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email subject'}),
        max_length=100,
        required=True
    )
    body = forms.CharField(
        label="Body",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter email body', 'rows': 5}),
        required=True
    )
    attachment = forms.FileField(
        label="Attachment",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False
    )
    to_emails = forms.CharField(
        label="To Emails (comma-separated)",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter recipient emails, separated by commas', 'rows': 3}),
        required=False,
        help_text="Enter comma-separated emails or upload a CSV/Excel file with emails."
    )
    csv_file = forms.FileField(
        label="Upload CSV/Excel File",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False
    )

    def clean_to_emails(self):
        to_emails = self.cleaned_data.get('to_emails')
        csv_file = self.cleaned_data.get('csv_file')

        emails = []
        if csv_file:
            try:
                # Read the file into a pandas DataFrame
                if csv_file.name.endswith('.csv'):
                    df = pd.read_csv(csv_file)
                elif csv_file.name.endswith('.xls') or csv_file.name.endswith('.xlsx'):
                    df = pd.read_excel(csv_file)
                else:
                    raise forms.ValidationError("Unsupported file format. Please upload a CSV or Excel file.")

                # Flatten the DataFrame and extract emails
                emails = df.values.flatten().tolist()
                emails = [email.strip() for email in emails if pd.notna(email) and email.strip()]
            except Exception as e:
                raise forms.ValidationError(f"Error reading file: {str(e)}")
        else:
            # Split comma-separated emails
            emails = [email.strip() for email in to_emails.split(',') if email.strip()]

        # Validate emails
        for email in emails:
            try:
                validate_email(email)
            except ValidationError:
                raise forms.ValidationError(f"Invalid email: {email}")

        return emails
    
    def clean_csv_file(self):
        to_emails = self.cleaned_data.get('to_emails')
        csv_file = self.cleaned_data.get('csv_file')

        emails = []
        if csv_file:
            try:
                # Read the file into a pandas DataFrame
                if csv_file.name.endswith('.csv'):
                    df = pd.read_csv(csv_file)
                elif csv_file.name.endswith('.xls') or csv_file.name.endswith('.xlsx'):
                    df = pd.read_excel(csv_file)
                else:
                    raise forms.ValidationError("Unsupported file format. Please upload a CSV or Excel file.")

                # Flatten the DataFrame and extract emails
                emails = df.values.flatten().tolist()
                emails = [email.strip() for email in emails if pd.notna(email) and email.strip()]
            except Exception as e:
                raise forms.ValidationError(f"Error reading file: {str(e)}")
        else:
            # Split comma-separated emails
            emails = [email.strip() for email in to_emails.split(',') if email.strip()]

        # Validate emails
        for email in emails:
            try:
                validate_email(email)
            except ValidationError:
                raise forms.ValidationError(f"Invalid email: {email}")

        return emails