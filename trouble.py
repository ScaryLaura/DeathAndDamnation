from pain import *
from misery import *
from theft import *

def weaponchooser(P1, qtd = 0, typ = 'none', mode = 'choose', ammo = 20):
  temp = []
  temp.clear()
  if mode == 'choose':
  #weapons
    List = {'simple': ['club', 'dagger', 'dart', 'greatclub', 'handaxe', 'javelin', 'light crossbow', 'light hammer', 'mace', 'quarterstaff', 'shortbow', 'sickle', 'sling', 'spear', 'staff'], 'martial': ['battleaxe', 'blowgun', 'flail', 'glaive', 'greataxe', 'greatsword', 'halberd', 'hand crossbow', 'heavy crossbow', 'lance', 'longbow', 'longsword', 'maul', 'morningstar', 'net', 'pike', 'rapier', 'scimitar', 'shortsword', 'trident', 'war pick', 'warhammer', 'whip']}

    if typ != 'none':
      temp = List[typ]
    else:
      temp = list(get_all_values(List))

    a = list(get_all_values(P1.Inv))
    for i in range(len(a)):
      if a[i] in temp:
        temp.remove(a[i])

    if qtd > 1:
      print('Choose {} weapons from the following list:' .format(qtd))
    if qtd == 1:
      print('Choose a weapon from the following list:')
      
    temp.sort()
    temp.sort() #AESTHETICS
    for i in range(len(temp)):
      print('{}: ' .format(i+1), temp[i])
    
    for i in range(qtd):
      a = int(input())
      P1.Inv['Equipped'].append(temp[a-1])

  elif mode == 'update':  
    
    List = {'Ammo': ['blowgun', 'light crossbow', 'handcrossbow','heavy crossbow', 'shortbow', 'sling', 'longbow'], 
            'Light': ['club','dagger','hand crossbow', 'handaxe','light hammer', 'scmitar', 'shortsword', 'sickle'], 
            'TwoHanded': ['glaive', 'greataxe','greatclub', 'greatsword', 'halberd', 'heavy crossbow', 'light crossbow', 'longbow', 'maul', 'pike', 'shortbow'], 
            'Versatile': ['battleaxe', 'longsword', 'quarterstaff', 'spear', 'staff', 'trident', 'warhammer'], 
            'Finesse': ['dagger', 'dart', 'rapier', 'scimitar', 'shortsword', 'whip']}
    DmgType = {'bludgeoning': ['club', 'flail', 'greatclub', 'light hammer', 'mace', 'maul', 'quarterstaff', 'sling', 'staff', 'warhammer'], 'piercing': ['blowgun', 'dagger', 'dart', 'hand crossbow', 'heavy crossbow', 'javelin', 'lance', 'light crossbow', 'longbow', 'morningstar', 'pike'], 'slashing': ['battleaxe', 'glaive', 'greataxe', 'greatsword', 'halberd', 'handaxe', 'longsword', 'scimitar', 'shortsword']}
    DmgDie = { 1: 'blowgun', 4: ['club', 'dagger', 'dart', 'light hammer', 'sickle', 'sling', 'whip'], 6: ['hand crossbow', 'handaxe', 'javelin', 'mace', 'quarterstaff', 'scimiter', 'shortbow', 'spear', 'staff', 'trident', 'shortsword'], 8: ['battleaxe', 'flail', 'greatclub', 'light crossbow', 'longbow', 'longsword', 'morningstar', 'rapier', 'war pick', 'warhammer'], 10: ['glaive', 'halberd', 'heavy crossbow', 'pike'], 12: ['greataxe', 'lance'], '2d6': ['greatsword', 'maul']}

    a = list(get_all_values(P1.Inv['Equipped']))
    P1.Inv['Equipped'].clear()
    kek = 'none'
    for i in range(len(a)):
      temp = Weapon()
      if a[i] == 'shield':
        kek = 'shield'
      else:
        temp.Name = a[i].lower()
        if temp.Name in List['Light']:
          temp.Light = 'yes'
        if temp.Name in List['Ammo']:
          temp.Ammo = ammo
          temp.Stat = 'Dex'
        if temp.Name in List['TwoHanded']:
          temp.TwoHanded = 'yes'
        if temp.Name in List['Versatile']:
          temp.TwoHanded = 'versatile'
        if temp.Name in List['Finesse']:
          temp.Stat = 'finesse'
        if ammo != 20:
          temp.ammo = ammo
      #damage type
      for key in DmgType:
        if temp.Name.lower() in DmgType[key]:
          temp.DmgType = key

      #damage die
      for key in DmgDie:
        if temp.Name.lower() in DmgDie[key]:
          temp.DmgDie = key
      
      P1.Inv['Equipped'].append(temp)
      del temp
      
    if kek == 'shield':
      P1.Inv['Equipped'].append(kek)

    
