'''
1for snake
-1 for water
0 for gun
'''
computer=-1
youstr=input("enter your cholce:")
youDict={"s":1,"w":-1, "g":0}
you=youDict[youstr]
if(computer==-1 and you==1):
    print("you win")
elif(computer==-1 and you==0):
    print("yuo losel")
elif(computer==you):
    print("it draw")
elif(computer==1 and you==-1):
    print("you losel")
elif(computer==-1 and you==0):
    print(" you win")
elif(computer==0 and you==-1):
   print("you win")
elif(computer==0 and you==-1):
    print("you losel")
else:
    print("somting with worg")

