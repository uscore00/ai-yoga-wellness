from rules import RULES


def show_plan(goal):
    if goal not in RULES:
        print("Sorry, that goal is not available.")
        return

    plan = RULES[goal]

    print("\n" + "=" * 45)
    print(f"YOGA PLAN: {goal.upper()}")
    print("=" * 45)

    print(f"\n{plan['description']}\n")

    print("Sequence:")
    for i, pose in enumerate(plan["sequence"], 1):
        print(f"{i}. {pose}")

    print("\nTips:")
    for tip in plan["tips"]:
        print(f"• {tip}")


def main():
    print("🧘 Welcome to Arogya & Ananda 🧘")
    print("\nChoose your goal:")

    goals = list(RULES.keys())

    for i, goal in enumerate(goals, 1):
        print(f"{i}. {goal.capitalize()}")

    choice = input("\nEnter your choice (1-4): ")

    if choice.isdigit() and 1 <= int(choice) <= len(goals):
        selected_goal = goals[int(choice) - 1]
        show_plan(selected_goal)
    else:
        print("Invalid choice. Please run the program again.")


if __name__ == "__main__":
    main()