def correct_sentence(text: str) -> str:
    if text[-1] == '.':
        return text[0].upper() + text[1:]
    else:
        return text[0].upper() + text[1:] + '.'


assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, Friends.") == "Greetings, Friends."
