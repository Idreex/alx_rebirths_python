#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    
    newdict = a_dictionary.copy()
    dictlist = list(newdict.items())
    for item in dictlist:
        if value in item:
            dictlist.remove(item)    

    return dict(dictlist)

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
print(complex_delete(a_dictionary, 'C'))







