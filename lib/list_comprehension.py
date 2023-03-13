#!/usr/bin/env python3

def return_evens(num_list):
    pass
    new_list = [x for x in num_list if not x % 2]
    return new_list

def make_exclamation(sentence_list):
    new_list = [x + "!" for x in sentence_list]
    return new_list
    pass