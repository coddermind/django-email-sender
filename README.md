# Django Email Sender

A simple Django-based email sender that supports CSV/Excel file uploads to send bulk emails.

## Features
- Send emails with attachments
- Bulk email sending using CSV/Excel file
- Secure email authentication with app passwords

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/django-email-sender.git
   cd my_project
   ```
   
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
   
3. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Open http://127.0.0.1:8000/ in your browser.

2. Enable Two-Step Verification:

      - Go to your Google Account (https://myaccount.google.com/).

      - Click on Security in the left sidebar.

      - Under "How you sign in to Google", enable Two-Step Verification (if not already enabled).

3. Generate an App Password:

      - In the Security section, scroll down and find "App Passwords".

      - Click on "App Passwords" and sign in if prompted.

      - Select "Mail" as the app and "Other (Custom name)", then enter a name (e.g., "Django Email App").

      - Click Generate, and a unique App Password will be displayed.

4. Use the App Password in Your Project:

      - Copy the generated App Password.

      - Paste it into the App Password field in the project form when sending emails.

5. Enter email details and upload a CSV/Excel file if needed.

6. Click Send to dispatch emails.

## Contributing

Feel free to fork the repository and submit pull requests.

