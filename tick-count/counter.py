import time

def calTime(sec):
    hr = 0
    mn = 0
    while(sec>=3600):
        hr += 1
        sec -= 3600
    while(mn>=60):
        mn += 1
        sec -= 60
    return [hr, mn, sec]

def inputFirstTick():
    print("Tell me what time is your first 'Tick'?")
    return [int(input("Hour: ")), int(input("Minute: ")), int(input("Second: "))]

def timeAdd(t1,t2):
    res = [0,0,0]
    res[2] = t1[2] + t2[2]
    while res[2]>=60:
        res[2] -= 60
        res[1] += 1
    res[1] += t1[1] + t2[1]
    while res[1]>=60:
        res[1] -= 60
        res[0] += 1
    res[0] += t1[0] + t2[0]
    while res[0]>=24:
        res[0] -= 24
    return res

tick = ''
timeTable = []
ans = []
count = 0
while(tick == ''):
    tick = input("Press 'ENTER' for tick (w/ other key to stop) ")
    timeTable.append(int(time.time()))
    count += 1
    myTime = calTime(timeTable[count-1]-timeTable[0])
    ans.append(myTime)
    print(f"{count} tick counted at {myTime[0]:02d}:{myTime[1]:02d}:{myTime[2]:02d}")
    print()
    print()
firstTick = inputFirstTick()
ans = [timeAdd(ans[i],firstTick) for i in range(len(ans))]
for i in range(len(ans)-1):
    j = i+1
    while(ans[i]==ans[j]):
        ans[j] = timeAdd(ans[j],[0,0,1])
        j+=1
        if(j==len(ans)):
            break
print("This is your Tick time table . . .")
print(f"Tick No.      Hour:Minute:Second")
for i in range(len(ans)):
    print(f"{i:3d}             {ans[i][0]:02d}:{ans[i][1]:02d}:{ans[i][2]:02d}")
tick = input("For copy to Google sheet press Y/y").lower()
if(tick=='y'):
    print("Hour")
    for i in range(len(ans)):
        print(f"{ans[i][0]:02d}")
    print("Minute")
    for i in range(len(ans)):
        print(f"{ans[i][1]:02d}")
    print("Second")
    for i in range(len(ans)):
        print(f"{ans[i][2]:02d}")
