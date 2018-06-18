import json
import difflib

with open('data.json') as file:
    data=json.load(file)

def translate(word:str)->list:
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        result=difflib.get_close_matches(word,data.keys(),cutoff=0.8)
        if len(result)>0:
            response=input('Did you mean "{}" instead? Press Y for "Yes" or N for "No": '.format(result[0]))
            if response.lower()=='y':
                return data[result[0]]
            elif response.lower()=='n':
                return ["The word doesn't exist. Please double check it."]
            else:
                return ["We didn't understand your entry."]
        else:
            return ["The word doesn't exist. Please double check it."]

word=input('Enter a word: ')
output=translate(word)
for i in output:
    print(i)
