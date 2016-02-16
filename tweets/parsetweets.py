import csv

def dict2xml(itemDict):
	xml = "<tweet>\n"
	xml += "\t<text>" + itemDict['text'] + "</text>\n"
	xml += "\t<name>" + itemDict['user']['screen_name'] + "</name>\n"
	return xml + "</tweet>\n"

if __name__ == "__main__":
	f = open("goldenglobes.json","r")
	fw = open("tweets.xml","w")

	xml = "<root>\n"
	item = f.readline()
	count = 0
	while item:
		itemDict = eval(item)
		xml += dict2xml(itemDict)
		count += 1
		item = f.readline()
		if count > 1000:
			break
	xml += "</root>"

	fw.write(xml)
	fw.close()
