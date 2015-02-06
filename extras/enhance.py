#!/usr/bin/env python

import sys; sys.path.append("../..")
from xml.etree import ElementTree

from fireplace.cards import cardxml
import chooseone


def add_chooseone_tags(card, ids):
	for id in ids:
		e = ElementTree.Element("ChooseCard")
		e.attrib["cardID"] = id
		card.xml.append(e)
	print("%s: Adding Choose One cards: %r" % (card.name, ids))

def main():
	db = cardxml.load("../TextAsset/enUS.txt")
	for id, card in db.items():
		if hasattr(chooseone, id):
			add_chooseone_tags(card, getattr(chooseone, id))


if __name__ == "__main__":
	main()
