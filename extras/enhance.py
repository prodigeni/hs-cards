#!/usr/bin/env python

import os
import re
import sys; sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
print(sys.path)
from xml.dom import minidom
from xml.etree import ElementTree
from fireplace.enums import GameTag
import buffs
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


def guess_overload(card):
	sre = re.search(r"Overload[^(]+\((\d+)\)", card.description)
	amount = int(sre.groups()[0])
	e = card._findTag(GameTag.RECALL)[0]
	e.attrib["value"] = str(amount)
	print("%s: Setting Overload to %i" % (card.name, amount))


def set_tag(card, tag, value):
	e = ElementTree.Element("Tag")
	if isinstance(value, bool):
		e.attrib["value"] = "1" if value else "0"
		e.attrib["Type"] = "Bool"
	elif isinstance(value, int):
		e.attrib["value"] = str(value)
		e.attrib["Type"] = "Int"
	else:
		raise NotImplementedError
	e.attrib["enumID"] = str(int(tag))
	card.xml.append(e)
	print("%s: Setting %r = %r" % (card.name, tag, value))


def remove_tag(card, tag):
	e = card._findTag(tag)[0]
	card.xml.remove(e)
	print("%s: Removing %r tag" % (card.name, tag))


def main():
	from fireplace.cardxml import load

	db, xml = load(sys.argv[1])
	for id, card in db.items():
		if hasattr(buffs, id):
			for tag, value in getattr(buffs, id).items():
				set_tag(card, tag, value)

		if hasattr(chooseone, id):
			add_chooseone_tags(card, getattr(chooseone, id))

		if card.tags.get(GameTag.SPELLPOWER):
			guess_spellpower(card)

		if card.tags.get(GameTag.RECALL):
			guess_overload(card)

		if "Can't Attack." in card.description:
			set_tag(card, GameTag.CANT_ATTACK, True)

		if "Can't be targeted by spells or Hero Powers." in card.description:
			set_tag(card, GameTag.CANT_BE_TARGETED_BY_ABILITIES, True)

		if id == "EX1_283":
			# Remove Freeze from Frost Elemental
			remove_tag(card, GameTag.FREEZE)

	# xml = db[next(db.__iter__())].xml
	with open(sys.argv[2], "w") as f:
		root = ElementTree.Element("CardDefs")
		for e in xml.findall("Entity"):
			# We want to retain the order so we can't just use db.keys()
			id = e.attrib["CardID"]
			card = db[id]
			root.append(card.xml)

		outstr = ElementTree.tostring(root)
		# Reparse for clean indentation
		outstr = minidom.parseString(outstr).toprettyxml(indent="\t")
		outstr = "\n".join(line for line in outstr.split("\n") if line.strip())
		f.write(outstr)
		print("Written to", f.name)


if __name__ == "__main__":
	main()
