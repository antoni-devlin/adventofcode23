import fileinput
import re

test_string = "Game 1: 19 blue, 12 red; 19 blue, 2 green, 1 red; 13 red, 11 blue"

cubes = {"red": 12, "green": 13, "blue": 14}


def get_game_info(gameString):
    gameID = re.findall(r"^Game\s\d+", gameString)[0].split(" ")[1]
    redCubes = [sub.replace(" red", "") for sub in re.findall(r"\d+\sred", gameString)]
    greenCubes = [
        sub.replace(" green", "") for sub in re.findall(r"\d+\sgreen", gameString)
    ]
    blueCubes = [
        sub.replace(" blue", "") for sub in re.findall(r"\d+\sblue", gameString)
    ]
    return gameID, redCubes, greenCubes, blueCubes


print(get_game_info(test_string))

# for line in fileinput.input():
#     print(line)
