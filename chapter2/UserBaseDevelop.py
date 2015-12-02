def UserBaseDevelop(prefs,similarity): #input data and similarity funtion name
	global simList
	simList = {}
	for item1 in prefs:
		for item2 in prefs:
			if item1 == item2: continue
			sim = similarity(prefs,item1,item2)
			itemSum=(item1,item2)
			simList[itemSum]=sim
	return simList

def getRecommendations(prefs,person):
	sim = {}
	for item in prefs:
		if item == person:continue
		itemSum = (person,item)
		sim[itemSum] = simList[(item,person)]
	sim = sorted(sim.iteritems(),key=lambda d:d[1],reverse = True)
	sim = sim[0:5]
	return sim