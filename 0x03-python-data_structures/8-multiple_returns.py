#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return 0, None
    if sentence is None:
        return 0,  None
    else:
        return len(sentence), sentence [0]
