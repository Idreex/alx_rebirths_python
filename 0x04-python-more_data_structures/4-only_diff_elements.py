#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = set_1 - set_2
    new_set.update(set_2 - set_1)
    return new_set

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
print(only_diff_elements(set_1, set_2))