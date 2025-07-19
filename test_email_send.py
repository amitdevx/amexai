import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
from dotenv import load_dotenv
import asyncio

# Step 1: Load environment variables
load_dotenv()

# Step 2: Email function
async def send_email(
    to_email: str,
    subject: str,
    message: str,
    cc_email: Optional[str] = None
) -> str:
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        gmail_user = os.getenv("GMAIL_USER")
        gmail_password = os.getenv("GMAIL_APP_PASSWORD")

        if not gmail_user or not gmail_password:
            return "Email sending failed: Gmail credentials not configured."

        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = to_email
        msg['Subject'] = subject

        recipients = [to_email]
        if cc_email:
            msg['Cc'] = cc_email
            recipients.append(cc_email)

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, recipients, msg.as_string())
        server.quit()

        return f"✅ Email sent successfully to {to_email}"

    except smtplib.SMTPAuthenticationError:
        return "❌ Authentication error. Check Gmail credentials."
    except Exception as e:
        return f"❌ Error sending email: {str(e)}"

# Step 3: Test function
async def test_email_send():
    to = "fakudas69@gmail.com"  # 👈 Yahan apna dusra email likho
    subject = "Test Email from Dhwaj"
    message = "Hello! This is a test email from Dhwaj AI."
    result = await send_email(to, subject, message)
    print(result)

# Step 4: Run the test
asyncio.run(test_email_send())
