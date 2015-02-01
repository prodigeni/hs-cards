#!/usr/bin/env python

from xml.etree import ElementTree

import chooseone


def add_chooseone_tags(card, ids):
	for id in ids:
		e = ElementTree.Element("ChooseCard")
		e.attrib["cardID"] = id
		card.xml.append(e)
	print("%s: Adding Choose One cards: %r" % (card.name, ids))

def main():
	path = "../TextAsset/enUS.txt"
	with open(path, "r") as f:
		xml = ElementTree.parse(f)
		for card in xml.findall("Entity"):
			id = card.attrib["CardID"]

			if hasattr(chooseone, id):
				add_chooseone_tags(card, getattr(chooseone, id))


if __name__ == "__main__":
	main()
