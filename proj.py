import os
from dotenv import load_dotenv
import pandas as pd
import yagmail

# Load email credentials from .env file
load_dotenv()
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Initialize the email client
yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASSWORD)

def personalize_email_template(hr_name, company_name):
    """Personalizes the email template with the HR name and company name."""
    email_template = """Subject: Internship Application – Yash Singh

Dear {HRName},

I hope this message finds you well. My name is Yash Singh, and I am currently pursuing a Bachelor of Technology in Information Technology at Jaypee Institute of Technology. I am writing to express my keen interest in an internship opportunity at {CompanyName}.

With a solid foundation in software development, I am eager to apply my knowledge in a professional setting and contribute meaningfully to the innovative work at {CompanyName}. My academic projects, coupled with my previous internship experience at Bhavna Software India Private Limited, have equipped me with the skills to tackle real-world challenges effectively.

I have attached my resume for your review. I would welcome the opportunity to discuss how my skills and aspirations align with the objectives of your esteemed organization.

Thank you for considering my application. Please feel free to reach out if there are any internship openings or if you require further details. I look forward to the possibility of contributing to your team.

Best regards,
Yash Singh
Phone: +91-8005526982
Email: ys648839@gmail.com
"""
    return email_template.format(HRName=hr_name, CompanyName=company_name)

def send_personalized_emails(excel_file, attachment=None):
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file)

        # Check if required columns exist
        required_columns = ['HR Name', 'Company Name', 'Email']
        for col in required_columns:
            if col not in df.columns:
                print(f"Error: '{col}' column not found in the Excel file.")
                return

        # Iterate through each row and send personalized email
        for index, row in df.iterrows():
            hr_name = row['HR Name']
            company_name = row['Company Name']
            email = row['Email']

            # Generate the personalized email body
            body = personalize_email_template(hr_name, company_name)

            print(f"Sending email to {email} ({hr_name} at {company_name})...")

            # Send email with optional attachment
            yag.send(
                to=email,
                subject="Internship Application – Yash Singh",
                contents=body,
                attachments=attachment
            )

            print(f"Email sent to {email}!")

        print("All emails have been sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
if __name__ == "__main__":
    # Define inputs
    excel_file = input("Enter the path to the Excel file: ")
    attachment = input("Enter the path to the attachment (leave blank if none): ") or None

    # Call the function to send personalized emails
    send_personalized_emails(excel_file, attachment)
