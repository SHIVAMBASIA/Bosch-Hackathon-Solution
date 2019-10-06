from decimal import Decimal
with open("Data.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)
with open("out.txt", "a") as myfile:
    myfile.write("\n")
f = open("out.txt", "r")
lines = f.readlines()
f.close()
f = open("output.txt", "w")
for i in range(len(lines)-1, -1, -1):
    f.write(lines[i])
f.close()
f = open("output.txt", "r")
lines1 = f.readlines()
f.close()
ab=[]
ef=[]
gh=[]
for i in range(len(lines1)):
    if((" to " in lines1[i])==True):
        if((("comes to" in lines1[i])==False) and (("bowl round" in lines1[i])==False) and (("THAT'S OUT" in lines1[i])==False) and (("needs to" in lines1[i])==False) and (("got to " in lines1[i])==False) and (("delight to" in lines1[i])==False)):
            ab.append([lines1[i].split(" to ")[0]])
            cd=lines1[i].split(" to ")[1]
            ef.append([cd.split(",")[0]])
            gh.append([cd.split(",")[1]])
 

bowlers=[]           
for x in ab: 
    if x not in bowlers: 
        bowlers.append(x) 
batsmen=[]
for x in ef: 
    if x not in batsmen: 
        batsmen.append(x)
batruns=[]
ballsfaced=[] 
boundaries=[]
sixes=[]
status=[]       
for x in range(len(batsmen)):
    batruns.append(batsmen[x])
    ballsfaced.append(batsmen[x])
    boundaries.append(batsmen[x])
    sixes.append(batsmen[x])
    status.append(batsmen[x])
    batruns[x]=0
    ballsfaced[x]=0
    boundaries[x]=0
    sixes[x]=0
    status[x]='\tnot out\t\t\t'
bowlruns=[]
ballsbowled=[]
widesbowled=[]
wickets=[]
noballs=[]
maidens=[]
oversbowled=[]
economy=[]
for x in range(len(bowlers)):
    bowlruns.append(bowlers[x])
    ballsbowled.append(bowlers[x])
    widesbowled.append(bowlers[x])
    wickets.append(bowlers[x])
    noballs.append(bowlers[x])
    maidens.append(bowlers[x])
    economy.append(bowlers[x])
    oversbowled.append(bowlers[x])
    bowlruns[x]=0
    ballsbowled[x]=0
    widesbowled[x]=0
    wickets[x]=0
    noballs[x]=0
    maidens[x]=0
    oversbowled[x]=0
    economy[x]=0

rq=[]
for x in range(len(gh)):
    rq.append(gh[x])

for i in range(len(batsmen)):
    for j in range(len(rq)):
        if((batsmen[i]==ef[j])==True):
            if(("out Caught by" in str(rq[j]))==True):
                cc=str(rq[j]).split('out Caught by')[1]
                dd=cc.split('!')[0]
                ee=str(ab[j])
                ff=ee.split("['")[1]
                gg=ff.split("']")[0]
                hh=str('c '+dd+' b '+gg)
                if(len(hh)<25):
                    hh=str(hh+"\t")
                if(len(str(batsmen[i]))<11):
                    hh=str("\t"+hh)
                status[i]=hh
            if(("out Bowled" in str(rq[j]))==True):
                ee=str(ab[j])
                ff=ee.split("['")[1]
                gg=ff.split("']")[0]
                hh=str("\t"+'b '+gg+"\t\t")
                status[i]=hh

for i in range(len(bowlers)):
    for j in range(len(rq)):
        if((bowlers[i]==ab[j])==True):
            if(("out" in str(rq[j]))==True):
                wickets[i]=wickets[i]+1
                rq[j]=-4
            if(rq[j]==[' wide']):
                widesbowled[i]=widesbowled[i]+1
                rq[j]=-1


for i in range(len(rq)):
    if(rq[i]==[' 1 run']):
        rq[i]=1
    if(rq[i]==[' no run']):
        rq[i]=0    
    if(rq[i]==[' SIX']):
        rq[i]=6
    if(rq[i]==[' FOUR']):
        rq[i]=4
    if(rq[i]==[' four']):
        rq[i]=4
    if(rq[i]==[' Six']):
        rq[i]=6
    if(rq[i]==[' leg byes']):
        rq[i]=-2
    if(rq[i]==[' 5 runs']):
        rq[i]=5
    if(rq[i]==[' 4']):
        rq[i]=4
    if(rq[i]==[' 2 runs']):
        rq[i]=2
    if(rq[i]==[' 3 runs']):
        rq[i]=3
    if(rq[i]==[' 6']):
        rq[i]=6
    if(rq[i]==['no ball']):
        rq[i]==-3
    if(rq[i]==['byes']):
        rq[i]==-5
    if(rq[i]==['penalty']):
        rq[i]==-6
legbyes=0
wides=0
totalnoballs=0
byes=0
penalty=0
for i in range(len(batsmen)):
    for j in range(len(rq)):
        if(batsmen[i]==ef[j]):
            if(rq[j]==0):
                ballsfaced[i]=ballsfaced[i]+1
            if(rq[j]>0):
                batruns[i]=batruns[i]+rq[j]
                ballsfaced[i]=ballsfaced[i]+1                    
                if(rq[j]==4):
                    boundaries[i]=boundaries[i]+1
                if(rq[j]==6):
                    sixes[i]=sixes[i]+1
            if(rq[j]==-2):
                ballsfaced[i]=ballsfaced[i]+1
                legbyes=legbyes+1
            if(rq[j]==-1):
                wides=wides+1   
            if(rq[j]==-4):
                ballsfaced[i]=ballsfaced[i]+1


for i in range(len(bowlers)):
    bowlruns[i]=widesbowled[i]
    for j in range(len(rq)):
        if(bowlers[i]==ab[j]):
            if(rq[j]==0):
                ballsbowled[i]=ballsbowled[i]+1
            if(rq[j]>0):
                bowlruns[i]=bowlruns[i]+rq[j]
                ballsbowled[i]=ballsbowled[i]+1                    
            if(rq[j]==-2):
                ballsbowled[i]=ballsbowled[i]+1  
            if(rq[j]==-4):
                ballsbowled[i]=ballsbowled[i]+1

fowball=[]
fowbatsman=[]
fowruns=[]
fowwickets=[]
currentruns=0
totalballsbowled=0
totalwickets=0
for j in range(len(rq)):
    if(rq[j]>=0):
        currentruns=currentruns+rq[j]
        totalballsbowled=totalballsbowled+1
    if(rq[j]==-1):
        currentruns=currentruns+1
    if(rq[j]==-2):
        currentruns=currentruns+1
        totalballsbowled=totalballsbowled+1
    if(rq[j]==-4):
        totalballsbowled=totalballsbowled+1
        totalwickets=totalwickets+1
        fowball.append(totalballsbowled)
        fowbatsman.append(ef[j])
        fowruns.append(currentruns)
        fowwickets.append(totalwickets)
strikerate=[]
for i in range(len(batsmen)):
    ee=str(batsmen[i])
    ff=ee.split("['")[1]
    gg=ff.split("']")[0]
    batsmen[i]=gg
    strike=Decimal((float(batruns[i])/float(ballsfaced[i]))*100)
    strike=round(strike,2)
    strikerate.append(strike)
for i in range(len(fowbatsman)):
    ee=str(fowbatsman[i])
    ff=ee.split("['")[1]
    gg=ff.split("']")[0]
    fowbatsman[i]=gg
for i in range(len(bowlers)):
    ee=str(bowlers[i])
    ff=ee.split("['")[1]
    gg=ff.split("']")[0]
    bowlers[i]=gg
    if(len(bowlers[i])<8):
        bowlers[i]=str(bowlers[i])+"\t"
    oversbowled[i]=int(ballsbowled[i]/6)
    economy[i]=Decimal(bowlruns[i]/oversbowled[i])
    economy[i]=round(economy[i],2)
fowover=[]
for i in range(len(fowball)):
    rouver=int(fowball[i]/6)
    rouver1=int(fowball[i]%6)
    roustr=str(rouver)+"."+str(rouver1)
    fowover.append(roustr)
totalovers=int(totalballsbowled/6)
f=open("scorecard.txt","w")
f.write("KINGS XI PUNJAB Innings\t\t\t\t\t\t\t"+str(currentruns)+"-"+str(totalwickets)+"("+str(totalovers)+")"+"\n")
f.write("Batsman\t\t\t\t\t\tR\tB\t4s\t6s\tSR\n")
for i in range(len(batsmen)):
    f.write(str(batsmen[i])+"\t"+str(status[i])+"\t"+str(batruns[i])+"\t"+str(ballsfaced[i])+"\t"+str(boundaries[i])+"\t"+str(sixes[i])+"\t"+str(strikerate[i])+"\n")
f.write("Extras\t\t\t\t\t\t"+str(totalnoballs+wides+legbyes+byes+penalty)+"(b "+str(byes)+",lb "+str(legbyes)+",w "+str(wides)+",nb "+str(totalnoballs)+",p "+str(penalty)+")"+"\n")
f.write("Total\t\t\t\t\t\t"+str(currentruns)+"("+str(totalwickets)+" wkts, "+str(totalovers)+" Ov)\n")
f.write("Fall of Wickets\n")
i=len(fowwickets)-1
while(i>0):
    f.write(str(fowruns[i])+"-"+str(fowwickets[i])+"("+str(fowbatsman[i])+", "+str(fowover[i])+"), ")
    i=i-1
f.write(str(fowruns[i])+"-"+str(fowwickets[i])+"("+str(fowbatsman[i])+", "+str(fowover[i])+")\n")
f.write("Bowler\t\t\t\tO\tM\tR\tW\tNB\tWD\tECO\n")
for i in range(len(bowlers)):
    f.write(str(bowlers[i])+"\t\t\t"+str(oversbowled[i])+"\t"+str(maidens[i])+"\t"+str(bowlruns[i])+"\t"+str(wickets[i])+"\t"+str(noballs[i])+"\t"+str(widesbowled[i])+"\t"+str(economy[i])+"\n")
f.close()
        
            