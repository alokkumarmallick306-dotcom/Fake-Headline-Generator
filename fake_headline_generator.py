import random

subjects = [
    "Shahrukh khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A Group of monkeys",
    "Prime Ministed Modi",
    "Auto Rickshaw Driver from Delhi",
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
]

places_or_things =[
    "at Red Fort",
    "in Mumbai Local Train",
    "a plote of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at  India Gate",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)
    user_input = input("\nDo you want another headline? (yes/no)").strip()
    if user_input == "no":
        break

    print("\nThank you for using the Fake Headline Generator!")