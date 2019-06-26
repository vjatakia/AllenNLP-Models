import json
import numpy as np

actions = ['playing', 'paying']
table = []
with open('test_examples_srl.json', 'r') as f:
    for line in f:
        table.append(json.loads(line))

i = 0
for row in table:
    print(row['words'])
    i+= 1
    for verb in row['verbs']:
            indices = []
            if verb['verb'] in actions:
                print(verb['tags'])
    if i > 0:
        break
