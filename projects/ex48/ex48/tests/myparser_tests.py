from nose.tools import *
from ex48.lexicon import *
from ex48.parser import *

def test_sentence():
    words = scan('player eat honey')
    s = Sentence(*words)
    assert_equal(s.subject, 'player')
    assert_equal(s.verb, 'eat')
    assert_equal(s.object, 'honey')
    # note that it doesn't check whether the words given are actually verbs or nouns

def test_peek():
    words = scan('the bear eat the honey')
    assert_equal(peek(words), 'stop')

def test_peek_empty():
    words2 = []
    assert_equal(peek(words2), None)

def test_skip():
    words = scan('the bear eat the honey')
    ref = scan('the bear eat the honey')
    skip(words, 'stop')
    assert_equal(words, ref[1:])

def test_match():
    words = scan('the bear eat the honey')
    assert_equal(match(words, 'stop'), ('stop', 'the'))

def test_match_empty():
    words = []
    assert_equal(match(words, 'stop'), None)

def test_match_wrong():
    words = scan('the bear eat the honey')
    assert_equal(match(words, 'noun'), None)

def test_parse_verb():
    words = scan('it eat the honey')
    assert_equal(parse_verb(words), ('verb', 'eat'))

def test_parse_verb_wrong():
    words = scan('the bear eat the honey')
    assert_raises(ParserError, parse_verb, words)

def test_parse_subject():
    words = scan('the bear eat the honey')
    assert_equal(parse_subject(words), ('noun', 'bear'))

def test_parse_subject_implicit():
    words = scan('eat the honey')
    assert_equal(parse_subject(words), ('noun', 'player'))

@raises(ParserError)
def test_parse_subject_wrong():
    words = scan('the it')
    parse_subject(words)

def test_parse_object():
    words = scan('the honey')
    assert_equal(parse_object(words), ('noun', 'honey'))

def test_parse_object_direction():
    words = scan('the north')
    assert_equal(parse_object(words), ('direction', 'north'))

def test_parse_object_wrong():
    words = scan('the it run')
    assert_raises(ParserError, parse_object, words)

def test_parse_sentence():
    words = scan('the bear eat the honey')
    attempt = parse_sentence(words)
    sol_words = scan('bear eat honey')
    solution = Sentence(*sol_words)

    assert_equal(attempt, solution)
