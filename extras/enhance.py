#!/usr/bin/env python

import re
import sys; sys.path.append("../..")
from xml.etree import ElementTree

from fireplace.cards import cardxml
from fireplace.enums import GameTag
import chooseone


def add_chooseone_tags(card, ids):
	for id in ids:
		e = ElementTree.Element("ChooseCard")
		e.attrib["cardID"] = id
		card.xml.append(e)
	print("%s: Adding Choose One cards: %r" % (card.name, ids))


def guess_spellpower(card):
	sre = re.search(r"Spell Damage \+(\d+)", card.description)
	dmg = int(sre.groups()[0])
	e = card._findTag(GameTag.SPELLPOWER)[0]
	e.attrib["value"] = str(dmg)
	print("%s: Setting Spell Power to %i" % (card.name, dmg))


def main():
	db = cardxml.load("../TextAsset/enUS.txt")
	for id, card in db.items():
		if hasattr(chooseone, id):
			add_chooseone_tags(card, getattr(chooseone, id))

		if card.tags.get(GameTag.SPELLPOWER):
			guess_spellpower(card)



if __name__ == "__main__":
	main()
