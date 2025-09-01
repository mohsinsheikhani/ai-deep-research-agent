import os
from typing import Dict
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from agents import Agent, function_tool

gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")
from_email = os.getenv("GMAIL_USER")
to_email = os.getenv("GMAIL_TO")


@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the given subject and HTML body"""

    # Create the email
    msg = MIMEText(html_body, "html")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_email, gmail_app_password)
            server.send_message(msg)
        return {"status": "success"}
    except Exception as e:
        return {"status": "failure", "message": str(e)}


INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini",
)
