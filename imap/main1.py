import imaplib
import email

imap_server = "imap.gmail.com"
email_address = "anjaliingle9421@gmail.com"
password = "gkcd tsjg npty qibi"

# Connect to the IMAP server
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

# Select the "inbox" folder
imap.select("inbox")

# Search for all emails in the inbox
_, msgnums = imap.search(None, "ALL")

# Print message numbers
print(msgnums)

# Loop through each email and print details
for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")

    message = email.message_from_bytes(data[0][1])

    print(f"Message Number: {msgnum}")
    print(f"From: {message.get('From')}")
    print(f"To: {message.get('To')}")
    print(f"BCC: {message.get('BCC')}")
    print(f"Date: {message.get('Date')}")
    print(f"Subject: {message.get('Subject')}")

    # Print the main message content
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            print("Main Message:")
            print(part.get_payload(decode=True).decode(part.get_content_charset(), 'ignore'))
            break  # Stop processing after finding the main text part

    print("\n")  # Add a newline between emails

# Close the connection
imap.close()
