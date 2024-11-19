# main.py

import os
import random
import time
import json
import msvcrt  # Windows-only; replace for cross-platform compatibility

from constants import SAVE_FOLDER, FOOD_DICT, EXERCISE_DICT, MEDICATION_DICT, DEFAULT_STATS
from faces import FACES

# -------------------- ANIMATIONS --------------------

def fat_animation():
    """Displays the 'stuffed' animation using a sequence of faces."""
    animation_faces = [3, 4]  # Sequence of faces for the animation
    message = "Urghhh, I'm stuff'd"  # Message to display with each frame

    for face_no in animation_faces:
        if face_no in FACES:  # Ensure the face exists in FACES
            print_face(face_no)
            print(message)
            time.sleep(0.5)
        else:
            print(f"Face {face_no} not found in FACES!")

def eating_animation():
    """Displays the eating animation using a sequence of faces."""
    word = random.randint(1, 3)  # Randomly select a eating message

    for _ in range(2):  # Loop animation twice
        for face_no in range(6, 11):  # Loop through face numbers 6 to 10
            if face_no in FACES:  # Ensure the face exists in FACES
                print_face(face_no)
                print(FOOD_DICT[word])
                time.sleep(0.5)
            else:
                print(f"Face {face_no} not found in FACES!")

def exercise_animation():
    """Displays the exercise animation using dynamic faces."""
    word = random.randint(1, 3)  # Randomly select a exercise message

    # Sequence of face numbers for the animation
    animation_faces = [18, 19, 20, 19]

    for _ in range(2):  # Loop animation twice
        for face_no in animation_faces:
            print_face(face_no)
            print(EXERCISE_DICT[word])
            time.sleep(0.5 if face_no == 19 else 0.6)  # Adjust timing

def wash_animation():
    """Displays the 'washing' animation using a sequence of faces."""
    animation_faces = [22, 23, 24, 25, 24, 23]  # Sequence of face numbers
    message = "Brush brush brush"  # Message to display with each frame

    for _ in range(2):  # Loop animation twice
        for face_no in animation_faces:
            if face_no in FACES:  # Ensure the face exists in FACES
                print_face(face_no)
                print(message)
                time.sleep(0.3)
            else:
                print(f"Face {face_no} not found in FACES!")

def sleep_animation(character):
    """Displays the 'sleeping' animation using a sequence of faces."""
    for _ in range(3):  # Loop animation three times
        for face_no in range(28, 31):  # Loop through face numbers 28 to 30
            if face_no in FACES:  # Ensure the face exists in FACES
                print_face(face_no)
                print(f"{character} is going to sleep! Good night and see you tomorrow...")
                time.sleep(1)
            else:
                print(f"Face {face_no} not found in FACES!")

def medication_animation():
    """Displays the medication animation using a sequence of faces and messages."""
    word = random.randint(1, 3)  # Randomly select a eating message

    for _ in range(2):  # Loop animation twice
        for face_no in range(14, 18):  # Loop through face numbers 14 to 17
            if face_no in FACES:  # Ensure the face exists in FACES
                print_face(face_no)
                print(MEDICATION_DICT[word])
                time.sleep(0.5)
            else:
                print(f"Face {face_no} not found in FACES!")

    # Final happy face after medication
    print_face(10)
    print("Ah, much better!")
    time.sleep(1)

def print_face(face_no):
    """Print the face corresponding to the face number."""
    os.system("cls")
    face = FACES.get(face_no, [])  # Retrieve the face by number

    if not face:
        print("Face not found!")
        return

    for row in face:
        for cell in row:
            if cell == 1:
                print("\u2592\u2592", end="")
            else:
                print("  ", end="")
        print("")

def play_idle_frame(stats, current_hour, current_frame):
    """
    Displays a single frame of the idle animation.

    Args:
        stats (dict): Tamagotchi's current stats.
        current_hour (int): Current hour for time-sensitive animations.
        current_frame (int): The current animation frame.

    Returns:
        int: The updated animation frame.
    """
    idle_sequences = {
        "dirty": [12, 13],
        "sick": [5],
        "sleepy": [26, 27],
        "sleeping": [28, 29],
        "high_fitness": [1, 2],
        "low_fitness": [3, 4],
    }
    if stats["asleep"]:
        sequence = idle_sequences["sleeping"]
    elif stats["sick"]:
        sequence = idle_sequences["sick"]
    elif stats["dirty"]:
        sequence = idle_sequences["dirty"]
    elif current_hour >= 21: # Sleepy at 9PM system time
        sequence = idle_sequences["sleepy"]
    elif stats["fitness"] >= 7:
        sequence = idle_sequences["high_fitness"]
    else:
        sequence = idle_sequences["low_fitness"]

    # Ensure current_frame is within bounds for the chosen sequence
    current_frame %= len(sequence)

    # Display the current frame
    print_face(sequence[current_frame])

    # Display the idle screen with options
    display_idle_screen(stats)

    time.sleep(0.5)  # Adjust animation speed

    # Update the frame index for the next call
    return (current_frame + 1) % len(sequence)

# -------------------- GAME LOGIC --------------------

def initialize():
    """
    Initialize the game by asking the user to load a saved character or create a new one.

    Returns:
        tuple: The name of the character and their stats.
    """
    os.system("cls")
    print("Welcome to Tamagotchi!")

    # Ensure the saves folder exists
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    # Get list of saved files
    saved_files = [f for f in os.listdir(SAVE_FOLDER) if f.endswith(".json")]

    # Only prompt to load if there are saved files
    if saved_files:
        choice = input("Do you want to load a saved character? (y/n): ").strip().lower()
        if choice == 'y':
            print("Available saved characters:")
            for i, file in enumerate(saved_files, 1):
                print(f"{i}. {file[:-5]}")  # Display file names without the ".json" extension

            # Allow the user to choose a file
            try:
                selected_index = int(input("Enter the number of the character to load: ")) - 1
                if 0 <= selected_index < len(saved_files):
                    character = saved_files[selected_index][:-5]
                    stats = load(character)
                    return character, stats
                else:
                    print("Invalid selection. Starting with a new character.")
            except ValueError:
                print("Invalid input. Starting with a new character.")

    # Create a new character with default stats
    character = input("Please input a name for your character: ").strip()
    print(f"{character}, that's a great name!")
    time.sleep(3)

    return character, DEFAULT_STATS

def process_input(key_char, stats, character, current_hour):
    """
    Handles player input and performs the corresponding actions.

    Args:
        key_char (str): Character of the pressed key (e.g., 'a', 'b', etc.).
        stats (dict): Tamagotchi's current stats.
        character (dict): Tamagotchi's character information.
        current_hour (int): Current hour of the day (24-hour format) used for time-dependent logic.
    """

    if key_char == 'a':  # Eat
        handle_eat(stats)
    elif key_char == 'b':  # Poop / Clean
        stats = handle_poop_clean(stats)
    elif key_char == 'c':  # Exercise
        handle_exercise(stats)
    elif key_char == 'd':  # Sleep
        handle_sleep(stats, character, current_hour)
    elif key_char == 'e':  # Medication
        handle_medication(stats)
    elif key_char == 'x':  # Quit
        handle_quit(character, stats)
    return stats

def display_idle_screen(stats):
    """Display the idle screen options and current status."""
    print("------------------------------")
    print("A: Eat")
    if stats["dirty"]:
        print("B: Clean")
    else:
        print("B: Poop")
    print("C: Exercise")
    print("D: Sleep")
    if stats["sick"]:
        print("E: Medication")
    print("X: Quit")
    print("------------------------------")

def save(character, stats):
    """
    Save the current stats of a character to a file.

    Args:
        character (str): The name of the character.
        stats (dict): The stats to save.

    Returns:
        None
    """
    save_path = os.path.join(SAVE_FOLDER, f"{character}.json")

    # Ensure the saves folder exists
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    # Save the stats as JSON
    with open(save_path, "w") as f:
        json.dump(stats, f, indent=4)

    print(f"{character}'s stats have been saved successfully!")

def load(character):
    """
    Load stats for a character from a file.

    Args:
        character (str): The name of the character.

    Returns:
        dict: The loaded stats for the character.
    """
    save_path = os.path.join(SAVE_FOLDER, f"{character}.json")

    if os.path.exists(save_path):
        with open(save_path, "r") as f:
            stats = json.load(f)
        print(f"Stats for {character} loaded successfully!")
        return stats
    else:
        print(f"No save file found for {character}. Initializing default stats.")
        return DEFAULT_STATS

def handle_eat(stats):
    """Handle the eat action."""

    if stats["hunger"] == 0:
        print_face(11)
        print("Urghhh, I'm too full!")
        time.sleep(3)

    else:
        # Show the eating animation
        eating_animation()

        # Decrease hunger level
        stats["hunger"] = max(stats["hunger"] - 3, 0)  # Ensure hunger doesn't drop below 0

        # Decrease fitness level
        stats["fitness"] = max(stats["fitness"] - 3, 0)  # Ensure fitness doesn't drop below 0

        # Able to poop after eating
        stats["bowel"] = True
    return stats

def handle_poop_clean(stats):
    """Handle the poop or clean action."""

    if stats["dirty"]:  # Perform cleaning
        stats["dirty"] = False

        wash_animation()
        print_face(1)
        print("I'm all clean now!")
        time.sleep(3)

    elif stats["bowel"]:  # If bowel is True, perform a poop action
        stats["bowel"] = False
        stats["dirty"] = True
        msg = ""
        for _ in range(3):  # Loop animation three time
            print_face(3)
            msg += ". . . "
            print(msg)
            time.sleep(1)

    else:  # If no need to poop
        print_face(4)
        print("But I don't wanna go!")
        time.sleep(3)
    return stats

def handle_exercise(stats):
    """Handle the exercise action."""
    stats["fitness"] += 1
    exercise_animation()
    return stats

def handle_sleep(stats, character, current_hour):
    """
    Handle the sleep action for Tamagotchi.

    Args:
        stats (dict): The current stats of the Tamagotchi.
        character (str): The name of the Tamagotchi character.
        current_hour (int): The current hour for determining sleep readiness.

    Returns:
        dict: Updated stats after handling the sleep action.
    """
    if 20 <= current_hour <= 24:  # Allow sleep between 8 PM and 12 PM
        sleep_animation(character)  # Call the sleep animation
        stats["asleep"] = True

        # Reset relevant stats to reflect the effect of sleep
        stats["fitness"] = min(stats["fitness"] + 2, 10)  # Boost fitness but max at 10
        stats["hunger"] = min(stats["hunger"] - 2, 0)     # Hunger decreases slightly but min at 0

        handle_quit(character, stats)
    else:
        print_face(3)
        print("It's too early! I don't wanna sleep!")
        time.sleep(3)

    return stats

def handle_forced_sleep(stats, character):
    """
    Handle the scenario where the Tamagotchi is forced to sleep due to neglect.

    Args:
        stats (dict): The Tamagotchi's stats.
        character (str): The name of the Tamagotchi character.
    """
    print(f"Where were you!? {character} was up all night waiting for you!")

    # Drop stats due to neglect
    stats["fitness"] = max(stats["fitness"] - 3, 0)  # Fitness decreases but min at 0
    stats["hunger"] = min(stats["hunger"] + 3, 10)   # Hunger increases but max at 10
    stats["sick"] = True  # Tamagotchi becomes sick
    stats["asleep"] = True  # Force sleep status

    time.sleep(3)
    handle_already_asleep(character, stats)

def handle_already_asleep(character, stats):
    """
    Handle the scenario where the Tamagotchi is already asleep.

    Args:
        character (str): The name of the Tamagotchi character.
        stats (dict): The Tamagotchi's stats.
    """
    print_face(28)  # Display a sleeping face
    print(f"{character} is asleep right now! Come back after 08:00 AM.")
    time.sleep(3)

    # Save progress and quit
    handle_quit(character, stats)

def handle_medication(stats):
    """Handle the medication action for Tamagotchi."""
    if stats["sick"]:  # Check if Tamagotchi is sick
        medication_animation()  # Show medication animation

        # Cure sickness
        stats["sick"] = False  

        # Reset both fitness and hunger
        stats["fitness"] = 3
        stats["hunger"] = 7

        print_face(1)
        print("I feel much better now!")
        time.sleep(3)
    else:
        print_face(3)
        print("But I'm not sick!")
        time.sleep(3)

    return stats        

def handle_death(character):
    """Handle the death of the Tamagotchi."""
    print_face(21)
    print(f"Game Over. {character} has died.")

    save_path = os.path.join(SAVE_FOLDER, f"{character}.json")
    if os.path.exists(save_path):
        os.remove(save_path)
        print(f"Save file for {character} has been deleted.")
    else:
        print(f"No save file found for {character} to delete.")
    print("Thanks for playing!")
    exit()

def handle_hourly_events(character, stats, current_hour):
    """Handle scheduled events and stat updates based on time."""
    if current_hour != stats["last_hour"]:
        drop_stats = 1
        # Stats worsten twice as fast when dirty or sick
        if stats["dirty"]:
            drop_stats = 2

        # Update hunger, fitness, and dirty stats
        stats["hunger"] = min(stats["hunger"] + drop_stats, 10)  # Hunger increases, max 10
        stats["fitness"] = max(stats["fitness"] - drop_stats, 0) # Fitness decreases, min 0

        # Check if hunger or fitness is at 0 for an hour
        if stats["hunger"] == 0 or stats["fitness"] == 0:
            if not stats["sick"]:  # Only set sick if not already sick
                stats["sick"] = True
                stats["sick_timer"] = current_hour

        # Check if Tamagotchi is sick for 2 hours
        if stats["sick"]:
            sick_duration = (current_hour - stats["sick_timer"]) % 24
            if sick_duration >= 2:
                handle_death(character)

        # Update last_hour after processing
        stats["last_hour"] = current_hour

    return stats

def handle_quit(character, stats):
    """Handle quitting the game."""
    save(character, stats)
    print("Game saved! Goodbye!")
    exit()

# -------------------- MAIN GAME LOOP --------------------

def main():
    """
    Main function to run the Tamagotchi game.
    Plays idle animations while continuously checking for player input.
    """
    character, stats = initialize()
    current_idle_frame = 0  # To track which idle animation frame to show
    current_hour = int(time.strftime("%H"))

    # Player logs in after Tamagotchi is already asleep
    if stats["asleep"]:
        handle_already_asleep(character, stats)
    # Player has logged in past 12PM, before 8AM and Tamagotchi was not asleep 
    elif 20 <= current_hour <= 24 or 0 <= current_hour <= 7:
        handle_forced_sleep(stats, character)

    # Idle animation and await user input
    try:
        while True:
            # Get the current hour
            current_hour = int(time.strftime("%H"))

            # DEVELOPER: Change from hour to seconds for testing
            #current_hour = int(time.strftime("%S"))

            # Handle scheduled events
            stats = handle_hourly_events(character, stats, current_hour)

            # Play a single frame of the idle animation
            current_idle_frame = play_idle_frame(
                stats, current_hour, current_idle_frame
            )

            # Check for user input
            if msvcrt.kbhit():
                ch = msvcrt.getch().decode('utf-8').lower()  # Decode the input and convert to lowercase
                stats = process_input(ch, stats, character, current_hour)

            # Clear the input buffer (for responsiveness)
            while msvcrt.kbhit():
                msvcrt.getch()

            # Add a small delay to avoid high CPU usage
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\nCtrl+C detected. Saving your progress...")
        handle_quit(character, stats)

if __name__ == "__main__":
    main()
