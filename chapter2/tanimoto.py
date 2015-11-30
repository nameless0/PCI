def tanimoto(prefs,person1,person2):
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:si[item] = 1
	c = float(len(si))
	a = len(prefs[person1])
	b = len(prefs[person2])
	t = c/(a+b-c)
	return t