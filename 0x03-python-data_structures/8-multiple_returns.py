#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        return tuple([len(sentence), sentence[0]])
    else:
        return tuple([0, None])
