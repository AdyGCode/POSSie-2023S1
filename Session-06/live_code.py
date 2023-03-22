# Live Coding 2023-03-15
def lyric(activity_item):
    activity = activity_item
    action_end = ""
    if isinstance(activity_item, dict):
        for key, value in activity_item.items():
            activity = key
            action_end = value
    line_end = ("doo-doo, " * 3)[:-2]
    for lyric_line in range(0, 3):
        print(f"{activity}, {line_end}")
        activity_line = f"{activity} ({action_end})"
    print(f"{activity_line}")
    print()


def sing_along():
    action_list = ["Baby Shark", "Mommy Shark", "Daddy Shark",
                   "Grandma Shark", "Grandad Shark",
                   "Shakespear Shark", "We all play",
                   "Let's go hunt", {"Run away": "ah!"},
                   {"Safe at last": "phew"}, "It's the end"]
    for action in action_list:
        lyric(action)


if __name__ == "__main__":
    sing_along()
