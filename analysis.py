import re
import requests
import urllib
import json

DEFAULT_DELIMITER = '+++$+++'
DEFAULT_URL = 'http://localhost:3000/'
PROFANITY_DETECTION_ROUTE = 'profanity-detection'

def is_profane(text):
    r = requests.get(DEFAULT_URL + PROFANITY_DETECTION_ROUTE + '?' + urllib.urlencode({'q' : text}))
    return json.loads(r.text)['profane']

characters = {}
f = open('data/movie_characters_metadata.txt')
for line in f:
    arr = line.split(DEFAULT_DELIMITER)
    arr = [e.strip() for e in arr]
    character_id = arr[0]
    character_name = arr[1]
    character_gender = arr[4]
    characters[character_id] = {'name': character_name, 'gender': character_gender}
assert(characters['u354']['name'] == 'MILO')
assert(characters['u354']['gender'] == 'm')
assert(len(characters.keys()) == 9035)
f.close()

utterances = {}
f = open('data/movie_lines.txt')
for line in f:
    arr = line.split(DEFAULT_DELIMITER)
    arr = [e.strip() for e in arr]
    utterance_id = arr[0]
    utterance_character_id = arr[1]
    utterance_text = arr[-1]
    utterances[utterance_id] = {'character_id': utterance_character_id,
                                'character_gender': characters[utterance_character_id]['gender'],
                                'is_profane': is_profane(utterance_text)}
assert(utterances['L538433']['character_id'] == 'u3014')
assert(len(utterances.keys()) == 304713)
f.close()

nb_female_lines = 0
nb_male_lines = 0
nb_female_profane_lines = 0
nb_male_profane_lines = 0
for utterance_id in utterances.keys():
    cur_utterance = utterances[utterance_id]
    spoken_by_male = (cur_utterance['character_gender'] == 'm')
    spoken_by_female = (cur_utterance['character_gender'] == 'f')
    is_profane_line = cur_utterance['is_profane']
    nb_male_lines += int(spoken_by_male)
    nb_male_profane_lines += int(spoken_by_male and is_profane_line)
    nb_female_lines += int(spoken_by_female)
    nb_female_profane_lines += int(spoken_by_female and is_profane_line)
print 'nb_female_lines = ' + str(nb_female_lines)
print 'nb_female_profane_lines = ' + str(nb_female_profane_lines)
print 'nb_male_lines = ' + str(nb_male_lines)
print 'nb_male_profane_lines = ' + str(nb_male_profane_lines)
