favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

participants = ['john', 'edward', 'steve', 'phil', 'bill']

for participant in participants:
    if participant in favorite_languages.keys():
        print(f"Thank you for taking the poll, {participant.title()}!")
    else:
        print(f"Please take part in the poll, {participant.title()}.")