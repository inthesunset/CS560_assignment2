import sys
import json

filepath = 'Tapajit_output'
inputlist = sys.argv[1:]

with open(filepath, 'r') as data_file:
    data = json.load(data_file)

for oneword in inputlist:
    if oneword not in data.keys():
        print(oneword + " can't be found in dataset")
        continue
    print("word \"oneword\" are found in these places:")
    for anyone in data[oneword]:
        print('document id:' + '\t' +
              anyone[0] + '\t' + 'line number:' + str(anyone[1]))
    print("********************************************")
