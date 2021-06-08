# message = input("Tell me something, I will repeat it back to you: ")
# print(message)

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nPress 'q' to quit the program. "

active = True
while active:
        message = input(prompt) 
        if message == 'q':
            active = False
        else:
            print(message)