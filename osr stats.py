import random

def d8():
    return random.randint(1,8)

def d6():
    return random.randint(1,6)

def d4():
    return random.randint(1,4)

def getOneStat():
    rolls = []
    rolls.append(d6())
    rolls.append(d6())
    rolls.append(d6())
    return sum(rolls)

# Roll 3d6.
def getStats():
    stats = []
    for _ in range(6):
        stats.append(getOneStat())
    stats.sort()
    return stats

# Get reduced point buy to match 3d6.
def getRandomPointBuyStats():
    stats = []
    points = 17
    for _ in range(6):
        stats.append(getOneStat())
    
    s18 = stats.count(18)
    s17 = stats.count(17)
    s16 = stats.count(16)
    s15 = stats.count(15)
    s14 = stats.count(14)
    s13 = stats.count(13)
    s12 = stats.count(12)
    s11 = stats.count(11)
    s10 = stats.count(10)
    s9 = stats.count(9)
    s8 = stats.count(8)
    s7 = stats.count(7)
    s6 = stats.count(6)
    s5 = stats.count(5)
    s4 = stats.count(4)
    s3 = stats.count(3)

    pointsUsed = s18*19+s17*15+s16*12+s15*9+s14*7+s13*5+s12*4+s11*3+s10*2+s9*1+s7*(-1)+s6*(-2)+s5*(-4)+s4*(-6)+s3*(-9)
    if(pointsUsed == points):
        stats.sort()
        return stats
    else:
        return getRandomPointBuyStats()

def averagePointBuyStats():
    stats = []
    for _ in range(10000):
        setOfStats = getRandomPointBuyStats()
        for i in setOfStats:
            stats.append(i)
    return sum(stats)/len(stats)


def countNumberOfOccurencesPointBuy(n):
    stats = []
    for _ in range(n):
        stats.extend(getRandomPointBuyStats())

    for i in range(3,19):
        print(f"{i}: {stats.count(i)}")

def countNumberOfOccurences3d6(n):
    stats = []
    for _ in range(n):
        stats.extend(getStats())

    for i in range(3,19):
        print(f"{i}: {stats.count(i)}")


print(getRandomPointBuyStats())