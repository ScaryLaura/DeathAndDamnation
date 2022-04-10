from pain import *
from misery import *
from suffering import *
import time

br()
print(color.BOLD, "Welcome to D&D simulator 1.5.280\n", color.END) #increase number every time you edit lmao
PC1 = Player()
  

PC1.Name = input('Your name: ').title()
if PC1.Name.lower() == ' ' or PC1.Name.lower() == 'dev':
  PC1.Name = 'Laura'
  print('DEV MODE')
  doDev(PC1)
  br()
else:
  print("Thanks, {}!".format(PC1.Name))
  print('Let\'s start with character creation!')
  statpain(PC1)

  br() #Race
  print('Choose a race:')
  while True:
    print('1- Elf -\x1B[3m +2 Dex and +1 Con, Int, Wis or Cha \x1B[0m')
    print(' 2- Gnome -\x1B[3m +2 Int and +1 Dex or Con \x1B[0m')
    print(' 3- Half-Elf -\x1B[3m +2 Cha and +1 any 2 unique \x1B[0m')
    print(' 4- Half-Orc -\x1B[3m +2 Str and +1 Con \x1B[0m')
    print(' 5- Halfling (not done) -\x1B[3m +2 Dex and +1 Cha or Con \x1B[0m')
    print(' 6- Human -\x1B[3m +1 all stats \x1B[0m')
    print(' 7- Tabaxi -\x1B[3m +2 Dex and +1 Cha \x1B[0m')
    print(' 8- Tiefling (not done) -\x1B[3m +2 Dex or Cha and +1 Int \x1B[0m')
    print(' 9- Triton -\x1B[3m +1 Str, Con and Cha \x1B[0m')
    print('10- Custom -\x1B[3m +1 any 3 unique\x1B[0m')
    print('11- Custom -\x1B[3m +2 any 1, +1 any 1\x1B[0m')
    ans = input('Option or \'info\': ')
    if ans.lower() in 'information':
      ans = int(input('Info about: '))
      raceinfo(ans)
      print('')
    else:
      ans = int(ans)
      racefinder(PC1, ans)
      break

  br()#background
  print('Background skills')
  skillchooser(PC1, 2)
  
  br() #class
  welcometoleagueofdraven(PC1)

update(PC1)  #it updates, who would've guessed

br()
testprints(PC1) #it shows a mini char sheet

if PC1.Name.lower() != 'none': #temp dev pass
  if input('Combat? ').lower() in 'yes':
    br()
    print("Choose your encounter:")
    print("1 - Suvlo, the Kobold Beastmaster")
    print("2 - Dr. Hoo, the angel of death")
    print("3 - Smasher and Probe, the constructs")
    ans = int(input())
  
    Monster = [monsterfinder(ans, 1), monsterfinder(ans, 2)]

    print('\nOkay! Rolling initiative...')
    init = initmaker(Monster[0], Monster[1], PC1)
    print('')
    for i in range(len(init)):
      print(*init[i], sep = ' - ')

    #combat time
    counter =  1
    i = k = 0 
    removed = []
    print(color.CYAN, color.BOLD,  '\nRound 1', color.END)
    while True: #loop babyyyy
      if len(removed) == 2: #if only player left
        print(color.GREEN)
        br()
        print('           YOU WIN!!')
        br()
        print(color.END)
        break

      if i == 3:
        i = 0
        counter = counter + 1    
        br()
        print(color.BOLD, color.CYAN, ' Round', counter, color.END)
  
      time.sleep(1)
      if init[i][0] in removed:
          pass
      else:
        print('\n{}\'s turn!'. format(init[i][0]))  
          
        if init[i][0] == Monster[0].Name:
          if Monster[0].HP <= 0:
            k = counter
            removed.append(Monster[0].Name)
          else:
            status(Monster[0])
            DoAtk(Monster[0], PC1, round = counter, special = Monster[0].Special)
            
        elif init[i][0] == Monster[1].Name:
          if Monster[1].HP <= 0:
            k = counter
            removed.append(Monster[1].Name)
          else:
            status(Monster[1])
            DoAtk(Monster[1], PC1, round = counter, special = Monster[1].Special)  
        
        elif init[i][0] == PC1.Name: #player round
          if PC1.HP <= 0:
            print(color.RED)
            br()
            print('         SE FUDEU!')
            br()
            print(color.END)
            break
          check(PC1, counter, 'start')
          status(PC1, 'show')
          #print('Action: Attack')
          chooser(PC1, Monster, removed, 'action', counter)
          #print(PC1.done)
          if PC1.done[counter]['action'][0] == 'Attack': 
            if PC1.done[counter]['action'][4] == 'yes':
              chooser(PC1, Monster, removed, 'bonus', counter)
          check(PC1, counter, 'end')
        
        
      if k == counter:
        print(init[i][0], 'was defeated! Removed from combat.')
        k = k-1
      
      i = i + 1

      
      
