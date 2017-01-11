#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != None:
        return tuple([len(sentence), sentence[0]])
