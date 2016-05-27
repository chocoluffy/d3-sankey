import json
import random
from random import randint

# output json structure, 
# {
# 	"nodes": [
# 		{
# 			"name": "cat",
#			"influence": 5  # determine node's height, and positive and negative value should sum up to this value.
# 			"id": 2
# 		}
# 	],
# 	"links": [
# 		{
# 			"source": 0,
# 			"target": 1,
# 			"value": <random number between 0 and 1>
# 		}
# 	]
# }

json_file = open('animals.json')
json_str = json_file.read()
rawdata = json.loads(json_str)

resultjson = {
	"nodes": [],
	"links": []
};

resultjson['nodes'].append({
		'name': 'Sentiment',
		'id': 0
	})

resultjson['nodes'].append({
		'name': 'Positive',
		'id': 1
	})

resultjson['nodes'].append({
		'name': 'Negative',
		'id': 2
	})

base = 3
cap = 30
for index, animal in enumerate(rawdata['animals']):
	rand = randint(1, 10) # randomly generate the influence value.(frequency)
	if(index < cap):
		resultjson['nodes'].append({
			'name': animal,
			'id': index + base,
			'influence': rand}) # start from base
	else:
		break

# resultjson['links'].append({
# 		'source': 0,
# 		'target': 1,
# 		'value' : 20
# 	})

# resultjson['links'].append({
# 		'source': 0,
# 		'target': 2,
# 		'value' : 10
# 	})

posSum = 0
negSum = 0

for node in resultjson['nodes']:
	if node['name'] != 'Positive' and node['name'] != 'Negative' and node['name'] != 'Sentiment': # ignore the first two nodes.
		negProb = random.random() * node['influence'] * 0.6
		posProb = node['influence'] - negProb
		posSum += posProb
		negSum += negProb

		resultjson['links'].append({
				'source': 1,
				'target': node['id'],
				'value': posProb
			})
		resultjson['links'].append({
				'source': 2,
				'target': node['id'],
				'value': negProb
			})
	else:
		continue

resultjson['links'].append({
		'source': 0,
		'target': 1,
		'value' : posSum
	})

resultjson['links'].append({
		'source': 0,
		'target': 2,
		'value' : negSum
	})

posPercentage = posSum / (posSum + negSum)
negPercentage = 1 - posPercentage

def int2percentage(num):
	return "{0:.0f}%".format(num * 100)
	
resultjson['nodes'][0]['influence'] = '100%'
resultjson['nodes'][1]['influence'] = int2percentage(posPercentage)
resultjson['nodes'][2]['influence'] = int2percentage(negPercentage)


# for node in data["results"]:
#     rand = randint(0, 2)
#     node['geoInference'] = {'geoName': countryName[rand], 'geoFlag': countryAcron[rand]}
#     sentiRand = random.random()
#     node['sentimentProbabilities'] = {'POS': sentiRand, 'NEG': (1 - sentiRand)}

with open('output.json', 'w+') as outfile:
    json.dump(resultjson, outfile)













