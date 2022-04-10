import random
import math
from misery import *
from theft import *
from trouble import *

def d(x):  #im lazy
  if type(x) == int: 
    a = random.randint(1, x)
  elif type(x) == str:
    a = 0
    b = x.split(sep = 'd')
    for i in range(int(b[0])):
      a = a + random.randint(1, int(b[1]))
    
  return int(a)

def mod(x):  #very lazy
    return int(math.floor(x / 2) - 5)

def NtN(x):
    lel = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha', 'none']

    if type(x) == str:
        a = int(lel.index(x))
    elif type(x) == int:
        a = str(lel[x])
    
    return a

def br():  #damn i'm lazy lazy
    print('--------------------------------------')

def stat():  #classic 4d6kh3|dl1
    a = [d(6), d(6), d(6), d(6)]
    i = tot = int(0)
    y = int(6)
    for i in range(4):
        if (y > a[i]):
            y = a[i]
    tot = sum(a) - y
    return int(tot)
  
def statpain(Player): #this is pain
	statarray= [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
	for i in range(3):
		for j in range (6):
			statarray[i][j] = stat()
	
	print('You can choose between the Standard or any of the arrays below.')
	print('Standard:  - 15 - 14 - 13 - 12 - 10 - 8')
	for i in range (3):
		statarray[i].sort(reverse = True)
		print('Option {}: ' .format(i+1), *statarray[i], sep = " - ") 
	a = input('\'Standard\' or option: ')
	if a.lower() in 'standard' or a.lower() in 'std':
		temp = [15, 14, 13, 12, 10, 8]

	else:
		a = int(a)
		temp = statarray[a-1]
	
	print('You chose: ',  *temp, sep = " - ")
	print('Insert the values in the order you want.')
	i = int(0)
	while i < 6:
		a = int(input('{}: '.format( NtN(i) ) ) )
		if a in temp:
			Player.Stats[i] = a
			temp.remove(a)
			i = i+1
		else:
			print('This value is not available')

def update(P1):
  #stats
  if P1.Race.MainBuff.lower() != 'none':
    P1.Stats[NtN(P1.Race.MainBuff)] = 2 + P1.Stats[NtN(P1.Race.MainBuff)]
    P1.Race.Mainbuff = 'none'
  while bool(P1.Race.MinorBuff) == True:
    P1.Stats[NtN(P1.Race.MinorBuff[0])] = P1.Stats[NtN(P1.Race.MinorBuff[0])] + 1
    P1.Race.MinorBuff.remove(P1.Race.MinorBuff[0])

  P1.MaxHP = P1.HP = 2*P1.Class.HitDie + 3*mod(P1.Stats[NtN('Con')]) 
  weaponchooser(P1, mode = 'update')
  #sorting
  P1.Skills = list(get_all_values(P1.Skills))
  P1.Skills.sort()
  P1.WeaponProf = list(get_all_values(P1.WeaponProf))
  P1.WeaponProf.sort()
  P1.Class.Saves.sort()
  P1.ArmorProf = list(get_all_values(P1.ArmorProf))
  if P1.ArmorProf.count('Shields') == 0:
    P1.ArmorProf.sort()
  elif P1.ArmorProf.count('Shields') == 1:
    P1.ArmorProf[:len(P1.ArmorProf)].sort()

  if bool(P1.Inv['Carried']) == False:
    P1.AC = 10 + mod(P1.Stats[NtN('Dex')])
    
  if 'shield' in P1.Inv['Equipped']:
    P1.Inv['Equipped'].remove('shield')
    P1.Inv['Carried'].append('shield')
  P1.Inv['Equipped'].sort( key =lambda Weapon: Weapon.Name)

def testprints(P1):
  a = b = int(0)
  print('Printing out character sheet.\033[1m')
  print(P1.Name.title(),' | ', P1.Race.Name.title(), ' | ', P1.Class.Name.title(), ' Level 3\033[0m')
  if bool(P1.Inv['Carried']) == True:
    if 'shield' in P1.Inv['Carried']:
      print('Hit Points {} | AC {} ({}, Shield) '.format(P1.HP, P1.AC, P1.Inv['Carried'][0].title()))
    else:
      print('Hit Points {} | AC {} ({}) '.format(P1.HP, P1.AC, P1.Inv['Carried'][0].title()))
  else:
    print('Hit Points {} | AC {} '.format(P1.HP, P1.AC))
    
  print('')
 
  statlist = []
  modlist = []
  for i in range(len(P1.Stats)):
    if mod(P1.Stats[i]) > 0:
      b = str(P1.Stats[i])
      a = '+' + str(mod(P1.Stats[i]))
    elif mod(P1.Stats[i]) < 0:
      b = ' ' + str(P1.Stats[i])
      a = str(mod(P1.Stats[i]))
    else:
      b = str(P1.Stats[i])
      a = ' ' + str(0)
    statlist.append(b)
    modlist.append(a)
  print(*statlist, sep = ' | ')
  print(*modlist, sep = ' | ')
      
  if len(P1.Speed) > 1:
    print('\nSpeeds:')
    for key, value in P1.Speed.items():
      print('{}ft {}'.format(value, key.lower()))
  else:
    print('\nSpeed: {}ft {}'.format(next(iter(P1.Speed.values())), next(iter(P1.Speed.keys()))))
      
  a = 2 + mod(P1.Stats[NtN(P1.Class.Saves[0].title())])
  b = 2 + mod(P1.Stats[NtN(P1.Class.Saves[1].title())])
  print('\nSaving Throws: {} +{}, {} +{}'.format(P1.Class.Saves[0], a, P1.Class.Saves[1], b) )
  print('\033[1m\nSkills Proficiencies:\033[0m')
  P1.Skills = list(get_all_values(P1.Skills))
  P1.Skills.sort()
  print(*P1.Skills, sep = ', ')
  
  #P1.Inv['Equipped'][:len(P1.Inv['Equipped'])].sort(key =lambda Weapon: Weapon.Name)
  print('\n|Inventory|\nEquipped:')
  for i in range(len(P1.Inv['Equipped'])):
    if P1.Inv['Equipped'][i].Stat == 'finesse':
      if P1.Stats[1] >= P1.Stats[0]:
        a = mod(P1.Stats[1])
      else:
        a = mod(P1.Stats[0])
    else:
      a = mod(P1.Stats[NtN(P1.Inv['Equipped'][i].Stat)])
    
        
    if type(P1.Inv['Equipped'][i].DmgDie) == int:
      print('{} | +{} | 1d{}+{}'.format (P1.Inv['Equipped'][i].Name.title(), a+2, P1.Inv['Equipped'][i].DmgDie, a))
    else:
      print('{} | +{} | {}+{}'.format (P1.Inv['Equipped'][i].Name.title(), mod(P1.Stats[NtN(P1.Inv['Equipped'][i].Stat)])+2, P1.Inv['Equipped'][i].DmgDie, a))

  if len(P1.Inv['Carried']) > 0:
    print('\nCarried')
    for i in range(len(P1.Inv['Carried'])):
      print(P1.Inv['Carried'][i].title())
  '''
  print('\033[1m\nWeapon Proficiencies:\033[0m') 
  print(*P1.WeaponProf, sep = ', ')
  print('\033[1m\nArmor Proficiencies:\033[0m')
  print(*P1.ArmorProf, sep = ', ')
  '''

def status(Y, show = 'no'):
  b = ''
  if show != 'no':
    b = ' - ' + str(Y.HP) + '/' + str(Y.MaxHP)
  #Healthy/Wounded/Bloodied
  if Y.HP >=  3 * Y.MaxHP / 4:
    print('<' + color.GREEN + 'Healthy' + b + color.END + '>')
  elif Y.HP >=  Y.MaxHP / 2:
    print('<' + color.YELLOW + 'Wounded' + b +  color.END + '>')
  elif Y.HP >=  Y.MaxHP / 4:
    print('<' + color.RED + 'Bloodied' + b +  color.END + '>')
  else:
    print('<' + color.RED + 'Critical' + b +  color.END + '>')
    
def setspeed(P1, qtd, do = 'set', typ = 'walk'):
  if do == 'set':
    if typ in P1.Speed.keys():
      P1.Speed[typ] = qtd
    else:
      a = {typ: qtd}
      P1.Speed.update(a)
  elif do == 'add':
    P1.Speed[typ] = P1.Speed[typ] + qtd

def initmaker(MonsterA, MonsterB, Player):
    init = []
    a = d(20)
    MonsterA.init = a + mod(MonsterA.Stats[1])
    print(MonsterA.Name, 'rolled: ', a, ' + ', mod(MonsterA.Stats[1]), ' = ',
          MonsterA.init)
    a = d(20)
    MonsterB.init = a + mod(MonsterA.Stats[1])
    print(MonsterB.Name, 'rolled: ', a, ' + ', mod(MonsterA.Stats[1]), ' = ',MonsterB.init)
    a = d(20)
    Player.init = a + mod(Player.Stats[NtN('Dex')])
    print(Player.Name, 'rolled: ', a, ' + ', mod(Player.Stats[NtN('Dex')]),' = ', Player.init)

    l = [(MonsterA.Name, MonsterA.init),
        (MonsterB.Name, MonsterB.init),
        (Player.Name, Player.init)]
  
    init = sorted(l, key= lambda tuple: tuple[1], reverse = True)

    return init

def adjacent(value):
  if value != 'A':
    pass

def DoMove(subject, arena, target = ('A', 1), round = 0, plan = 'approach'): #pain
  if type(subject) == Monster: 
    if plan == 'approach':
      if type(target) == tuple:
        temp = [target]
      else:
        temp = [target.Position]
      if subject.Position not in temp:
        move = math.floor(subject.Speed['Walk']/5)
        if distancebetween(subject.Position, temp[0]) > move:
          temp.append(adjacent(temp))
          temp = list(get_all_values(temp))
          for i in range(len(random.shuffle(temp))):
            if distancebetween(subject.Position, temp[i]) <= move:
              subject.Position = temp[i]
              i = 'done'
              break
          if i != 'done':
            a = 'eh'
            for i in range(len(temp)):
              del a
              a = [temp[i]]
              a.append(adjacent(temp[i]))
              a = list(get_all_values(a))
              for j in range(len(random.shuffle(temp))):
                if distancebetween(subject.Position, a[j]) <= move:
                  subject.Position = a[j]
                  j = 'done'
                  break
                  
  elif type(subject) == Player:
    pass

def DoDodge(subject, targets, round):
  #print('check dodge')
  #subject.done = {round: {'action': ['name'], 'effect': ['name', final round, 'start', 'Special', 'none', targets]}}
  if type(targets) != list:
    targets = [targets]
    
  for i in range(len(targets)):
    targets[i].Special = 'disadv'

  subject.done[round] = {'action': ['Dodge'], 'effect': ['Dodge', round+1, 'start', 'Special', 'none', targets]}
    

def DoAtk(Creature, Target, chosen = -1, mode = 'action', special = 'none', round = 1):

  if type(Creature) == Monster:
    x = len(Creature.Atk)
    i = d(x)-1      
    for i in range(Creature.Atk[i].Multiattack):
      if Creature.Atk[i].Save == 'no' or type(Creature.Atk[i].Save) == int: #non save attacks
          a = d(20)
          if special != 'none':
            b = d(20)
            if b == a:
              pass
            elif (b > a and special == 'adv') or (b < a and special == 'disadv'):
              a = b       
          
          b = a + Creature.Atk[i].AtkBonus
          print(Creature.Name,'attacks {} with {}!'.format(Target.Name.title(), Creature.Atk[i].Name))
          if special != 'none':
            print('Rolled with {}antage!' .format(special))
          print( a, ' + ', Creature.Atk[i].AtkBonus, ' = ', b)
          if  b >= Target.AC:
            if a == 20:
              h = 'crit'
              print('Critical hit!')
              a = d(Creature.Atk[i].DmgDie) + d(Creature.Atk[i].DmgDie)
            elif a < 20:
              h = 'hit'
              print('Hit!')
              a = d(Creature.Atk[i].DmgDie)
            b = a + Creature.Atk[i].DmgBonus
            dmg = b
            if Creature.Atk[i].DmgType in list(get_all_values(Target.Typing)):
              if Creature.Atk[i].DmgType in Target.Typing['Resistance']:
                dmg = math.ceil(b /2)
              if Creature.Atk[i].DmgType in Target.Typing['Vulnerability']:
                dmg = b * 2
              if Creature.Atk[i].DmgType in Target.Typing['Immunity']:
                dmg = 0
            print('Dealing {} {} damage!'.format(dmg, Creature.Atk[i].DmgType))
            Target.HP = Target.HP - dmg
            if Creature.Atk[i].Save != 'no':
              if int(Creature.Atk[i].Save) > 0:
                print('Follow-up attack!')
                return DoAtk(Creature, Target, Creature.Atk[i].Save)
          else:
            h = 'miss'
            print('Miss!')
          
      elif type(NtN(Creature.Atk[i].Save)) == int: #save attacks
        print('{} makes an attack against {} with {}! {} makes a {} save, DC {}!' .format(Creature.Name, Target.Name, Creature.Atk[i].Name, Target.Name, Creature.Atk[i].Save, Creature.Atk[i].SaveDC))
        a = d(20)
        if NtN(Creature.Atk[i].Save) in Target.Class.Saves:
          b = a + 2 + mod(Target.Stats[NtN(Creature.Atk[i].Save)])
          print('Rolled {} + {} = {}' . format(a + mod(Target.Stats[NtN(Creature.Atk[i].Save)])+2, b))
        else:
          b = a + mod(Target.Stats[NtN(Creature.Atk[i].Save)])
          print('Rolled {} + {} = {}' . format(a, mod(Target.Stats[NtN(Creature.Atk[i].Save)]) , b))
        if b < Creature.Atk[i].SaveDC:
          print('Fail!')
          a = d(Creature.Atk[i].DmgDie)
          b = a + Creature.Atk[i].DmgBonus
          dmg = b
          if Creature.Atk[i].DmgType in list(get_all_values(Target.Typing)):
            if Creature.Atk[i].DmgType in Target.Typing['Resistance']:
              dmg = math.ceil(b /2)
            if Creature.Atk[i].DmgType in Target.Typing['Vulnerability']:
              dmg = b * 2
            if Creature.Atk[i].DmgType in Target.Typing['Immunity']:
              dmg = 0
          print('Dealing {} {} damage!'.format(dmg, Creature.Atk[i].DmgType))
          Target.HP = Target.HP - dmg
        else:
          print('Pass!')

      if Creature.Atk[i].Multiattack > 1:
        print('Attacked {} times!'. format( Creature.Atk[i].Multiattack) )

# -------------------------- PLAYER --------------------------
  if type(Creature) == Player:
    k = 0
    temp = []
    bonus = 'no'
    if mode == 'bonus': #bonus action atk
      if chosen != -1:
        if Creature.Inv['Equipped'][chosen].Light != 'yes':
          print('Invalid option.')
          return DoAtk(Creature, Target, mode == 'bonus')
      else:
        for i in range(len(Creature.Inv['Equipped'])):
          if Creature.Inv['Equipped'][i].Light == 'yes':
            if Creature.Inv['Equipped'][i].Name != Creature.done[round]['action'][1] or Creature.Inv['Equipped'].count( Creature.done[round]['action'][1]) > 1:
              temp.append(Creature.Inv['Equipped'][i])              
        print('Choose a weapon attack:')
        for i in range(len(temp)):
          print('{}- ' . format(i+1), Creature.Inv['Equipped'][i].Name.title())
        i = int(input())
        temp = temp[i-1]
        return DoAtk(Creature, Target, temp, round = round)
      
    elif chosen != -1:
      i = chosen
    else:
      print('Choose a weapon attack:')
      for i in range(len(Creature.Inv['Equipped'])):
        if 'shield' in Creature.Inv['Carried']:
          if Creature.Inv['Equipped'][i].TwoHanded != 'yes':
            print('{}- ' . format(i+1), Creature.Inv['Equipped'][i].Name.title())
        else:
          print('{}- ' . format(i+1), Creature.Inv['Equipped'][i].Name.title())
      temp = int(input())
      return DoAtk(Creature, Target, temp-1, round = round) 

    a = d(20)
    if special != 'none':
      b = d(20)
      if b == a:
        pass
      elif (b > a and special == 'adv') or (b < a and special == 'disadv'):
        a = b
        b = 0
      if Creature.Inv['Equipped'][i].TwoHanded == 'versatile' and 'shield' not in Creature.Inv['Carried']:
        print('One-handed or two-handed?')
        k = int(input('1/2: ')) 
        if k == 1:
          k = 0
        
    if Creature.Inv['Equipped'][i].Stat != 'finesse':
      b = mod(Creature.Stats[NtN(Creature.Inv['Equipped'][i].Stat)])
    else:
      if Creature.Stats[NtN('Dex')] >= Creature.Stats[NtN('Str')]:
        b = mod(Creature.Stats[NtN('Dex')])
      elif Creature.Stats[NtN('Str')] > Creature.Stats[NtN('Dex')]:
        b = Creature.Stats[NtN('Str')]
    if Creature.Inv['Equipped'][i].Name in Creature.WeaponProf:
      b = b + 2
    c = a + b
    print('{} attacks {} with a {}!\n {} + {} = {}' .format( Creature.Name, Target.Name, Creature.Inv['Equipped'][i].Name, a, b, c))
    if c >= Target.AC:
      if a == 20:
        h = 'crit'
        print('Critical hit!')
        a = d(Creature.Inv['Equipped'][i].DmgDie + k) + d(Creature.Inv['Equipped'][i].DmgDie + k)
      else:
        h = 'hit'
        print('Hit!')
        a = d(Creature.Inv['Equipped'][i].DmgDie + k)
      if (Creature.Inv['Equipped'][i].Stat == 'finesse' and Creature.Class.Name.lower() == 'rogue') and special == 'adv':
        a = a + d('2d6')
      if mode != 'bonus':
        if Creature.Inv['Equipped'][i].Stat != 'finesse':
          b = mod(Creature.Stats[NtN(Creature.Inv['Equipped'][i].Stat)])
        else:
          if Creature.Stats[NtN('Dex')] >= Creature.Stats[NtN('Str')]:
            b = mod(Creature.Stats[NtN('Dex')])
          elif Creature.Stats[NtN('Str')] > Creature.Stats[NtN('Dex')]:
            b = mod(Creature.Stats[NtN('Str')])
            
      dmg = a + b 

      if Creature.Inv['Equipped'][i].DmgType in list(get_all_values(Target.Typing)):
            if Creature.Inv['Equipped'][i].DmgType in Target.Typing['Resistance']:
              dmg = math.ceil(b /2)
            if Creature.Inv['Equipped'][i].DmgType in Target.Typing['Vulnerability']:
              dmg = b * 2
            if Creature.Inv['Equipped'][i].DmgType in Target.Typing['Immunity']:
              dmg = 0

      print('Dealing {} {} damage!' .format(dmg, Creature.Inv['Equipped'][i].DmgType))
      Target.HP = Target.HP - dmg
    else:
      h = 'miss'
      print('Miss!')
    if (Creature.Inv['Equipped'][i].Light == 'yes' and mode != 'bonus') and 'shield' not in Creature.Inv['Carried']:
      bonus = 'yes'
    
    done = ['Attack', Creature.Inv['Equipped'][i].Name, h, Target.Name, bonus]

    if mode == 'action':
      Creature.done[round]= {mode: done}
    else:
      Creature.done[round].update({mode: done})
    #Creatue.done[1] = {'action': ['Attack', 'Longsword', 'hit', 'Suvlo', 'no']}
    #print(Creature.done)     

def DoSpell (Caster, Target, chosen, mode = 'action', round = 1, special = 'none'):
  pass

def chooser(P1, Options, notOptions, mode, turn , action = 'choose'):
  #print('check chooser')
  if action == 'choose':
    actions = ['Attack']
    if mode == 'action':
      actions.append('Dodge')
      #print('check chooser / found dodge')
    
    if ('shield' in P1.Inv['Carried'] or 'shield' in P1.Inv['Removed']) and mode == 'action':
      #print('check chooser/ found shield')
      actions.append('Don/Doff shield')

    
    if P1.Class.Caster != 'no':
      #print('check chooser/ found caster')
      actions.append('Cast a spell')

    #print('check chooser / did choices')
    if len(actions) > 1:
      if mode == 'action':
        a = 'standard'
      else:
        a = mode
      print('Choose your', a, 'action:')
      actions.sort()
      for i in range(len(actions)):
        print(i+1, '-', actions[i])
      return chooser(P1, Options, notOptions, mode, turn, actions[int(input('Option: '))-1])
  
  elif action == 'Attack' or (action == 'choose' and len(actions) == 1):  
    print('Action: Attack')
    if bool(notOptions) == False:
      for i in range(len(Options)):
        print(i+1,'-', Options[i].Name)
      a = int(input('Target: '))
      a = Options[a-1]
    else:
      if Options[0].Name == notOptions[0]:
        a = Options[1]
      else:
        a = Options[0]
      print('Target:', a.Name)
    return DoAtk(P1, a, mode = mode, round = turn)

  if 'Don' in action:
    if 'shield' in P1.Inv['Carried']:
      print('Action: Doff shield')
      P1.AC = P1.AC - 2
      P1.Inv['Carried'].remove('shield')
      P1.Inv['Removed'].append('shield')
    else:
      print('Action: Don shield')
      P1.AC = P1.AC + 2 
      P1.Inv['Removed'].remove('shield')
      P1.Inv['Carried'].append('shield')
    P1.done[turn] = {'action': ['Don/doff', 'shield']}
    return

  if action == 'Dodge':
    #print('check chooser / chose dodge')
    if bool(notOptions) == False:
      return DoDodge(P1, Options, turn)
    elif Options[0].Name == notOptions[0]:
      return DoDodge(P1, Options[1], turn)
    else:
      return DoDodge(P1, Options[0], turn)  
    
  
  
def check(Target, round, k): #the souls franchise
  #Target.done = {1: {'effect': ['Rage', 12, 'end', 'Stat[0]', -2, 'self']}}
  for keys in Target.done:
    if 'effect' in Target.done[keys]:
      if Target.done[keys]['effect'][1] == round:
        if Target.done[keys]['effect'][2] == k:
          print(Target.Name + '\'s', Target.done[keys]['effect'][0], 'ends!')
          if len(Target.done[keys]['effect']) == 5 or Target.done[keys]['effect'][5] == 'self':
            setattr (Target, Target.done[keys]['effect'][3], Target.done[keys]['effect'][4])
          else: 
            for i in range(len(Target.done[keys]['effect'][5])):
              setattr (Target.done[keys]['effect'][5][i], Target.done[keys]['effect'][3], Target.done[keys]['effect'][4])
