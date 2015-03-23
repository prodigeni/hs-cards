from fireplace.enums import GameTag


# Buff helper
def buff(atk=0, health=0):
	ret = {}
	if atk:
		ret[GameTag.ATK] = atk
	if health:
		ret[GameTag.HEALTH] = health
	return ret


###
# Classic set
#


##
# Druid

# Claws
CS2_017o = buff(atk=1)

# Rooted (Ancient of War)
EX1_178ae = {
	GameTag.HEALTH: 5,
	GameTag.TAUNT: True,
}

# Uproot (Ancient of War)
EX1_178be = buff(atk=5)

# Claw
CS2_005o = buff(atk=2)

# Mark of the Wild
CS2_009e = {
	GameTag.ATK: 2,
	GameTag.HEALTH: 2,
	GameTag.TAUNT: True,
}

# Savage Roar
CS2_011o = buff(atk=2)

# Mark of Nature (Attack)
EX1_155ae = buff(atk=4)

# Mark of Nature (Health)
EX1_155be = {
	GameTag.HEALTH: 4,
	GameTag.TAUNT: True,
}

# Leader of the Pack (Power of the Wild)
EX1_160be = buff(+1, +1)

# Bite
EX1_570e = buff(atk=4)


##
# Hunter

# Master's Presence (Houndmaster)
DS1_070o = {
	GameTag.ATK: 2,
	GameTag.HEALTH: 2,
	GameTag.TAUNT: True,
}

# Furious Howl (Timber Wolf)
DS1_175o = buff(atk=1)

# Charge (Tundra Rhino)
DS1_178e = {
	GameTag.CHARGE: True,
}

# Well Fed (Scavenging Hyena)
EX1_531e = buff(+2, +1)

# Bestial Wrath

EX1_549o = {
	GameTag.ATK: 2,
	GameTag.CANT_BE_DAMAGED: True,
}

# Trapped (Freezing Trap)
EX1_611e = {
	GameTag.COST: 2,
}

# Eye in the Sky (Leokk)
NEW1_033o = buff(atk=1)

# Upgraded (Eaglehorn Bow)
EX1_536e = {
	GameTag.DURABILITY: 1,
}


##
# Mage

# Raw Power! (Ethereal Arcanist)
EX1_274e = buff(+2, +2)

# Mana Gorged (Mana Wyrm)
NEW1_012o = buff(atk=1)


##
# Paladin

# Blessing of Might
CS2_087e = buff(atk=3)

# Blessing of Kings
CS2_092e = buff(+4, +4)

# Justice Served (Sword of Justice)
EX1_366e = buff(+1, +1)


##
# Priest

# Warded (Lightwarden)
EX1_001e = buff(atk=2)

# Infusion (Temple Enforcer)
EX1_623e = buff(health=3)

# Power Word: Shield
CS2_004e = buff(health=2)

# Dark Command (Shadow Madness)
EX1_334e = {
	GameTag.OneTurnEffect: True,
}


##
# Rogue

# VanCleef's Vengeance (Edwin VanCleef)
EX1_613e = buff(+2, +2)

# Cold Blood (+2)
CS2_073e = buff(atk=2)

# Cold Blood (+4)
CS2_073e2 = buff(atk=4)

# Deadly Poison
CS2_074e = buff(atk=2)

# Conceal
EX1_128e = {
	GameTag.STEALTH: True,
}


##
# Shaman

# Overloading (Unbound Elemental)
EX1_258e = buff(+1, +1)

# Flametongue (Flametongue Totem)
EX1_565o = buff(atk=2)

# Ancestral Infusion (Ancestral Healing)
CS2_041e = {
	GameTag.TAUNT: True,
}

# Rockbiter Weapon
CS2_045e = buff(atk=3)

# Bloodlust
CS2_046e = buff(atk=3)

# Totemic Might
EX1_244e = buff(health=2)


##
# Warlock

# Blood Pact (Blood Imp)
CS2_059o = buff(health=1)

# Power Overwhelming
EX1_316e = buff(+4, +4)


# Demonfire
EX1_596e = buff(+2, +2)


##
# Warrior

# Berserk (Frothing Berserker)
EX1_604o = buff(atk=1)

# Whipped Into Shape (Cruel Taskmaster)
EX1_603e = buff(atk=2)

# Charge
CS2_103e2 = {
	GameTag.ATK: 2,
	GameTag.CHARGE: True,
}

# Rampage
CS2_104e = buff(+3, +3)

# Heroic Strike
CS2_105e = buff(atk=4)

# Upgraded (Upgrade!)
EX1_409e = {
	GameTag.ATK: 1,
	GameTag.DURABILITY: 1,
}

# Inner Rage
EX1_607e = buff(atk=2)

# Commanding Shout
NEW1_036e = {
	GameTag.HEALTH_MINIMUM: 1,
}


##
# Neutral common

# Enhanced (Raid Leader)
CS2_122e = buff(atk=1)

# Might of Stormwind (Stormwind Champion)
CS2_222o = buff(+1, +1)

# Frostwolf Banner (Frostwolf Warlord)
CS2_226e = buff(+1, +1)

# Berserking (Gurubashi Berserker)
EX1_399e = buff(atk=3)

# Sharp! (Spiteful Smith)
CS2_221e = buff(atk=2)

# 'Inspired' (Abusive Seargent)
CS2_188o = buff(atk=2)

# Cleric's Blessing (Shattered Sun Cleric)
EX1_019e = buff(+1, +1)

# Tempered (Dark Iron Dwarf)
EX1_046e = buff(atk=2)

# Strength of the Pack (Dire Wolf Alpha)
EX1_162o = buff(atk=1)

# Mlarggragllabl! (Grimscale Oracle)
EX1_508o = buff(atk=1)

# Cannibalize (Flesheating Ghoul)
tt_004o = buff(atk=1)


##
# Neutral rare

# Elune's Grace (Young Priestess)
EX1_004e = buff(health=1)

# Hour of Twilight (Twilight Drake)
EX1_043e = buff(health=1)

# Level Up! (Questing Adventurer)
EX1_044e = buff(+1, +1)

# Empowered (Mana Addict)
EX1_055o = buff(atk=2)

# Keeping Secrets (Secretkeeper)
EX1_080o = buff(+1, +1)

# Hand of Argus (Defender of Argus)
EX1_093e = {
	GameTag.ATK: 1,
	GameTag.HEALTH: 1,
	GameTag.TAUNT: True,
}

# Mrghlglhal (Coldlight Seer)
EX1_103e = buff(health=2)

# Blarghghl (Murloc Tidecaller)
EX1_509e = buff(atk=1)

# Equipped (Master Swordsmith)
NEW1_037e = buff(atk=1)


##
# Neutral epic

# Shadows of M'uru (Blood Knight)
EX1_590e = buff(+3, +3)

# Mrgglaargl! (Murloc Warleader)
EX1_507e = buff(+2, +1)

# Full Belly (Hungry Crab)
NEW1_017e = buff(+2, +2)

# Yarrr! (Southsea Captain)
NEW1_027e = buff(+1, +1)


##
# Neutral legendary

# Bananas (King Mukla)
EX1_014te = buff(+1, +1)

# Greenskin's Command (Captain Greenskin)
NEW1_024o = {
	GameTag.ATK: 1,
	GameTag.DURABILITY: 1,
}

# Growth (Gruul)
NEW1_038o = buff(+1, +1)

# Emboldened! (Emboldener 3000)
Mekka3e = buff(+1, +1)


##
# Curse of Naxxramas set
#

# Consume (Shade of Naxxramas)
FP1_005e = buff(+1, +1)

# Power of the Ziggurat (Dark Cultist)
FP1_023e = buff(health=3)

# Darkness Calls (Undertaker)
FP1_028e = buff(atk=1)


##
# Goblins vs. Gnomes set
#

##
# Hunter

# Metal Teeth (Metaltooth Leaper)
GVG_048e = buff(atk=2)

# Glaivezooka
GVG_043e = buff(atk=1)


##
# Paladin

# Retribution (Bolvar Fordragon)
GVG_063a = buff(atk=1)


##
# Neutral common

# Metabolized Magic (Stonesplinter Trogg)
GVG_067a = buff(atk=1)

# Metabolized Magic (Burly Rockjaw Trogg)
GVG_068a = buff(atk=2)

# Pistons (Micro Machine)
GVG_076a = buff(atk=1)


##
# Neutral epic

# HERE, TAKE BUFF. (Hobgoblin)
GVG_104a = buff(+2, +2)


##
# Spare parts

# Armor Plating
PART_001e = buff(health=1)

# Cloaked (Finicky Cloakfield)
PART_004e = {
	GameTag.STEALTH: True,
}

# Whirling Blades
PART_007e = buff(atk=1)


###
# Debug set
#

# Weapon Buff Enchant
XXX_054e = buff(+100, +100)

# 1000 Stats Enchant
XXX_055e = buff(+1000, +1000)
