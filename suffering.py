#import random
#import math
from pain import *
from misery import *
from theft import *
from trouble import *
from purgatory import *
import math


def doDev(P1):
  #dev is a triton fighter
  P1.Stats = [15, 12, 13, 8, 14, 11]
  racefinder(P1, 9)
  P1.Skills.append(['Athletics', 'Insight'])
  welcometoleagueofdraven(P1, 2)

def monsterfinder(type, i):
  if type == 1:
    if i == 1:
      kobbo = Monster()
      kobbo.Name = 'Suvlo'
      kobbo.Stats = [7, 15, 9, 8, 7, 8]
      kobbo.AC = 12
      kobbo.MaxHP = kobbo.HP = 5
      kobbo.Atk[0].Name = 'Dagger'
      kobbo.Atk[0].AtkBonus = 4
      kobbo.Atk[0].DmgDie = 4
      kobbo.Atk[0].DmgBonus = 2
      kobbo.Atk[1] = kobbo.Atk[0]
      kobbo.Atk[1].Name = 'Sling'
      kobbo.Atk[1].DmgType = 'bludgeoning'

      return kobbo
    
    if i == 2:
      crab = Monster()
      crab.Name = 'Giant Crab'
      crab.Stats = [13, 15, 11, 1, 9, 3] 
      crab.AC = 15
      crab.MaxHP = crab.HP = 13
      crab.Atk[0].Name = 'Claw'
      crab.Atk[0].AtkBonus = 3
      crab.Atk[0].DmgDie = 6
      crab.Atk[0].DmgBonus = 1
      crab.Atk[0].DmgType = 'bludgeoning'

      return crab
  
  elif type == 2:
     if i == 1:
       drow = Monster()
       drow.Name = 'Myrbrin'
       drow.Str = 11
       drow.Dex = 12
       drow.Con = 10
       drow.Int = 10
       drow.Wis = 11
       drow.Cha = 10
       drow.AC = 12
       drow.HP = 9
       drow.Atk[0].Name = 'Scimitar'
       drow.Atk[0].AtkBonus = 3
       drow.Atk[0].DmgDie = 6
       drow.Atk[0].DmgBonus = 1
       drow.Atk[0].DmgType = 'slashing'
 
       return drow
  
     if i == 2:
        spider = Monster()
        spider.Name = 'Spider'
        spider.Str = 2
        spider.Dex = 14
        spider.Con = 18
        spider.Int = 1
        spider.Wis = 14
        spider.Cha = 7
        spider.AC = 12
        spider.HP = 3
        spider.Atk[0].Name = 'Bite'
        spider.Atk[0].AtkBonus = 4
        spider.Atk[0].DmgDie = 1
        spider.Atk[0].DmgBonus = 0
        spider.Atk[0].SaveAtk = '1'
        spider.Atk[1].Name = 'Poison Bite'
        spider.Atk[1].SaveDC = 9
        spider.Atk[1].SaveAtk = 'Con'
        spider.Atk[1].DmgDie = 4
        spider.Atk[1].DmgBonus = 0
        spider.Atk[1].DmgType = 'poison'
 
        return spider

  elif type == 3:
    if i == 1:
      owl = Monster()
      owl.Name = 'Dr. Hoo'
      owl.Str = 13
      owl.Dex = 15
      owl.Con = 12
      owl.Int = 8
      owl.Wis = 13
      owl.Cha = 10
      owl.AC = 12
      owl.HP = 19
      owl.Atk[0].Name = 'Talons'
      owl.Atk[0].AtkBonus = 3
      owl.Atk[0].DmgDie = '2d6'
      owl.Atk[0].DmgBonus = 1
      owl.Atk[0].DmgType = 'slashing'

      return construct

    if i == 2:
      monodrone = Monster()
      monodrone.Name = 'Probe'
      monodrone.Str = 10
      monodrone.Dex = 13
      monodrone.Con = 12
      monodrone.Int = 4
      monodrone.Wis = 10
      monodrone.Cha = 5
      monodrone.AC = 15
      monodrone.HP = 5
      monodrone.Atk[0].Name = 'Dagger'
      monodrone.Atk[0].AtkBonus = 3
      monodrone.Atk[0].DmgDie = 4
      monodrone.Atk[0].DmgBonus = 1
      monodrone.Atk[1].Name = 'Javelin'
      monodrone.Atk[1].AtkBonus = 2
      monodrone.Atk[1].DmgDie = 6
      monodrone.Atk[1].DmgBonus = 0

      return monodrone



def raceinfo(a):
  br()
  if a == 1: #Elf
    print('\x1B[3mElves are a magical people of otherworldly grace, living in the world but not entirely part of it.\n\x1B[0m')
    print('As an elf you have darkvision and resistance to charms due to your fey descendence.Every elf gets +2 Dexterity.\n')
    print('\033[1mElves have 6 subraces:\033[0m\nDark Elves aka Drow are elves from the Underdark, with better darkvision and spells such as Dancing Lights and Faerie Fire. They get +1 Charisma.\n')
    print('Eladrin elves come directly from the Feywild, bringing with them the power of seasons and short distance teleportation. They also get +1 Charisma.\n')
    print('High elves aka Sun/Moon elves are elves exceptionally proficient in combat and magic. They get +1 Intelligence.\n')
    print('Sea elves are, as the name suggests, native to water thus being proficient in aquatic weapons such as tridents. They get +1 Constitution.\n')
    print('The Shadar-kai are elves working for the Raven Queen, thus they dwelve from Shadowfell, to fulfill their duty in eliminating undead. They are resistant against such forces. They also get +1 Constitution.\n')
    print('Wood elves aka forest/wild elves are distrusting of non-elves and native to the forests further from society, they\'re faster and can easily hide in the wild. They get +1 Wisdom.\n')

  if a == 2: #Gnome
    print('\x1B[3mGnomes take delight in life, enjoying every moment of invention, exploration, investigation, creation, and play.\n\x1B[0m')
    print('Gnomes are small and smart. They have darkvision, and their cunning mind is strong against magic. Every gnome gets +2 Intelligence.\n')
    print('\033[1mGnomes have 3 subraces:\033[0m\nDeep gnomes aka Svirfneblin are gnomes found deep in the underground and Underdark. Their darkvision is superior and their stone-like skin make it easy to hide in caves. They get +1 Dexterity.\n')
    print('Forest gnomes are adapted to the wild and thus can speak with small beasts and creat magical illusions. They also get +1 Dexterity.\n')
    print('Rock gnomes are the most common gnomes, found all over the surface so long as rocks are readily available. They\'re natural born tinkers and are historians when the subject is technology. They get +1 Constitution.\n')

  if a == 3: #Half-elf
    print('\x1B[3mHalf-elves combine what some say are the best qualities of their elf and human parents: human curiosity, inventiveness, and ambition tempered by the refined senses, love of nature, and artistic tastes of the elves.\n\x1B[0m')
    print('Half-elves are naturally charismatic and versatile, they have the same resistance to charms and darkvision as their elven parent and the fast-learner pace of humans. Every half-elf gets +2 Charisma and can choose where to put both of their +1 bonuses, as long as they are all unique.\n')
    print('While half-elves have theoretically the same amount of subraces as elves do, they only change the human versatility for a elven-learnt ability. If you decide to get a subrace, choose one ability from the elves (such as drow magic or Sun elf combat proficiency) and replace the human versatility with it.\n')

  if a == 4: #Half-Orc
    print('\x1B[3mMost Half-orcs become adventurers, to achieve greatness for their mighty deeds and notoriety for their barbaric customs and savage fury.\n\x1B[0m')
    print('Half-orcs look and act more like orcs than humans but make it up with the sheer stubborness they inherit from humans. Half-orcs are scary and hit hard, but they are \"too stubborn to die\" which enemies despise. Every half-orc gets +2 Strength and +1 Constitution.\n')
    print('Half-orcs don\'t have subraces.')
  
  if a == 5: #Halfling
    print('\x1B[3mThough some halflings live out their days in remote agricultural communities, others form nomadic bands that travel constantly, lured by the open road and the wide horizon to discover the wonders of new lands and peoples.\x1B[0m')
    print('Halflings are small, nimble and brave, and they love adventure as much as they love comfort. Halflings are naturally lucky and do not cower with fear. Every halfling gets +2 Dexterity.')
    print('\033[1mHalflings have 3 subraces:\033[0m\nGhostwise halflings are the rarest of them all, from remote lands and distrustiful of others, their ancestral lineage gives them a silent form of speech, basically telepathical. They get +1 Wisdom.')
    print('Lightfoot halflings hide easily, hiding even behind bigger people if needed, and it might be needed. They have +1 Charisma.')
    print('Stout halflings are hardier than average and have a good natural defense against poison. They have +1 Constitution.')

  if a == 6: #Humans
   print('\x1B[3mhumans are the youngest of the common races, late to arrive on the world scene and short-lived in comparison to gnomes, elves, and dragons.\x1B[0m')
   print('Humans are a baseline race, short-living and thus adaptable although sometimes reckless. That\'s expressed in their \"all-around bonus\" in stats. Every human gets +1 to all their stats.') 
   print('Humans don\'t have subraces.')
  
  if a == 7: #Tiefling
    print('\x1B[3mTo be greeted with stares and whispers, to suffer violence and insult on the street, to see mistrust and fear in every eye: this is the lot of the tiefling. And to twist the knife, tieflings know that this is because of a hellish pact struck many generations ago.\x1B[0m')
    print('Tieflings may look devilish but that doesn\'t stop their charming nature, the pact is almost forgotten but their effects are clearly seen. Tieflings can easily see in darkness and are strong agaisnt fire, and depending on who the pact was struck with they may get spells or otherwise useful abilities. Every tiefling gets +1 Intelligence.\n')
    print('\033[1mTieflings have 4 standard subraces:\033[0m\nAsmodeus tieflings are the most common, they get spells such as Thaumaturgy and Hellish Rebuke, intellect and fire. They get +2 Charisma or Dexterity.\n')
    print('Baalzebul is the embodiment of corruption and so are their tiefings, they learn Thaumaturgy and Ray of Sickness, making evil worse and morals falter. They also get +2 Charisma.\n')
    print('Mammon is greedy and influenced his tieflings this way, they\'re expert in gathering wealth, so they learn Mage Hand and Floating Disk. They also get +2 Charisma.\n')
    print('Mephistopheles tieflings are attracted to the arcane, desiring magical power above all. They learn Mage Hand and Burning Hands. They also get +2 Charisma or Dexterity.\n')
    print('Some tieflings didn\'t get their usual pact, these are called Variants, there are 2 Variant Tieflings:\n Devil\'s Tongue get, as the the name suggest, sharp and enthralling communication skills. They learn Vicious Mockery and Charm Person. They also get +2 Charisma or Dexterity.\n')
    print('Winged tieflings are also as the name suggests, they get wings instead of magic, giving them superior mobility as long as they don\'t wear heavy armor. They also get +2 Charisma or Dexterity.\n')
  
  if a == 8: #Triton
    print('\x1B[3mTritons guard the ocean depths, building small settlements beside deep trenches, portals to the elemental planes, and other dangerous spots far from the eyes of land-bound folk.\n \x1B[0m')
    print('Triton are the aquatic and amphibious folk,fully adept to the cold, darl and deep waters, they venture from. They have elemental spells such as Fog Cloud and Gust of Wind, and can talk to aquatic beasts. Every triton gets +1 Strength, Constitution and Charisma.\n')   
  if a == 9: #tabaxi, maybe idk
    print('\x1B[3mHailing from a strange and distant land, wandering tabaxi are catlike humanoids driven by curiosity.\n \x1B[0m')
    print('Tabaxi are the agile feline humanoids from lands far too distant. With sharp claws they attack and climb, versatile in every way. Every tabaxi gets +2 Dexterity, and +1 Charisma.\n')  

  if a == 10 or a == 11:
    print('\x1B[3mCustomization is key when you want to try wacky combos.\n \x1B[0m')
    print('Every customized race is diferent from stats and skills to names, and with these tools you can customize a existing race as you wish.\n') 

  else:
    print('Invalid option.')   
  br()

def racefinder(P1, a):
  i = int(0)
  if a == 1: #Elf / done
    print('Elf! Choose a subrace:')
    P1.Race.MainBuff = 'Dex'
    P1.Skills.append('Perception')
    P1.Extras['Race'] = {'Fey Ancestry': ['Fey Ancestry']}    

    print('1- Drow\n2- Eladrin\n3- High Elf\n4- Sea Elf\n5- Shadar-kai\n6- Wood Elf\n')
    temp = int(input())
    if temp == (1 or 2):
      P1.Race.MinorBuff = ['Cha']
    if temp == (4 or 5):
      P1.Race.MinorBuff = ['Con']  
    if temp == 3: #high elf done
      P1.Race.Name = 'High Elf'
      P1.Race.MinorBuff = ['Int']
      spellchooser(P1, 0, 'wizard')
      languagechooser(P1, 1)
    if temp == 6: #wood elf done
      P1.Race.Name = 'Wood Elf'    
      P1.Race.MinorBuff = ['Wis'] 
      setspeed(P1, 35)
    if temp == 5: #shadar-kai done
      P1.Race.Name = 'Shadar-kai' 
      P1.Typing.update({'necrotic':'resistant'})
    if temp == (3 or 6):
      b = ['longsword', 'shortsword', 'shortbow', 'longbow']
      P1.WeaponProf.append(b)
    if temp == 1: #drow done
      P1.Race.Name = 'Drow' 
      b = [ 'rapier', 'shortsword', 'hand crossbow']
      P1.WeaponProf.append(b)
      spellchooser(P1, spellname = 'dancing lights')
      spellchooser(P1, spellname = 'faerie fire')      
    if temp == 4: #sea elf done
      P1.Race.Name = 'Sea Elf' 
      b = ['spear', 'trident', 'light crossbow', 'net']
      P1.WeaponProf.append(b)
      setspeed(P1, 30, typ = 'swim')
      languagechooser(P1, name = 'Aquan')
    if temp == 2: #eladrin done
      P1.Race.Name = 'Eladrin' 
      spellchooser(P1, spellname = 'misty step')

  
  if a == 2: #Gnome / done
    print('Gnome! Choose a subrace:')
    P1.Race.MainBuff = 'Int'
    setspeed(P1, 25)
    P1.Extras['Racial'] = {'Gnome Cunning':['enabled']}
    P1.Size = 'Small'

    print('1-Deep Gnome/Svirfneblin\n2- Forest Gnome\n3- Rock Gnome')
    temp = int(input())
    if temp == 1: #Svirfneblin not done
      P1.Race.Name = 'Svirfneblin'
      P1.Race.MinorBuff = ['Dex']
      P1.Extras['Racial'].update({'Stone Camouflage': ['enabled']})

    if temp == 2: #forest not done
      P1.Race.Name = 'Forest Gnome'
      P1.Race.MinorBuff = ['Dex']
      spellchooser(P1, spellname = 'minor illusion', stat = 'Int', source = 'Race')

    if temp == 3: #rock not done
      P1.Race.Name = 'Rock Gnome'
      P1.Race.MinorBuff = ['Con']        
  
  if a == 3: #Half-elf /not done don't care, use base h-elf
    print('Half-elves are the best!')
    P1.Help.append('Fey Ancestry')

    print('Choose 2 different stats:')
    print('1- Str\n2- Dex\n3- Con\n4- Int\n5- Wis')
    P1.Race.MainBuff = 'Cha'
    temp = int(input())
    P1.Race.MinorBuff = [NtN(temp-1)]
    temp = int(input())
    P1.Race.MinorBuff.append(NtN(temp-1))

    #print('Will you choose a subrace?')
    while True:
      #temp = input('yes/no: ')
      if True: #temp.lower() in 'no' or
        P1.Skills.append(skillchooser(P1, 2))
        break
      elif temp.lower() in 'yes':
        print('Which will it be?')
        print('1- Drow\n2- Eladrin\n3- High Elf\n4- Sea Elf\n5- Shadar-kai\n6- Wood Elf\n')
        temp = int(input())
        if 0 < temp <= 6:
          print('Sorry, subraces are not implemented.')
          break
      else:
        print('Choose a valid option.')

  
  if a == 4: #Half-orc / done
    print('Half-orc it is!')
    P1.Race.Name = 'Half-Orc'
    P1.Race.MainBuff = 'Str'
    P1.Race.MinorBuff = ['Con']
    P1.Skills.append('Intimidation')
    P1.Extras['Racial'] = {'Savage': ['Savage', 1], 'Relentless': ['Relentless']}

  
  if a == 5: #Halfling
    print('Halfling! Choose a subrace:')

  
  if a == 6: #Human / done
    print('Human it is!')
    P1.Race.MinorBuff = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']
  
  if a == 8: #Tielfing 
    print('Tiefling! Choose a subrace:')
    P1.Typing['Resistance'].append('Fire')
    
  if a == 9: #Triton 
    print('Triton it is!')
    P1.Race.Name = 'Triton'
    P1.Race.MainBuff = 'none'
    P1.Race.MinorBuff = ['Str', 'Cha', 'Con']
    setspeed(P1, 30, typ = 'swim')
    spellchooser(P1, spellname = 'Fog Cloud', source = 'Race')
    spellchooser(P1, spellname = 'Gust of Wind', source = 'Race')

  if a == 7: #TABAXI BITCH / done
    print('Tabaxi it is!')
    P1.Race.Name = 'Tabaxi'
    P1.Race.MainBuff = 'Dex'
    P1.Race.MinorBuff = ['Cha']
    setspeed(P1, 20, typ = 'climb')
    P1.Skills.append(['Perception', 'Stealth'])
    P1.Race.Atk[0].Name = 'Claws'
    P1.Race.Atk[0].AtkType = 'Str'
    P1.Race.Atk[0].DmgDie = 4
    P1.Race.Atk[0].DmgType = 'slashing'

  if a == 10: #custom 3x+1
    print('Customizing...')
    P1.Race.Name = input('Please inform the name of the race: ').title()
    print('Choose 3 unique stats:')
    for i in range(6):
      print('{}- '.format(i+1), NtN(i))
    while i < 3:
      temp = NtN(int(input())-1)
      if temp in P1.Race.MinorBuff:
        print('You cannot choose this option again.')
      else:
        P1.Race.MinorBuf.append(temp)
        i = i+1
    skillchooser(P1, 2)
    spellchooser(P1, qtd = 1, spelllevel = 0)
        
  if a == 11: #custom +2 +1
    print('Customizing...')
    P1.Race.Name = input('Please inform the name of the race: ').title()
    print('Stats:')
    for i in range(6):
      print('{}- '.format(i+1), NtN(i))
    P1.Race.MainBuff = NtN( int(input('(+2) Choose 1 stat: ')) -1)
    temp = NtN( int(input('(+1) Choose 1 stat: ')) -1)
    while i < 5:
      if temp == P1.Race.MainBuff:
        print('You cannot choose this option again.')
        temp = NtN( int(input('Choose another stat: ')) -1)
      else:
        P1.Race.MinorBuff = [temp]
        break
      skillchooser(P1, 2)
      spellchooser(P1, qtd = 1, spelllevel = 0)
    

def welcometoleagueofdraven(P1, chosen = -1):
  temp = ['Life Cleric', 'Champion Fighter', 'Assassin Rogue', 'Draconic Sorcerer']
    
  if chosen == -1:
    print('Choose your class. You\'ll start at level 3. You cannot choose subclass.')
    for i in range(len(temp)):
      print(i+1, '-', temp[i])
    a = int(input())
  else:
    a = chosen

  #CLERIC
  if a == 1: 
    print('\x1B[3mClerics are intermediaries between the mortal world and the distant planes of the gods.\x1B[0m\n')
    P1.Class.Saves = ['Wis', 'Cha']
    P1.Class.Caster = 'Wis'
    b = ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion']
    skillchooser(P1, 2, given = b)
    b = ['simple', 'light', 'medium']
    profgiver(P1, b, 'shield')
    P1.WeaponProf = list(get_all_values(P1.WeaponProf))
    P1.ArmorProf = list(get_all_values(P1.ArmorProf))
    print('Choose between:')
    if 'warhammer' in P1.WeaponProf:
      print('(1)A mace OR (2)a warhammer')
      a = int(input('1|2: '))
      if a == 2:
        P1.Inv['Equipped'].append('warhammer')
    elif a == 1 or 'warhammer' not in P1.WeaponProf:
      P1.Inv['Equipped'].append('mace')
    if 'chain mail' in P1.ArmorProf:
      print('(1)Scale mail, (2)leather armor OR (3)chain mail')
      a = int(input('1|2|3: '))
      if a == 3:
        P1.Inv['Carried'].append('chain mail')
        P1.AC = 16
    else:
      print('(1)Scale mail OR (2)leather armor')
      a = int(input('1|2: '))
    if a == 1:
      P1.Inv['Carried'].append('scale mail')
      if mod(P1.Stats[NtN('Dex')]) > 2:
        P1.AC = 16
      elif mod(P1.Stats[NtN('Dex')]) >= 0:
        P1.AC = 14 + mod(P1.Stats[NtN('Dex')])
      else:
        P1.AC = 14
    if a == 2:
      P1.Inv['Carried'].append('leather armor')
      if mod(P1.Stats[NtN('Dex')]) >= 0:
        P1.AC = 11 + mod(P1.Stats[NtN('Dex')])
      else:
        P1.AC = 11
    #classfeats
    P1.Extras['Class'] = {'Channel Divinity': ['Turn Undead/Preserve Life', [1, 1, 'rest']], 'Disciple of Life': ['Disciple of Life']}
    
  #ROGUE
  if a == 3: 
    print('\x1B[3mRogues rely on skill, stealth, and their foes\' vulnerabilities to get the upper hand in any situation.\n\x1B[0m')
    P1.Class.Name = temp[2]
    P1.Class.Saves = ['Dex', 'Int']
    b = ['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth']
    skillchooser(P1, 4, given = b)
    b = ['simple', 'light']
    profgiver(P1, b)
    b = ['hand crossbow', 'longsword', 'rapier', 'shortsword']
    P1.WeaponProf.append(b)
    P1.WeaponProf = list(get_all_values(P1.WeaponProf))
    P1.ArmorProf = list(get_all_values(P1.ArmorProf))
    P1.WeaponProf.sort()
    P1.ArmorProf.sort()
    #inv    
    print('(1)A rapier OR (2)a shortsword')
    temp = ['rapier', 'shortsword']
    a = int(input('1|2: '))
    P1.Inv['Equipped'].append(temp[a-1])
    print('(1)A shortbow and 20 arrows OR (2)a shortsword')
    temp = ['shortbow', 'shortsword']
    a = int(input('1|2: '))
    P1.Inv['Equipped'].append(temp[a-1])
    print('You also get leather armor, and 2 daggers.')
    temp = ['dagger', 'dagger']
    P1.AC = 11 + mod(P1.Stats[NtN('Dex')])
    P1.Inv['Equipped'].append(temp)
    P1.Inv['Equipped'] = list(get_all_values(P1.Inv['Equipped']))
    P1.Inv['Equipped'].sort()
    #classfeats
    P1.Extras['Class'] = {'Sneak Attack': ['Sneak Attack', [1, 1, 'round']], 'Assassinate': ['Assassinate'], 'Cunning Action': ['Cunning Action', 'bonus']}

  #FIGHTER
  if a == 2: 
    print('\x1B[3mFigthers share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat.\n\x1B[0m')
    P1.Class.Name = temp[1]
    P1.Class.HitDie = 10
    P1.Class.Saves = ['Dex', 'Con']
    b = ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival.']
    skillchooser(P1, 2, given = b)
    b = ['simple', 'martial', 'light', 'medium', 'heavy']
    profgiver(P1, b, 'shield')
    P1.WeaponProf = list(get_all_values(P1.WeaponProf))
    P1.ArmorProf = list(get_all_values(P1.ArmorProf))
    #inv
    print('Choose between:')
    print('(1)Chain mail OR (2)leather armor, longbow and 20 arrows')
    a = int(input('1|2: '))
    if a == 1:
      P1.Inv['Carried'].append('chain mail')
      P1.AC = 16
    if a == 2:
      P1.Inv['Carried'].append('leather armor')
      P1.AC = 11 + mod(P1.Stats[NtN('Dex')])
      P1.Inv['Equipped'].append('longbow')   
    print('(1)A martial weapon and a shield OR (2) 2 martial weapons')
    a = int(input('1|2: '))
    if a == 1:
      temp = input('Equip shield? y/n: ')
      if temp.lower() in 'yes':
        P1.Inv['Carried'].append('shield')
        P1.AC = P1.AC + 2
      else:
        P1.Inv['Removed'].append('shield')      
    weaponchooser(P1, a, 'martial') 
    print('(1)A light crossbow OR (2) 2 handaxes')
    a = int(input('1|2: '))
    if a == 1:
      P1.Inv['Equipped'].append('light crossbow')
    if a == 2:
      temp = ['handaxe', 'handaxe']
      P1.Inv['Equipped'].append(temp)
    P1.Inv['Equipped'] = list(get_all_values(P1.Inv['Equipped']))
    P1.Inv['Equipped'].sort()
    #classfeats
    P1.Extras['Class'] = {'Second Wind': ['Second Wind', [1, 'rest'], 'bonus'], 'Action Surge': ['Action Surge', [1, 'rest']], 'Improved Critical': ['Improved Critical']}
    fschooser(P1)

  #SORCERER
  if a == 4: 
    print('\x1B[3mOne can\'t study sorcery as one learns a language, any more than one can learn to live a legendary life. \x1B[0m\n')
    P1.Class.Name = temp[3]
    P1.Class.HitDie = 6
    P1.Class.Saves = ['Con', 'Cha']
    P1.Class.Caster = 'Cha'
    b = ['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion']
    skillchooser(P1, 2, given = b)
    P1.WeaponProf.remove('None')
    P1.WeaponProf.append('dagger', 'dart', 'sling', 'quarterstaff', 'light crossbow')
    #inv
    print('Choose between:')
    print('(1)A light crossbow and 20 bolts OR (2) any simple weapon')
    a = int(input('1|2: '))
    if a == 1:
      P1.Inv['Equipped'].append('light crossbow')
    if a == 2:
      weaponchooser(P1, 1, 'simple')
    P1.Inv['Equipped'].append(['dagger', 'dagger'])
    #classfeats
    P1.AC = 13 + mod(P1.Stats[1])
    P1.Extras['Class'] = {'Font of Magic': ['Font of Magic', [3, 3, 'rest'], 'bonus'], 'Metamagic': ([], [])}

  #all classes stuff
  weaponchooser(P1, mode = 'update')

def profgiver(P1, a, b = 'none'):
  temp = []
  temp.clear()
  #weapons
  if a.count('simple') > 0:
    if b.count('melee') > 0:
      temp.append(['club', 'dagger',  'greatclub', 'handaxe', 'javelin', 'light hammer', 'mace', 'quarterstaff', 'sickle', 'spear', 'staff'])
    if b.count('ranged') > 0:
      temp.append(['dart',	'light crossbow', 'shortbow', 'sling'])
    else:
      temp.append(['club', 'dagger', 'dart', 'greatclub', 'handaxe', 'javelin', 'light crossbow', 'light hammer', 'mace', 'quarterstaff', 'shortbow', 'sickle', 'sling', 'spear', 'staff'])
  
  if a.count('martial') > 0:
    if b.count('melee') > 0:
      temp.append(['battleaxe', 'flail', 'glaive', 'greataxe', 'greatsword', 'halberd', 'lance', 'longsword', 'maul', 'morningstar', 'pike', 'rapier', 'scimitar', 'shortsword', 'trident', 'war pick', 'warhammer', 'whip'])
    if b.count('ranged') > 0:
      temp.append(['blowgun', 'hand crossbow', 'heavy crossbow',  'longbow', 'net'])
    else:
        temp.append(['battleaxe', 'blowgun', 'flail', 'glaive', 'greataxe', 'greatsword', 'halberd', 'hand crossbow', 'heavy crossbow', 'lance', 'longbow', 'longsword', 'maul', 'morningstar', 'net', 'pike', 'rapier', 'scimitar', 'shortsword', 'trident', 'war pick', 'warhammer', 'whip'])
  for i in range(len(P1.WeaponProf)): #this is my beloved
    if P1.WeaponProf[i] in temp:
      temp.remove(P1.WeaponProf[i])
  P1.WeaponProf.remove('None')
  temp.sort()
  P1.WeaponProf.extend(temp)
    #armor
  temp.clear()
  if a.count('light') > 0:
      temp.append(['leather armor', 'padded armor', 'studded leather armor'])
  if a.count('medium') > 0:
      temp.append(['breastplate', 'chain shirt', 'half plate', 'hide armor', 'scale mail'])
  if a.count('heavy') > 0:
      temp.append(['chain mail', 'plate armor', 'ring mail', 'splint armor'])
  for i in range(len(P1.ArmorProf)): #look! it's them again
    if P1.ArmorProf[i] in temp:
      temp.remove(P1.ArmorProf[i])
  if P1.ArmorProf[0] == 'None':
    P1.ArmorProf.remove('None')
  temp.sort()
  P1.ArmorProf.append(temp)
  if b.count('shield') > 0:
    P1.ArmorProf.append('shields')
    
  
def skillchooser(P1, qtd, mode = 'standard', given = []): #FUCKING DONE HELP
  if len(P1.Skills) == 18 or qtd == 0: #major pre-error test, saves CPU
    print('You have no more skills to choose.')
    return

  List = {'Str':'Athletics', 'Dex': ['Acrobatics', 'Sleight of Hand', 'Stealth'], 'Int': ['Arcana', 'History', 'Investigation', 'Nature', 'Religion'], 'Wis': ['Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival'], 'Cha': ['Deception', 'Intimidation', 'Performance', 'Persuasion']}
  if bool(given) == False:  
    temp = list(get_all_values(List))
  else:
    temp = given

  if type(temp) == dict: #The Binding of Isaac: Repentance
      for i in range (len(P1.Skills)):
        for key in List:
         for items in List[key]:
           if P1.Skills[i] == items:
               temp.remove(P1.Skills[i])

  elif type(temp) == list: #The Binding of Isaac: Rebirth
    for i in range(len(P1.Skills)):
      if P1.Skills[i] in temp:
        temp.remove(P1.Skills[i])
      
  #the checks
  if bool(temp) == False: #temp is empty
      return skillchooser(P1, qtd) #gives the whole list of skills to choose from
  if len(temp) < qtd: #temp too small
    qtd = qtd - len(temp) 
    P1.Skills.append(temp) #adds all it can
    return skillchooser(P1, qtd) #gives the whole list for what it can't

  if qtd > 1: #GRAMMAR
    print('Choose {} skills from the following list:' .format(qtd))
  elif qtd == 1:
    print('Choose a skill from the following list:')

  temp.sort()
  temp.sort() #AESTHETICS
  for i in range(len(temp)):
    print('{}: ' .format(i+1), temp[i])
    
  for i in range(qtd):
    a = int(input())
    P1.Skills.append(temp[a-1])    
  
def languagechooser(P1, qtd = 0, typ = 'none', given = []):
  pass
  List:{'Standard': ['Common', 'Elven', 'Dwarven', 'Orcish', 'Gnomish','Giant', 'Halfling', 'Goblin'], 'Exotic': ['Abyssal', 'Infernal', 'Deep Speech', 'Celestial', 'Draconic', 'Sylvan', 'Primordial', 'Undercommon']}
  List['Standard'].sort()
  List['Exotic'].sort()
  if bool(given) == False:
    temp = list(get_all_values(List))
  if typ == 'Exotic':
    temp = List[typ]
  if typ == 'Standard':
    temp = List[Standard]

  #the checks
  if bool(temp) == False: #temp is empty
      return languagechooser(P1, qtd) #gives the whole list of languages to choose from
  if len(temp) < qtd: #temp too small
    qtd = qtd - len(temp) 
    P1.Skills.append(temp) 
    #adds all it can
    return languagechooser(P1, qtd) 
    #gives the whole list for what it can't

  if qtd > 1: #GRAMMAR
    print('Choose {} languages from the following list:' .format(qtd))
  elif qtd == 1:
    print('Choose a language from the following list:')

  temp.sort()
  temp.sort() #AESTHETICS
  for i in range(len(temp)):
    print('{}: ' .format(i+1), temp[i])
    
  for i in range(qtd):
    a = int(input())
    P1.Skills.append(temp[a-1])    

def fschooser(P1):
  print('Fighting style')
  L = ['archery', 'defense', 'dueling', 'great weapon fighting', 'two-weapon fighting']
  if 'Class' in P1.Extras:
    if 'Fighting Style' in P1.Extras['Class']:
      a = 1
      for i in range(len(P1.Extras['Class']['Fighting Style'])):
        L.remove(P1.Extras['Class']['Fighting Style'][i])

  for i in range(len(L)):
    print(i+1, '-', L[i])
  if a == 1:
    P1.Extras['Class']['Fighting Style'].append(L[int(input('Choose a fighting style: ')) - 1])
  else:
    P1.Extras['Class']= {'Fighting Style': [L[int(input('Choose a fighting style: ')) - 1]]}
  
def metamagic(P1, qtd, Target, spellchoice = 'none', metachoice = 'none', source = 'Class', mode = 'choose', action = 'action', round = 1):
  if mode == 'choose':
    metaknight = [('Empowered', 'When you roll damage for a spell, you can spend 1 sorcery point to reroll a number of the damage dice up to your Charisma modifier.'), ('Heightened', 'When you cast a spell that forces a creature to make a saving throw to resist its effects, you can give one target of the spell disadvantage on its saving throw.'), ('Quickened', 'When you cast a spell that has a casting time of 1 action, you can spend 2 sorcery points to change the casting time to 1 bonus action for this casting.'), ('Twinned', 'When you cast a spell that targets only one creature and doesn\'t have a range of self, you can spend a number of sorcery points equal to the spell\'s level to target a second creature in range with the same spell (min 1 sorcery point).')]
    for i in range(len(metaknight)):
      print(i + 1, '-', metaknight[i][0], 'spell:\n' + metaknight[i][1])
    if qtd == 1:
      a = [int(input('Choose a metamagic option: ')) - 1]
    else:
      print('Choose {} metamagic options: '. format(qtd))
      a = []
      for i in range(qtd):
        a.append(int(input()) - 1)
    if 'Metamagic' not in P1.Extras[source]:
      P1.Extras[source]['Metamagic'] = []
    for i in range(len(a)):
      if a[i] == 2:
        temp = [metknight[a[i]], 'bonus']
      else:
        temp = [metaknight[a[i]]]        
      P1.Extras[source]['Metamagic'].append(temp)
      del temp

  elif mode == 'use':
    if metachoice == 'none' and P1.Class.Name == 'Sorcerer':
      a = input('Use metamagic? ')
      if a.lower in 'yes':
        for i in range(len(P1.Extras['Class']['Metamagic'])):
          if P1.Extras['Class']['Font of Magic'][1][0] >= 1 and P1.Extras['Class']['Metamagic'][i][0] == 'Empowered':
            P1.Extras['Class']['Font of Magic'][1][0] = P1.Extras['Class']['Font of Magic'][1][0] - 1
            pass
            
          elif P1.Extras['Class']['Font of Magic'][1][0] >= 2 and (P1.Extras['Class']['Metamagic'][i][0] == 'Quickened' and action == 'bonus'):
            if spellchoice != 'none':
              DoSpell(P1, Target, spellchoice, 'action', round)
            else:
              DoSpell(P1, Target, 'action', round)
            P1.done[round]['bonus'] = P1.done[round]['action']
            P1.done[round]['bonus'].append(['metamagic', 'quickened'])
            P1.Extras['Class']['Font of Magic'][1][0] = P1.Extras['Class']['Font of Magic'][1][0] - 2
            del P1.done[round]['action']
            
          elif P1.Extras['Class']['Font of Magic'][1][0] >= 3 and P1.Extras['Class']['Metamagic'][i][0] == 'Heightened':
            P1.Extras['Class']['Font of Magic'][1][0] = P1.Extras['Class']['Font of Magic'][1][0] - 3
            pass
            
          elif P1.Extras['Class']['Font of Magic'][1][0] > 0 and P1.Extras['Class']['Metamagic'][i][0] == 'Twinned':
            P1.Extras['Class']['Font of Magic'][1][0] = P1.Extras['Class']['Font of Magic'][1][0] - math.max(1, P1.Class.Spells[spellchoice].Level)
            pass
