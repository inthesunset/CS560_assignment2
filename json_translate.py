import json
filepath = 'index.json'
filepath2 = 'index2.json'
with open (filepath, 'r') as datafile:
  data = json.load(datafile)
finaldata = {}
for anyword in data.keys():
  finaldata[anyword] = []
  for anydocid in data[anyword].keys():
    item = {'document_id': anydocid, 'line_number':[],'col_number':[]}
    for i in range(len(data[anyword][anydocid])):
      item[line_number].append(data[anyword][anydocid][i][0])
      item[col_number].append(data[anyword][anydocid][i][1])
    finaldata[anyword].append(item)

with open(filepath2,'w') as f:
  json.dump(finaldata,f)
