def between_markers(text: str, start: str, end: str) -> str:
    if start in text and end in text:
        return text[text.find(start)+len(start):text.find(end)]
    elif start not in text and end in text:
        return text[0:text.find(end)]
    elif end not in text and start in text:
        return text[text.find(start)+len(start):]
    else:
        return text


if __name__ == '__main__':

    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    assert between_markers('What is >apple<', '>', '<') == 'apple'
    assert between_markers('What is [apple]', '[', ']') == 'apple'
    assert between_markers('What is ><', '>', '<') == ''
    assert between_markers('[an apple]', '[', ']') == 'an apple'

    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>", "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
