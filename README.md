# Cold Email Automation System

A powerful and efficient cold email automation system built with Python that helps streamline your outreach campaigns. This system allows you to send personalized cold emails to multiple recipients while maintaining professionalism and tracking engagement.

## Features

- 📧 Automated email sending with personalized templates
- 📊 Excel-based contact management
- 🔄 Template customization and management
- 📈 Email tracking and analytics
- 🔒 Secure email authentication
- 🎯 Batch processing capabilities
- 📱 Responsive web interface for easy management

## Tech Stack

- Python 3.x
- Flask (Web Framework)
- Yagmail (Email Service)
- Pandas (Data Processing)
- HTML/CSS (Frontend)
- Excel (Data Storage)

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Gmail account with App Password enabled

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Yashsingh1901/cold-email-automation.git
cd cold-email-automation
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Configure your email settings:
   - Create a `.env` file in the root directory
   - Add your Gmail credentials:
     ```
     EMAIL=your.email@gmail.com
     APP_PASSWORD=your_app_password
     ```

### Usage

1. Prepare your contact list in Excel format (see `sample_emails.xlsx` for reference)
2. Customize email templates in the `templates` directory
3. Run the server:

```bash
python server.py
```

4. Access the web interface at `http://localhost:5000`

## Project Structure

```
cold-email-automation/
├── server.py           # Main Flask application
├── proj.py            # Core email automation logic
├── templates/         # Email templates and web interface
├── uploads/          # Temporary file storage
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## Security Notes

- Never commit sensitive information like email passwords
- Use environment variables for credentials
- Keep your contact lists secure and comply with data protection regulations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Yash Singh

- GitHub: [@Yashsingh1901](https://github.com/Yashsingh1901)

## Acknowledgments

- Thanks to all contributors and users of this project
- Special thanks to the open-source community for the amazing tools and libraries
