import fileinput
import re

test_string = "Game 1: 19 blue, 12 red; 19 blue, 2 green, 1 red; 13 red, 11 blue"

cubes = {"red": 12, "green": 13, "blue": 14}


def get_game_info(gameString):
    gameID = re.findall(r"^Game\s\d+", gameString)[0].split(" ")[1]
    redCubes = [sub.replace(" red", "") for sub in re.findall(r"\d+\sred", gameString)]
    redCubes = [int(i) for i in redCubes]
    greenCubes = [
        sub.replace(" green", "") for sub in re.findall(r"\d+\sgreen", gameString)
    ]
    greenCubes = [int(i) for i in greenCubes]
    blueCubes = [
        sub.replace(" blue", "") for sub in re.findall(r"\d+\sblue", gameString)
    ]
    blueCubes = [int(i) for i in blueCubes]
    return {
        "gameID": gameID,
        "redCubes": redCubes,
        "greenCubes": greenCubes,
        "blueCubes": blueCubes,
    }


def check_if_valid_game(gameDict):
    if (
        sum(gameDict["redCubes"]) <= cubes["red"]
        and sum(gameDict["blueCubes"]) <= cubes["blue"]
        and sum(gameDict["greenCubes"]) <= cubes["green"]
    ):
        possible_games += gameDict["gameID"]


possible_games = 0
for line in fileinput.input():
    print(check_if_valid_game((get_game_info(line))))
