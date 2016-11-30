import re

DEFAULT_DELIMITER = '+++$+++'

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
    utterances[utterance_id] = {'character_id': utterance_character_id, 'text': utterance_text.lower()}
assert(utterances['L538433']['character_id'] == 'u3014')
assert(utterances['L538433']['text'] == "When whoever it is makes their move, you won't be here to ask if he's the one.".lower())
assert(len(utterances.keys()) == 304713)
f.close()
