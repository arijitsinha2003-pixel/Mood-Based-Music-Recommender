
import random

# Mood-based music collection
music = {
    "happy": [
        "Happy - Pharrell Williams",
        "On Top of the World - Imagine Dragons",
        "Perfect - Ed Sheeran"
    ],

    "sad": [
        "Let Her Go - Passenger",
        "Someone Like You - Adele",
        "Channa Mereya - Arijit Singh"
    ],

    "romantic": [
        "Kesariya - Arijit Singh",
        "Raataan Lambiyan - Jubin Nautiyal",
        "Heeriye - Jasleen Royal"
    ],

    "motivated": [
        "Believer - Imagine Dragons",
        "Zinda - Siddharth Mahadevan",
        "Kar Har Maidaan Fateh - Sukhwinder Singh"
    ],

    "relaxed": [
        "Husn - Anuv Jain",
        "Kho Gaye Hum Kahan - Jasleen Royal",
        "Until I Found You - Stephen Sanchez"
    ]
}

messages = {
    "happy": "Keep smiling! Spread your happiness.",
    "sad": "Every difficult day will pass. Stay strong!",
    "romantic": "Enjoy the beautiful feeling of love!",
    "motivated": "Believe in yourself. You can do it!",
    "relaxed": "Take a deep breath and enjoy the moment."
}

print("=" * 45)
print("       MOOD-BASED MUSIC RECOMMENDER")
print("=" * 45)

while True:

    print("\nAvailable moods:")
    print("1. Happy")
    print("2. Sad")
    print("3. Romantic")
    print("4. Motivated")
    print("5. Relaxed")
    print("6. Exit")

    choice = input("\nChoose your mood: ")

    moods = {
        "1": "happy",
        "2": "sad",
        "3": "romantic",
        "4": "motivated",
        "5": "relaxed"
    }

    if choice == "6":
        print("Thanks for using Music Recommender!")
        break

    if choice not in moods:
        print("Invalid choice! Try again.")
        continue

    mood = moods[choice]

    print("\nYour mood:", mood.upper())
    print("\nRecommended songs:")

    # Display three random songs
    recommendations = random.sample(
        music[mood],
        min(3, len(music[mood]))
    )

    for index, song in enumerate(recommendations, 1):
        print(f"{index}. {song}")

    print("\nMessage:", messages[mood])

    print("\nEnjoy your music!")
