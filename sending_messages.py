def show_messages(texts):
    for text in texts:
        print(f"\n{text}")


def send_messages(texts):
    while texts:
        sent_msg = texts.pop()
        print(f"\nSent the message: {sent_msg}")
        sent_messages.append(sent_msg)




messages = ['hello world!', 'how are you?', 'shush you shmuck']

sent_messages = []

send_messages(messages)

print("\nSent Messages:")

show_messages(sent_messages)

print(messages)