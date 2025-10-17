import re
from datetime import datetime
from jinja2 import Template
import os

TEMPLATE_PATH = "templates/base_email.txt"

def clean_text(text):
    """Clean and normalize user input."""
    text = re.sub(r'\s+', ' ', text.strip())
    return text[0].upper() + text[1:] if text else ""

def load_template():
    """Load the Jinja2 email template."""
    if not os.path.exists(TEMPLATE_PATH):
        os.makedirs("templates", exist_ok=True)
        with open(TEMPLATE_PATH, "w") as f:
            f.write(
"""Subject: {{ subject }}

Dear {{ recipient_name }},

{{ body }}

Best regards,
{{ sender_name }}
{{ sender_role }}
{{ company_name }}
{{ current_date }}
"""
            )
    with open(TEMPLATE_PATH, "r") as f:
        return Template(f.read())

def format_email():
    """Main function to format an email using user input."""
    print("📧 Auto Email Formatter\n")

    recipient_name = input("Enter recipient name: ").title()
    subject = input("Enter subject: ")
    body = input("Enter main message or bullet points: ")
    sender_name = input("Your name: ").title()
    sender_role = input("Your role/designation: ").title()
    company_name = input("Your company name: ").title()

    # Clean inputs
    subject = clean_text(subject)
    body = clean_text(body)

    template = load_template()
    formatted_email = template.render(
        recipient_name=recipient_name,
        subject=subject,
        body=body,
        sender_name=sender_name,
        sender_role=sender_role,
        company_name=company_name,
        current_date=datetime.now().strftime("%B %d, %Y"),
    )

    print("\n✅ Formatted Email:\n")
    print("=" * 60)
    print(formatted_email)
    print("=" * 60)

    # Optionally save
    save = input("\nDo you want to save this email? (y/n): ").lower()
    if save == "y":
        filename = f"formatted_email_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write(formatted_email)
        print(f"📂 Saved as {filename}")

if __name__ == "__main__":
    format_email()
