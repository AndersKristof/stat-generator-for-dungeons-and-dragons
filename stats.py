import random
import argparse

def d8():
    return random.randint(1,8)

def d6():
    return random.randint(1,6)

def d4():
    return random.randint(1,4)

def pointBuyStat():
    return random.randint(6,16)

def getOneStat():
    rolls = []
    rolls.append(d6())
    rolls.append(d6())
    rolls.append(d6())
    rolls.append(d6())
    rolls.sort()
    rolls.pop(0)
    return sum(rolls)

def getStats():
    stats = []
    for _ in range(6):
        stats.append(getOneStat())
    if(sum(stats) > 74 or sum(stats) < 70):
        return getStats()
    stats.sort()
    return stats

def averageStat():
    stats = []
    for _ in range(100000):
        stats.append(getOneStat())
    return sum(stats)/len(stats)

def averageStats():
    stats = []
    for _ in range(10000):
        setOfStats = getStats()
        for i in setOfStats:
            stats.append(i)
    return sum(stats)/len(stats)

def getRandomPointBuyStats():
    stats = []
    points = 27
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

def getNumberOfRollsBeforeRandomPointBuySucceeds(n):
    stats = []
    points = 27
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
        return n+1
    else:
        return getNumberOfRollsBeforeRandomPointBuySucceeds(n+1)

def averagePointBuyStats():
    stats = []
    for _ in range(10000):
        setOfStats = getRandomPointBuyStats()
        for i in setOfStats:
            stats.append(i)
    return sum(stats)/len(stats)

def averageNumberOfRollsBeforeRandomPointBuyStatsSucceeds():
    numRolls = []
    for _ in range(10000):
        numRolls.append(getNumberOfRollsBeforeRandomPointBuySucceeds(0))
    return sum(numRolls)/len(numRolls)

def countNumberOfOccurencesPointBuy(n):
    stats = []
    for _ in range(n):
        stats.extend(getRandomPointBuyStats())

    for i in range(3,19):
        print(f"{i}: {stats.count(i)}")

def getOneStatOSR():
    rolls = []
    rolls.append(d6())
    rolls.append(d6())
    rolls.append(d6())
    return sum(rolls)

# Roll 3d6.
def getOSRStats():
    stats = []
    for _ in range(6):
        stats.append(getOneStatOSR())
    stats.sort()
    return stats

# Get reduced point buy to match 3d6.
def getRandomPointBuyStatsOSR():
    stats = []
    points = 17
    for _ in range(6):
        stats.append(getOneStatOSR())
    
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
        return getRandomPointBuyStatsOSR()

def main():
    parser = argparse.ArgumentParser(description="Generate D&D stats.")
    parser.add_argument('--amount', type=int, help="Number of sets of stats to generate")
    parser.add_argument('--osr', action='store_true', help="Generate OSR stats")

    args = parser.parse_args()

    if args.osr:
        if args.amount:
            for _ in range(args.amount):
                print(getRandomPointBuyStatsOSR())
        else:
            print(getRandomPointBuyStatsOSR())
        return

    if args.amount:
        for _ in range(args.amount):
            print(getRandomPointBuyStats())
    else:
        print(getRandomPointBuyStats())

if __name__ == "__main__":
    main()