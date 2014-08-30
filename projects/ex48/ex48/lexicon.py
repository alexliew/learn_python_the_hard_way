def scan(phrase):
    """Takes in a phrase and returns the tokens for that phrase"""
    words = phrase.split(' ')
    directions = ('north', 'south', 'east', 'west', 'up', 'down', 'left', 'right', 'back')
    verbs = ('go', 'kill', 'eat', 'stop', 'run')
    stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
    nouns = ('door', 'bear', 'princess', 'cabinet', 'honey')

    tokens = []
    for word in words:
        if word in directions:
            tokens.append(('direction', word))
        elif word in verbs:
            tokens.append(('verb', word))
        elif word in stop_words:
            tokens.append(('stop', word))
        elif word in nouns:
            tokens.append(('noun', word))
        elif word.isdigit():
            tokens.append(('number', int(word)))
        else:
            # everything else is an error
            tokens.append(('error', word))

    return tokens
