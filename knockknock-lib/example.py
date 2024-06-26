from knockknock import email_sender


@email_sender(recipient_emails=["udson.willams@gmail.com"], sender_email="udsonqa@gmail.com")
def train_your_nicest_model():
    import time
    time.sleep(20)
    return {'loss': 0.9} # Optional return value

if __name__ == "__main__":
    train_your_nicest_model()
