import random
phealth=100
pattack=15
pdefence=5
pgold=100
ppotion=2
pexperience=0
plevel=1
monsterdefeated=0
pinventory=0
print("""
KINGDOM OF SHADOWS

The kingdom has fallen into darkness, and dangerous monsters now roam the land.
 The powerful Shadow King is behind it all.

You are a brave warrior who must explore the kingdom, 
collect gold and weapons, fight monsters, complete quests, 
and become stronger.

Your ultimate goal is to defeat the Shadow King and bring peace back to the kingdom.
 
YOUR ADVENTURE BEGIN NOW......
you can fight with shadow king when you have gold

""")
while phealth>0:
    print("""
======================================
         KINGDOM OF SHADOWS
======================================
    """)
    print("player health=",phealth)
    print("player attack=",pattack)
    print("player defence=",pdefence)
    print("player gold=",pgold)
    print("player potions=",ppotion)
    print("player experience=",pexperience)
    print("player level=",plevel)
    pchoice=input("""
    explore
    fight
    inventory
    shop
    character
    rest
    quit
    ====
    ====
    """)
    #explore logic
    if pchoice=="explore":
        rexplore=random.choice(["forest","abandoned village","mountain","dark cave"])
        #forest whole logic
        if rexplore=="forest":
            print("you are entering in the forest")
            forestevent=random.choice(["wolf","gold","potion","nothing"])
            #wolf logic attact and enmey
            if forestevent=="wolf":
                whealth=30
                wattack=10
                wgoldreward=20
                xpreward=10
                while whealth>0 and phealth>0:
                    print("========WOLF BATTLE========")
                    print("a wolf appear")
                    print("wolf health:",whealth)
                    print("player health:",phealth)
                    print("your attack",pattack)
                    print("your defence:",pdefence)
                    wcombact=input("""
                you have three choices:
                attack
                potion
                run
                """)
                    if wcombact=="attack":
                      attack=random.randint(15,25)    
                      whealth-=attack
                      print("wolf health is:",whealth)
                      if whealth<=0:
                          print("the wolf dies")
                          pgold+=wgoldreward
                          print("your gold increase so total gold is",pgold)
                          pexperience+=xpreward
                          print("you get XP:",xpreward)
                          monsterdefeated+=1
                          print("monster counter increase:",monsterdefeated)
                          break
                      elif whealth>0:
                          damage=max(0,wattack-pdefence)
                          phealth-=pdefence
                          print("the wolf attack on you")
                          print("your health is:",phealth)
                          if phealth>0:
                            print("continue the battle")
                          elif phealth<=0:
                            print("you die game over")
                            break
                    elif wcombact=="potion":
                        if ppotion>0:
                          ppotion-=1
                          phealth=min(100,phealth+30)
                          print("your health is increase +30",phealth)
                          if  whealth>0:
                            damage=max(0,wattack-pdefence)
                            phealth-=pdefence
                            print("the wolf attack on you")
                            print("your health is:",phealth)
                            if phealth>0:
                                print("continue the battle")
                            elif phealth<=0:
                                print("you die game over")
                                break
                    if ppotion==0:
                        print("you dont have any potions")
                    elif wcombact=="run":
                      escape=random.choice([20,30,40,50])
                      if escape==20 or escape==30 or escape==40 :
                        print("""you sucessfully escape
                        you sucessfully escape
                        the battle ended
                              """)
                        break
                      elif escape==50:
                        print("""
                    the battle is still continue:
                    """)
                        damage=max(0,wattack-pdefence)
                        phealth-=damage
                        #wolf logic ended
            elif forestevent=="gold":
                gold=random.randint(20,60)
                pgold+=gold
                print("player find",gold,"coins in forest")
                print("soo total gold is:",pgold)
            elif forestevent=="potion":
                ppotion+=1
                print("player find one portion in forest")
            elif forestevent=="nothing":
                print("nothing found in forest")
        # village logic
        elif rexplore=="abandoned village":
            print("you are going to abandond village")
            villageevent=random.choice(["gold","potion","zombie","empty village"])
            if villageevent=="gold":
                gold=random.randint(30,80)
                pgold+=gold
                print("you find gold from abandond village",gold)
                print("total gold",pgold)
            elif villageevent=="potion":
                ppotion+=1
                print("find one potion from abandond village =total potion:",ppotion)
                #zombie logic
            elif villageevent=="zombie":
                print("zombie attack you in abandond village")
                zhealth=50
                zattack=15
                zgold=40
                zxp=20
                while phealth>0 and zhealth>0:
                    print("============ ZOMBIE BATTLE============")
                    print("zombie health:",zhealth)
                    print("your health:",phealth)
                    print("your attack:",pattack)
                    print("your defence:",pdefence)
                    zcombact=input("""
                attack
                potion
                run
                """)
                    if zcombact=="attack":
                        attack=random.randint(15,30)
                        zhealth-=attack
                        print("you attack the zombie:",attack)
                        print("zombie health:",zhealth)
                        if zhealth>0:
                            print("zombie attack on you:",zattack)
                            damage=max(0,zattack-pdefence)
                            phealth-=pdefence
                            print("you losehealth:",phealth)
                        elif zhealth<=0:
                            pgold+=zgold
                            pexperience+=zxp
                            monsterdefeated+=1
                            print("zombie deafeted")
                            print("you got gold",pgold)
                            break
                        elif phealth<=0:
                            print("you died game over")
                            break
                    elif zcombact=="potion":
                        if ppotion>0:
                            ppotion-=1
                            phealth=min(100,phealth+30)
                            print("your health is increase by +30:",phealth)
                            print("player potion",ppotion)
                        elif ppotion<=0:
                            print("you dont have enough potions")
                    elif zcombact=="run":
                        rchance=random.choice([20,30,40,50])
                        if rchance==20 or rchance==30 or rchance==40:
                            print("sucessful escape")
                            break
                        elif rchance==50:
                            print("escape unsuccesfull")
                            damage=max(0,zattack-pdefence)
                            phealth-=pdefence
                            #zombie logic ended
            elif villageevent=="empty village":
                print("you found an empty village so nothing found")
        #mountain logic
        elif rexplore=="mountain":
            print("you are going to mountains")
            mountainevent=random.choice(["weapon","strong monster","gold","nothing"])
            if mountainevent=="weapon":
                pattack+=5
                print("congrats you find a better weapon from mountains")
                print("attack increase:",pattack)
            elif mountainevent=="strong monster":
                print("start combact with a monster in mountains")
            elif mountainevent=="gold":
                gold=random.randint(50,100)
                pgold+=gold
                print("you find gold in mountains soo total gold is:",pgold)
            elif mountainevent=="nothing":
                print("nothing found in mountains")
        # dark cAVE logic
        elif rexplore=="dark cave":
            print("you are going in dark cave")
            caveevent=random.choice(["rare weapon","treasure","dragon","trap","nothing"])
            if caveevent=="rare weapon":
                pattack+=10
                print("found a powerfull weapon in dark cave attack increase")
                print("total attack",pattack)
            elif caveevent=="treasure":
                gold=random.randint(100,200)
                pgold+=gold
                print("you found gold in dark cave so totle gold is :",pgold)
            elif caveevent=="trap":
                phealth-=20
                print("you are inside a dark cave and in trap health decrease by 20")
            elif caveevent=="nothing":
                print("nothing found in cave")
            elif caveevent=="dragon":
                dhealth=100
                dattack=30
                dgold=120
                dxp=50
                print("========DRAGON BATTLE=======")
                print("a dragon appear")
                print("dragon health:",dhealth)
                print("player health:",phealth)
                print("your attack",pattack)
                print("your defence:",pdefence)
                while dhealth>0 and phealth>0:
                    dcombact=input("""
                     you have three choices:
                    attack
                    potion
                    run
                       """)
                    if dcombact=="attack":
                            attack=random.randint(15,25)    
                            dhealth-=attack
                            print("dragon health is:",dhealth)
                            if dhealth<=0:
                                print("the dragon dies")
                                pgold+=dgold
                                print("your gold increase so total gold is",pgold)
                                pexperience+=dxp
                                print("you get XP:",dxp)
                                monsterdefeated+=1
                                print("monster counter increase:",monsterdefeated)
                                break
                            elif dhealth>0:
                                damage=max(0,dattack-pdefence)
                                phealth-=pdefence
                                print("dragon attack on you")
                                print("your health is:",phealth)
                                if phealth>0:
                                    print("continue the battle")
                                elif phealth<=0:
                                        print("you die game over")
                                        break
                    elif dcombact=="potion":
                        if ppotion>0:
                            ppotion-=1
                            phealth=min(100,phealth+30)
                            print("your health is increase +30",phealth)
                            if  dhealth>0:
                                damage=max(0,dattack-pdefence)
                                phealth-=pdefence
                                print("dragon attack on you")
                                print("your health is:",phealth)
                                if phealth>0:
                                        print("continue the battle")
                                elif phealth<=0:
                                        print("you die game over")
                                        break
                        if ppotion==0:
                            print("you dont have any potions")
                    elif dcombact=="run":
                        escape=random.choice([20,30,40,50])
                        if escape==20 or escape==30 or escape==40 :
                                print("""you sucessfully escape
                                        you sucessfully escape
                                        the battle ended
                                              """)
                                break
                        elif escape==50:
                            print("""
                                    the battle is still continue:
                                    """)
                            damage=max(0,dattack-pdefence)
                            phealth-=damage
    elif pchoice=="shop":
        shoping=input("""
        potion
        sword
        armor
        dragon sword
        """)
        if shoping=="potion":
            if pgold>=30:
                pgold-=30
                ppotion+=1
                print("you get a potion:",ppotion)
            elif pgold<30:
                print("you did not hve enought gold")
                
        if shoping=="sword":
            if pgold>=100:
                pgold-=100
                pattack+=10
                print("you geta sword you attack is increase",pattack)
            elif pgold<100:
                print("you have not enough gold")
        if shoping=="armor":
            if pgold>=150:
                pgold-=150
                pdefence+=5
                print("you get an armor your defence is increase:",pdefence)
            elif pgold<150:
                print("you do not have enough gold")
        if shoping=="dragon sword":
            if pgold>=400:
                pgold-=400
                pattack+=25
                print("you get a dragon sword your attack increase:",pattack)
            elif pgold<400:
                print("you do not have enough gold")
    elif pchoice=="inventory":
        print("========INVENTORY========")
        print("POTIONS=",ppotion)
        print("GOLD=",pgold)
        print("PLAYER DEFENCE=",pdefence)
        print("PLAYER ATTACK=",pattack)
        print("PLAYER LEVEL=",plevel)
    elif pchoice=="rest":
        if pgold>=20:
            phealth+=30
            pgold-=20
            print("your are resting at village your hralth increase:",phealth)
        elif pgold<20:
            print("you did not have enough gold to rest")
    if phealth<=0:
        print("YOU DIED")
        print("level=",plevel)
        print("gold=",pgold)
        print("monster deafeted=",monsterdefeated)
        print("GAME OVER")
        break
    elif pchoice=="fight":
        enemey=random.choice(["wolf","zombie","dragon",])
        if  enemey=="wolf":
                        whealth=30
                        wattack=10
                        wgoldreward=20
                        xpreward=10
                        while whealth>0 and phealth>0:
                            print("========WOLF BATTLE========")
                            print("a wolf appear")
                            print("wolf health:",whealth)
                            print("player health:",phealth)
                            print("your attack",pattack)
                            print("your defence:",pdefence)
                            wcombact=input("""
                        you have three choices:
                        attack
                        potion
                        run
                        """)
                            if wcombact=="attack":
                              attack=random.randint(15,25)    
                              whealth-=attack
                              print("wolf health is:",whealth)
                              if whealth<=0:
                                  print("the wolf dies")
                                  pgold+=wgoldreward
                                  print("your gold increase so total gold is",pgold)
                                  pexperience+=xpreward
                                  print("you get XP:",xpreward)
                                  monsterdefeated+=1
                                  print("monster counter increase:",monsterdefeated)
                                  break
                              elif whealth>0:
                                  damage=max(0,wattack-pdefence)
                                  phealth-=pdefence
                                  print("the wolf attack on you")
                                  print("your health is:",phealth)
                                  if phealth>0:
                                    print("continue the battle")
                                  elif phealth<=0:
                                    print("you die game over")
                                    break
                            elif wcombact=="potion":
                                if ppotion>0:
                                  ppotion-=1
                                  phealth=min(100,phealth+30)
                                  print("your health is increase +30",phealth)
                                  if  whealth>0:
                                    damage=max(0,wattack-pdefence)
                                    phealth-=pdefence
                                    print("the wolf attack on you")
                                    print("your health is:",phealth)
                                    if phealth>0:
                                        print("continue the battle")
                                    elif phealth<=0:
                                        print("you die game over")
                                        break
                            if ppotion==0:
                                print("you dont have any potions")
                            elif wcombact=="run":
                              escape=random.choice([20,30,40,50])
                              if escape==20 or escape==30 or escape==40 :
                                print("""you sucessfully escape
                                you sucessfully escape
                                the battle ended
                                      """)
                                break
                              elif escape==50:
                                print("""
                            the battle is still continue:
                            """)
                                damage=max(0,wattack-pdefence)
                                phealth-=damage
        elif enemey=="dragon":
                dhealth=100
                dattack=30
                dgold=120
                dxp=50
                print("========DRAGON BATTLE=======")
                print("a dragon appear")
                print("dragon health:",dhealth)
                print("player health:",phealth)
                print("your attack",pattack)
                print("your defence:",pdefence)
                while dhealth>0 and phealth>0:
                    dcombact=input("""
                     you have three choices:
                    attack
                    potion
                    run
                       """)
                    if dcombact=="attack":
                            attack=random.randint(15,25)    
                            dhealth-=attack
                            print("dragon health is:",dhealth)
                            if dhealth<=0:
                                print("the dragon dies")
                                pgold+=dgold
                                print("your gold increase so total gold is",pgold)
                                pexperience+=dxp
                                print("you get XP:",dxp)
                                monsterdefeated+=1
                                print("monster counter increase:",monsterdefeated)
                                break
                            elif dhealth>0:
                                damage=max(0,dattack-pdefence)
                                phealth-=pdefence
                                print("dragon attack on you")
                                print("your health is:",phealth)
                                if phealth>0:
                                    print("continue the battle")
                                elif phealth<=0:
                                        print("you die game over")
                                        break
                    elif dcombact=="potion":
                        if ppotion>0:
                            ppotion-=1
                            phealth=min(100,phealth+30)
                            print("your health is increase +30",phealth)
                            if  dhealth>0:
                                damage=max(0,dattack-pdefence)
                                phealth-=pdefence
                                print("dragon attack on you")
                                print("your health is:",phealth)
                                if phealth>0:
                                        print("continue the battle")
                                elif phealth<=0:
                                        print("you die game over")
                                        break
                        if ppotion==0:
                            print("you dont have any potions")
                    elif dcombact=="run":
                        escape=random.choice([20,30,40,50])
                        if escape==20 or escape==30 or escape==40 :
                                print("""you sucessfully escape
                                        you sucessfully escape
                                        the battle ended
                                              """)
                                break
                        elif escape==50:
                            print("""
                                    the battle is still continue:
                                    """)
                            damage=max(0,dattack-pdefence)
                            phealth-=damage
        elif enemey=="zombie":
                print("zombie attack you in abandond village")
                zhealth=50
                zattack=15
                zgold=40
                zxp=20
                while phealth>0 and zhealth>0:
                    print("============ ZOMBIE BATTLE============")
                    print("zombie health:",zhealth)
                    print("your health:",phealth)
                    print("your attack:",pattack)
                    print("your defence:",pdefence)
                    zcombact=input("""
                attack
                potion
                run
                """)
                    if zcombact=="attack":
                        attack=random.randint(15,30)
                        zhealth-=attack
                        print("you attack the zombie:",attack)
                        print("zombie health:",zhealth)
                        if zhealth>0:
                            print("zombie attack on you:",zattack)
                            damage=max(0,zattack-pdefence)
                            phealth-=pdefence
                            print("you losehealth:",phealth)
                        elif zhealth<=0:
                            pgold+=zgold
                            pexperience+=zxp
                            monsterdefeated+=1
                            print("zombie deafeted")
                            print("you got gold",pgold)
                            break
                        elif phealth<=0:
                            print("you died game over")
                            break
                    elif zcombact=="potion":
                        if ppotion>0:
                            ppotion-=1
                            phealth=min(100,phealth+30)
                            print("your health is increase by +30:",phealth)
                            print("player potion",ppotion)
                        elif ppotion<=0:
                            print("you dont have enough potions")
                    elif zcombact=="run":
                        rchance=random.choice([20,30,40,50])
                        if rchance==20 or rchance==30 or rchance==40:
                            print("sucessful escape")
                            break
                        elif rchance==50:
                            print("escape unsuccesfull")
                            damage=max(0,zattack-pdefence)
                            phealth-=pdefence

    if pgold>=1000:
        player=input("""
    you can fight with shadow king
    quit
    """)
        if player=="shadow king":
                whealth=300
                wattack=35
                wgoldreward=1000
                xpreward=200
                while whealth>0 and phealth>0:
                    print("========SHADOW KING BATTLE FINAL BOSS========")
                    print(" SHADOW KING IS IN FORONT OF YOU")
                    print("SHADOW KING  health:",whealth)
                    print("player health:",phealth)
                    print("your attack",pattack)
                    print("your defence:",pdefence)
                    wcombact=input("""
                you have three choices:
                attack
                potion
                run
                """)
                    if wcombact=="attack":
                      attack=random.randint(15,25)    
                      whealth-=attack
                      print("SHADOW KING health is:",whealth)
                      if whealth<=0:
                          pgold+=wgoldreward
                          pexperience+=xpreward
                          monsterdefeated+=1
                          print("""
            ====================================
                    SHADOW KING DEFEATED
            ====================================
                  THE KINGDOM HAS BEEN SAVED
""")
                          print("player level=",plevel)
                          print("player gold=",pgold)
                          print("the monsters you have defeated=",monsterdefeated)
                          print("YOU ARE THE HERO OF KINGDOM")
                          print("GAME ENDED")
                          break
                      elif whealth>0:
                          damage=max(0,wattack-pdefence)
                          phealth-=pdefence
                          print("the SHADOW KING attack on you")
                          print("your health is:",phealth)
                          if phealth>0:
                            print("continue the battle")
                          elif phealth<=0:
                            print("you die game over")
                            break
                    elif wcombact=="potion":
                        if ppotion>0:
                          ppotion-=1
                          phealth=min(100,phealth+30)
                          print("your health is increase +30",phealth)
                          if  whealth>0:
                            damage=max(0,wattack-pdefence)
                            phealth-=pdefence
                            print("the SHADOW KING attack on you")
                            print("your health is:",phealth)
                            if phealth>0:
                                print("continue the battle")
                            elif phealth<=0:
                                print("you die game over")
                                break
                    if ppotion==0:
                        print("you dont have any potions")
                    elif wcombact=="run":
                      escape=random.choice([20,30,40,50])
                      if escape==20 or escape==30 or escape==40 :
                        print("""you sucessfully escape
                        you sucessfully escape
                        the battle ended
                              """)
                        break
                      elif escape==50:
                        print("""
                    the battle is still continue:
                    """)
                        damage=max(0,wattack-pdefence)
                        phealth-=damage
    elif pchoice=="character":
        print("=======CHARACTER STATUS=======")
        print("HEALTH=",phealth)
        print("ATTACK=",pattack)
        print("GOLD=",pgold)
        print("POTIONS=",ppotion)
        print("XP=",pexperience)
        print("LEVEL=",plevel)
        print("MONSTER DEFEATED=",monsterdefeated)
    elif pchoice=="quit":
        print("you quit the game")
        break
