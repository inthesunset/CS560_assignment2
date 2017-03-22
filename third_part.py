import sys
import json

filepath = 'index.json'
inputlist = sys.argv[1:]

with open(filepath, 'r') as data_file:
    data = json.load(data_file)

for oneword in inputlist:
    if oneword not in data.keys():
        print(oneword + " can't be found in dataset")
        continue
    print("word" + '\"'+oneword+'\" are found in these places:')
    for anyone in data[oneword].keys():
        print('document id:' + '\t' +
              anyone)
        for line_col in data[oneword][anyone]:
            print('line number:' + str(line_col[0]))
        
    print("********************************************")
