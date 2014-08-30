class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = w_val(subject)
        self.verb = w_val(verb)
        self.object = w_val(obj)

    def __eq__(self, other):
        return self.subject == getattr(other, 'subject', None) and \
               self.verb == getattr(other, 'verb', None) and \
               self.object == getattr(other, 'object', None)

    def __str__(self):
        return "{}, {}, {}".format(self.subject, self.verb, self.object)

def w_type(token):
    return token[0]

def w_val(token):
    return token[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return w_type(word)
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if w_type(word) == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
