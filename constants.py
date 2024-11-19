# constants.py

import time

SAVE_FOLDER = "saves"

FOOD_DICT = {1: "Nom nom nom!", 2: "Delicious!", 3: "Yummy!"}
EXERCISE_DICT = {1: "One! Two! One! Two!", 2: "Ready! Go!", 3: "Yaaaaaaaah!"}
MEDICATION_DICT = {1: "Glug glug glug", 2: "Yuck!", 3: "Cough... cough..."}

DEFAULT_STATS = {
    "fitness": 5,
    "hunger": 5,
    "bowel": False,
    "sick": False,
    "dirty": False,
    "asleep": False,
    "last_hour": int(time.strftime("%H"))
}