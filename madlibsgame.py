# 🎭 Advanced Mad Libs Game

import random
import time

print("=" * 50)
print("🎉 Welcome to the Ultimate Mad Libs Game! 🎉")
print("=" * 50)

# Taking user inputs
name = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb1 = input("Enter a verb: ")
place = input("Enter a place: ")
food = input("Enter a type of food: ")
adjective2 = input("Enter another adjective: ")
superpower = input("Enter a superpower: ")

# Story templates
stories = [
    f"""
    One day, {name} found a {adjective1} {animal} in {place}.
    Surprisingly, the {animal} could {verb1} better than anyone else!
    
    Together, they ate {food} and became {adjective2} friends.
    Soon, they discovered they both had the power of {superpower}!
    
    From that day on, they became heroes of {place}.
    """,

    f"""
    In the magical land of {place}, there lived a {adjective1} {animal}.
    Every morning, it loved to {verb1} while eating {food}.
    
    One day, {name} appeared with the amazing power of {superpower}.
    The villagers were shocked by how {adjective2} they were together!
    
    Their adventures became legendary forever.
    """
]

# Loading effect
print("\n📖 Creating your story", end="")
for i in range(5):
    print(".", end="", flush=True)
    time.sleep(0.5)

# Display random story
print("\n")
print("=" * 50)
print("✨ YOUR MAD LIBS STORY ✨")
print("=" * 50)

print(random.choice(stories))

print("=" * 50)
print("🎊 Thanks for Playing! 🎊")