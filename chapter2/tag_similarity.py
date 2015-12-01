import pylast

API_KEY = "71d1ca867d5ae43c3422973f77589e7d"
API_SECRET ="d0e8b27d953ae1abe939be6fa6f58627"
username= "nameless_97"
password_hash = pylast.md5("741963456528ybx?")
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret =API_SECRET, username = username, password_hash = password_hash)

def tanimoto(person1,person2):
	si = {}
	for item in person1:
		if item in person2:si[item] = 1
	c = float(len(si))
	a = len(person1)
	b = len(person2)
	t = c/(a+b-c)
	return t
	
def tagList(tag=''):
	albums_list={}
	albums_list[tag]={}
	tags=network.get_tag(tag)
	for p1 in tags.get_top_albums():
		p1=str(p1)
		p1start=p1.index('Album')+8
		p1end=p1.index(',')-1
		p1=p1[p1start:p1end]
		albums_list[tag][p1]=1.0
	return albums_list
	
def similar(tag1='',tag2=' '):
    raw_list1=tagList(tag1)
    raw_list2=tagList(tag2)
    print raw_list1
    print raw_list2
    coefficient=0
    coefficient=tanimoto(raw_list1,raw_list2)
    return coefficient