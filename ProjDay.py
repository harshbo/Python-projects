n =input("Enter date dd-mm-yy : ")
d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
lp=0
l=n.split("-")
l=[eval(i) for i in l]	
y=l[2]
y-=1
r=y%100
y1=y-r
y1 = y1%400
odays=0
if(y1==100):
    odays = 5
elif(y1==200):
    odays = 3
elif(y1==300):
    odays = 1
else:
    odays = 0


if(r<4):
    odays=odays+r
else:
    q=r//4
    r=r-q
    odays=odays+q*2+r
m=l[1]
s=0
for i in d:
    if(i<m):
        s=s+d[i]
s=s+l[0]
#print(s)
odays=odays+s
#print(odays)
odays=odays%7
#print(odays,y)
y=y+1
# century year divided by 400 is leap year
if (((y% 4  == 0) and (y % 100 != 0 ))or(y%400==0) ):
    lp=1
    if(lp==1):
        odays +=1
#print(odays,lp)
    
if(odays == 1):
    print("MONDAY")
elif(odays == 2):
    print("TUESDAY")
elif(odays == 3):
    print("WEDNESDAY")
elif(odays == 4):
    print("THURSDAY")
elif(odays == 5):
    print("FRIDAY")
elif(odays == 6):
    print("SATURDAY")
elif(odays==0 or odays==7):
    print("SUNDAY")

        