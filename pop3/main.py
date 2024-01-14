import poplib
from email import parser

pop_server = "pop.gmail.com"
email_address = "anjaliingle9421@gmail.com"
password = "gkcd tsjg npty qibi"

pop = poplib.POP3_SSL(pop_server)
pop.user(email_address)
pop.pass_(password)

# Get the number of messages in the mailbox
num_messages = len(pop.list()[1])

for i in range(1, num_messages + 1):
    # Retrieve the email by message number
    _, message_data, _ = pop.retr(i)
    message_text = b'\n'.join(message_data).decode('utf-8')
    
    # Parse the email using the email.parser.Parser class
    email_message = parser.Parser().parsestr(message_text)
    
    print(f"Message Number: {i}")
    print(f"From: {email_message['From']}")
    print(f"To: {email_message['To']}")
    print(f"Date: {email_message['Date']}")
    print(f"Subject: {email_message['Subject']}")
    
    print("Content:")
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            print(part.get_payload(decode=True).decode('utf-8'))

# Close the connection
pop.quit()
