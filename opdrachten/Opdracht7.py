from keyword import iskeyword


def contains_keyword(*args):
    key_word = False
    for arg in args:
        if iskeyword(arg):
            key_word = True
    return key_word


print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha", "lol", "chickens are evel", 42))
print(contains_keyword("four", "for", "if"))
print(contains_keyword("blabla", "doggo", "crab", "anchor",))
print(contains_keyword("grizzly", "ignore", "return", "False"))
