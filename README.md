# Stat Generator for Dungeons and Dragons
This project provides a set of Python functions to generate and analyze character stats for Dungeons and Dragons (D&D). The stats are generated using a combination of various methods, including rolling dice and point buy systems.

## Why This Script?

I created this script to have a way of generating stats for Dungeons and Dragons characters that combines the fun of randomness from dice rolls with the possibility of achieving very high (16, 17, 18) and very low (down to 3) stats. This approach maintains the rarity of extreme stats while also incorporating the balance that systems like point buy provide.

## Features

- **Dice Roll Methods**: Functions to simulate rolling different types of dice (d4, d6, d8).
- **Stat Generation**: Functions to generate individual stats and sets of stats using different methods.
- **Point Buy System**: Functions to generate stats using the point buy system and analyze the number of rolls required to achieve a valid set of stats.
- **Stat Analysis**: Functions to calculate average stats and count occurrences of specific stats.

## Functions

### Dice Roll Functions

- `d8()`: Rolls an 8-sided die.
- `d6()`: Rolls a 6-sided die.
- `d4()`: Rolls a 4-sided die.

### Stat Generation Functions

- `getOneStat()`: Generates a single stat by rolling four 6-sided dice and summing the highest three rolls.
- `getStats()`: Generates a set of six stats using the above method.
- `getStatsBetween70and74()`: Generates a set of six stats, ensuring the sum of the stats is between 70 and 74.
- `getOneStatOSR()`: Generates a single stat by rolling three 6-sided dice.
- `getStatsOSR()`: Generates a set of six stats using the OSR method (rolling three 6-sided dice for each stat).

And my favourites:
- `getRandomPointBuyStats()`: Generates a set of six sets by rolling four 6-sided dice and summing the highest three rolls for each stat until the six stats generated follow the rules for an extended point buy system where all stats possible to roll (3 to 18) are allowed.
- `getRandomPointBuyStatsOSR()`: Generates a set of six stats using the OSR method but ensuring the stats align with a reduced point buy system.

### Stat Analysis Functions

- `averageStat()`: Calculates the average value of a single stat over 100,000 trials.
- `averageStats()`: Calculates the average value of a set of stats over 10,000 trials.
- `averagePointBuyStats()`: Calculates the average value of stats generated using the point buy system over 10,000 trials.
- `averageNumberOfRollsBeforeRandomPointBuyStatsSucceeds()`: Calculates the average number of rolls required to achieve a valid set of stats using the point buy system over 10,000 trials.
- `countNumberOfOccurencesPointBuy(n)`: Counts the occurrences of each stat value in `n` sets of stats generated using the point buy system.

## Usage
### Using the Script in the Terminal
Running the script directly uses the `getRandomPointBuyStats()` and `getRandomPointBuyStatsOSR()` functions.

To generate OSR stats, use the `--osr` flag:

```sh
python stats.py --osr
```

To generate multiple sets of stats, use the `--amount` flag:

```sh
python stats.py --amount 5
```

You can combine flags to generate multiple sets of OSR stats:

```sh
python stats.py --osr --amount 5
```

### Using the functions in your own Python projects

To use the functions, simply import the `stats.py` module and call the desired functions. For example:

```python
from stats import getRandomPointBuyStats

print(getRandomPointBuyStats())
```



## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Contact

For any questions or suggestions, please contact Anders Kristoffersen.
