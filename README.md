Automated Email Sender for Job Applications
This mini-project is a Python script designed to automate the process of sending acceptance and rejection emails to candidates who have applied for a working student position. The script reads candidate information from a CSV file, categorizes them based on their application status, and sends personalized emails accordingly.

Features
Reads candidate data from a CSV file.
Categorizes candidates into accepted and rejected lists.
Sends personalized acceptance emails to accepted candidates.
Sends personalized rejection emails to rejected candidates.
Uses Gmail's SMTP server for sending emails.
Project Structure
interview_candidates1.csv: CSV file containing candidate information.
email_sender.py: Python script that handles reading the CSV file and sending emails.
Requirements
Python 3.x
smtplib library (included in the Python Standard Library)
email library (included in the Python Standard Library)
Gmail account for sending emails
CSV File Format
The CSV file should have the following format:

sql
Copy code
First Name,Last Name,Email Address,Accepted
John,Doe,johndoe@example.com,Yes
Jane,Smith,janesmith@example.com,No
...
How to Use
Clone the repository to your local machine.
Ensure you have the required libraries (Python 3.x).
Update the interview_candidates1.csv file with the list of candidates.
Run the email_sender.py script.
When prompted, enter your Gmail address and password (consider using app-specific passwords for security).
