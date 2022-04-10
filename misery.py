class Arena:
  Name = 'Arena'
  Size = [(), ()]
  Cover = {'Half': [], 34: [], 'Full': []}
  Hazards = {}
  People = {'Player': (), 'MonsterA': (), 'MonsterB': ()}
 
class Weapon:
  Name = 'Longsword'
  Stat = 'Str'
  DmgDie = 8
  DmgType = 'slashing'
  Light = 'no'
  TwoHanded = 'versatile'
  Ammo = 'no'
  
class Attack:
  Name = 'Club'
  Save = 'no'
  Multiattack = 1
  AtkType = 'none'
  SaveDC = 10
  AtkBonus = 4
  DmgDie = 4
  DmgBonus = 2
  DmgType = 'piercing'

class Spell:
  Name = 'Spell'
  Level = 0
  School = 'Abj'
  CastTime = 'acion'
  Range = '30'
  Duration = 'inst'
  Conc = 'no'
  Effect = []
  Source = 'Class'

class Dmg:
  Hit = 'yes'
  Target = 1
  Die = 6
  Bonus = 'no'
  Extra = []
  Type = 'force'

class Heal:
  Die = 6
  Target = 'self'
  Temp = 'no'

class Effect:
  Name = 'Hex'
  Target = 1
  Change = []

class Class:
  Name = 'Cleric'
  Saves = ['dex', 'wis']
  HitDie = 8
  Caster = 'no'
  Spells = [Spell()]

class Race:
  Name = 'Human'
  MainBuff = 'none'
  MinorBuff = [] 
  Atk = [Attack()]
  Spells = [Spell()]

class Player:
  Name = 'Player'
  Size = 'Medium'
  Stats = [10, 10, 10, 10, 10, 10]
  Speed = {'Walk': 30}
  init = MaxHP = HP = THP = 0 
  pos = ()
  AC = 10
  Inv = {'Equipped': [], 'Carried': [], 'Removed': []}
  Skills = []
  done = Extras = {}
  Special = 'none'
  WeaponProf = ArmorProf = ['None']
  Languages = ['Common']
  Typing = {'Resistance': [], 'Vulnerability': [], 'Immunity': []} #resistances etc
  Class = Class()
  Race = Race()
  
class Monster:
  Name = 'Monster'
  Stats = [10, 10, 10, 10, 10, 10]
  init = 0 
  AC = 10
  MaxHP = HP = 5
  Atk = [Attack(), Attack()]
  Special = 'none'
  Typing = {'Resistance': [], 'Vulnerability': [], 'Immunity': []}

