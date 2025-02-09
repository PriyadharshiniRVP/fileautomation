import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
DIRECTORY = R'C:\Users\priya\OneDrive\Documents'  # Change this to your target directory
EMAIL_ADDRESS = 'priyarama2209@gmail.com'  # Your email address
EMAIL_PASSWORD = 'vykk sfyv niqr ljhh'  # Your email password
RECIPIENT_EMAIL = 'priyarama2209@gmail.com'  # Recipient's email address

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  # Change this condition based on your needs
            new_name = f"renamed_{filename}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f'Renamed: {filename} to {new_name}')

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split('.')[-1]
            folder_name = file_extension + '_files'
            folder_path = os.path.join(directory, folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            os.rename(os.path.join(directory, filename), os.path.join(folder_path, filename))
            print(f'Moved: {filename} to {folder_path}')

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

def main():
    rename_files(DIRECTORY)
    organize_files(DIRECTORY)
    send_email('File Management Update', 'Files have been renamed and organized successfully.')

if __name__ == '__main__':
    main()