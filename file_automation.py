import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Setup Logging
logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Configuration (Use Environment Variables for Security)
DIRECTORY = R'C:\Users\priya\OneDrive\Documents'  # Change this to your target directory
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # Your email from environment variable
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Your email password from environment variable
RECIPIENT_EMAIL = 'priyarama2209@gmail.com'  # Recipient's email address

def rename_files(directory):
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):  # Change this condition based on your needs
                new_name = f"renamed_{filename}"
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
                logging.info(f'Renamed: {filename} → {new_name}')
    except Exception as e:
        logging.error(f"Error renaming files: {e}")

def organize_files(directory):
    try:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                file_extension = filename.split('.')[-1]
                folder_name = file_extension + '_files'
                folder_path = os.path.join(directory, folder_name)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                os.rename(os.path.join(directory, filename), os.path.join(folder_path, filename))
                logging.info(f'Moved: {filename} → {folder_path}')
    except Exception as e:
        logging.error(f"Error organizing files: {e}")

def send_email(subject, body, attachment_path="log.txt"):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Attach log file
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={attachment_path}")
            msg.attach(part)

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        logging.info("Email sent successfully.")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

def main():
    rename_files(DIRECTORY)
    organize_files(DIRECTORY)
    send_email('File Management Update', 'Files have been renamed and organized successfully. See attached log.')

if __name__ == '__main__':
    main()

