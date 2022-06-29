# Create class Email. The __init__ method should receive sender, receiver and a content. It should also have a default set to False attribute called is_sent. The class should have two additional methods:
# •	send() - sets the is_sent attribute to True
# •	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


# You will receive some emails until you receive "Stop" (separated by single space).
# The first will be the sender, the second one – the receiver and the third one – the content
# On the final line you will be given the indices of the sent emails separated by comma and space.
# Call the send() method for the given emails. For each email call the get_info() method

my_emails = []

current_email = input()
while not current_email == "Stop":
    current_email = current_email.split()
    current_sender, current_receiver, current_content = current_email[0], current_email[1], current_email[2]
    my_current_email = Email(current_sender, current_receiver, current_content)
    my_emails.append(my_current_email)
    current_email = input()

sent_emails_indices = [int(index) for index in input().split(", ")]
for email_sent in sent_emails_indices:
    my_emails[email_sent].send()

for email in my_emails:
    print(email.get_info())
