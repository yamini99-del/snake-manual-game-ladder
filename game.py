import random
count1=0
count2=0
flag=0
print("                           ----- Snake and ladder-----")
print("                           ------------------------")                
print("                            41  42 // 44  45  \\\    47  48  49  50")
print("                            40   //   38  37 36 \\\  34  33  32  31")
print("                                //22   23 // 25 26 27  28  29  30")
print("                            20  19  18   //  16  ||   14  13  12  11")
print("             [start]  =>  01  02  03  04  05  ||   07  08  09  10")
print("Enter player name 1:")
p1=input()
print("Enter player name 2:")
p2=input()
print("-------Press enter to roll--------") 
for i in range(1,101):
    for j in range(1,3):
        if j==1:
            print(p1,"turn:",end="\n")
            choice=input()
            if choice=='':
              a1=random.randint(1,6)
              print("rolled:",a1,end="\n")
              count1=count1+a1
              print("You are at:",count1,"\n")
              if count1==6:
                  count1=15
                  print("You just climbed a ladder",end="\n")
                  print("You are at:",count1,"\n")
              elif count1==21:
                  count1=43
                  print("You just climbed a ladder",end="\n")
                  print("You are at:",count1,"\n")
              elif count1==17:
                  count1=24
                  print("You just climbed a ladder",end="\n")
                  print("You are at:",count1,"\n")
              elif count1==35:
                  count1=46
                  print("You just climbed a ladder",end="\n")
                  print("You are at:",count1,"\n")
              elif count1==11:
                  count1=2
                  print("You were killed by a snake",end="\n")
                  print("You are at:",count1,"\n")
              elif count1==23:
                  count1=13
                  print("You were killed by a snake",end="\n")
                  print("You are at:",count1,"\n")
              elif count1==37:
                  count1=28
                  print("You were killed by a snake",end="\n")
                  print("You are at:",count1,"\n")
              elif count1==48:
                  count1=7
                  print("You were killed by a snake",end="\n")
                  print("You are at:",count1,"\n")
              if count1>=50:
                  flag=1
                  break
              
        if j==2:
            print(p2,"turn:",end="\n")
            choice=input()
            if choice=='':
              b1=random.randint(1,6)
              print("rolled:",b1,end="\n")
              count2=count2+b1
              print("You are at:",count2,"\n")
              if count2==6:
                  count2=15
                  print("You just climbed a ladder",end="\n")
                  print("You are at:",count2,"\n")
              elif count2==21:
                  count2=43
                  print("You just climbed a ladder",end="\n")
                  print("You are at:",count2,"\n")
              elif count2==17:
                  count2=24
                  print("You just climbed a ladder",end="\n")
                  print("You are at",count2,"\n")
              elif count2==35:
                  count2=46
                  print("You just climbed a ladder",end="\n")
                  print("You are at:",count2,"\n")
              elif count2==11:
                  count2=2
                  print("You were killed by a snake",end="\n")
                  print("You are at:",count2,"\n")
              elif count2==23:
                  count2=13
                  print("You were killed by a snake",end="\n")
                  print("You are at:",count2,"\n")
              elif count2==37:
                  count2=28
                  print("You were killed by a snake",end="\n")
                  print("You are at:",count2,"\n")
              elif count2==48:
                  count2=7
                  print("You were killed by a snake",end="\n")
                  print("You are at:",count2,"\n")
              if count2>=50:
                  flag=2
                  break
    if flag==1:
        print(p1,"wins")
        break
    elif flag==2:
        print(p2,"wins")
        break
