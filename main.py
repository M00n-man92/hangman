import random
from art import art_list
mylist=["yellow","red","blue","orange"]
something=[]
hope=0
a=random.choice(mylist) 


for smile in range(0,len(a)):
    something.append("__ ")
print(something)
megasonic=""
supersonic=""
error=0
count=0
win=True

while win and error<7:
   
    b=input("select the character of yore choice   ").lower()
    
    for skip in range(0,len(a)):
        
        if something[skip]=="__ ":
            if b==a[skip]:
                if skip==len(a)-1:
                    
                    something.append(b)
                    
                    something.pop(len(a))
                something.insert(skip,b)
                
                something.pop(skip+1)
                 
                
            elif b!=a[skip]:
                count+=1
                
                if count==len(a):
                    error+=1
                    
        else:
            if b!=a[skip]:
                count+=1
                
                if count==len(a):
                    error+=1
                    print("you've lost a life")
        megasonic+=something[skip]+" "
    for skipp in range(0,len(a)):
            if something[skipp]!="__ ":
                hope+=1
                
                if hope==len(a):
                   print("you've done it you've won")
                   for hi in range(0,len(something)):
                        supersonic+=something[hi]+" "
                
                    
    if supersonic=="":              
        if error<7:
            print(art_list[error])
            print(f"you've lost a life {8-error}s left")
            print(something)
     
        else:
            print(art_list[7]) 
    else:
        print(supersonic)
        win=False      
                

    
   
    megasonic=""
    count=0
    hope=0
print("gameover")