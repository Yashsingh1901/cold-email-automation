from flask import Flask, render_template, request
import os
import yagmail
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configuration for email login (loaded from the .env file)
EMAIL_USER = os.getenv('EMAIL_USER', 'your_email@example.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your_password_here')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        # Handle file upload (CSV or Excel)
        file = request.files['email_file']
        if file:
            # Save the uploaded file temporarily
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)

            # Read the emails from the uploaded file (CSV or Excel)
            try:
                if file.filename.endswith('.csv'):
                    email_data = pd.read_csv(file_path)
                elif file.filename.endswith('.xlsx'):
                    email_data = pd.read_excel(file_path)
                else:
                    return "Unsupported file format", 400

                # Get subject and body from the form
                subject = request.form['subject']
                body = request.form['body']

                # Initialize Yagmail for sending emails
                yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASSWORD)

                # Send emails to all addresses in the uploaded file
                for _, row in email_data.iterrows():
                    to_email = row['email']
                    yag.send(to_email, subject, body)

                return "Emails sent successfully!"

            except Exception as e:
                return f"An error occurred: {e}"

        return "No file uploaded", 400

if __name__ == '__main__':
    # Ensure the uploads directory exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(debug=True)
