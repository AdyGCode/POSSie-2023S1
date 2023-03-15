# Live Coding 2023-03-15
def lyric(activity):
    action_ends = {
        "Run away": "ah!",
        "Safe at last": "phew",
    }
    line_end = ("doo-doo, " * 3)[:-2]
    for lyric_line in range(0, 3):
        print(f"{activity}, {line_end}")
    if activity in action_ends:
        activity += f" ({action_ends[activity]})"
    print(f"{activity}")
    print()


def sing_along():
    action_list = ["Baby Shark", "Mommy Shark", "Daddy Shark",
                   "Grandma Shark", "Grandad Shark",
                   "Shakespear Shark", "We all play",
                   "Let's go hunt",
                   "Run away", "Safe at last", "It's the end"]
    for action in action_list:
        lyric(action)


if __name__ == "__main__":
    sing_along()
