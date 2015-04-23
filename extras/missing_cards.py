from fireplace.enums import CardType, GameTag


__all__ = [
	"GVG_003e", "GVG_017e",
	"EX1_144e",
	"CS2_227a",
	"EX1_076a", "EX1_145oa", "EX1_315a", "EX1_591a", "EX1_608a", "EX1_612oa", "EX1_616a",
	"FP1_017a", "FP1_030ea", "FP1_031a",
	"GVG_006a", "GVG_021e2",
	"NEW1_029ta",
]


# Missing buffs

GVG_003e = {
	GameTag.CARDNAME: "Unstable Portal Buff",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.COST: -3,
}

GVG_017e = {
	GameTag.CARDNAME: "Call Pet Buff",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.COST: -4,
}

EX1_144e = {
	GameTag.CARDNAME: "Shadowstep Buff",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.COST: -2,
}


# Missing auras

CS2_227a = {
	GameTag.CARDNAME: "Venture Co. Mercenary (Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.COST: 3,
}

EX1_076a = {
	GameTag.CARDNAME: "Pint-Sized Summoner (Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.COST: -1,
}

EX1_145oa = {
	GameTag.CARDNAME: "Preparation (Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.COST: -3,
}

EX1_315a = {
	GameTag.CARDNAME: "Summoning Portal (Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
}

EX1_591a = {
	GameTag.CARDNAME: "Auchenai Soulpriest (Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.OUTGOING_HEALING_ADJUSTMENT: -1,
}

EX1_608a = {
	GameTag.CARDNAME: "Sorcerer's Apprentice (Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.COST: -1,
}

EX1_612oa = {
	GameTag.CARDNAME: "Power of the Kirin Tor (Kirin Tor Mage Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
}

EX1_616a = {
	GameTag.CARDNAME: "Mana Wraith (Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.COST: 1,
}

FP1_017a = {
	GameTag.CARDNAME: "Nerub'ar Weblord (Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.COST: 2,
}

FP1_030ea = {
	GameTag.CARDNAME: "Necrotic Aura (Loatheb Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
}

FP1_031a = {
	GameTag.CARDNAME: "Baron Rivendare (Deathrattle Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.EXTRA_DEATHRATTLES: True,
}

GVG_006a = {
	GameTag.CARDNAME: "Mechwarper (Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.COST: -1,
}

GVG_021e2 = {
	GameTag.CARDNAME: "Mal'Ganis Hero Immune Aura",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.CANT_BE_DAMAGED: True,
}

GVG_122a = {
	GameTag.CARDNAME: "Wee Spellstopper Aura",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
	GameTag.CANT_BE_TARGETED_BY_ABILITIES: True,
	GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: True,
}

NEW1_029ta = {
	GameTag.CARDNAME: "Kill Millhouse! (Millhouse Aura)",
	GameTag.CARDTYPE: CardType.ENCHANTMENT,
}
