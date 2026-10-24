
from datetime import datetime
from pathlib import Path

# Find the folder where this Python file is saved.
PROJECT_FOLDER = Path(__file__).parent

# File where we will save our experiment results.
RESULTS_FILE = PROJECT_FOLDER / "experiment_results.md"

# Three prompts for the same creative task.
PROMPTS = {
    "A": """Generate 5 startup ideas for college students.""",

    "B": """Act as a startup mentor for college students.

Generate 5 practical startup ideas that students can
test with a small budget.

For each idea, include:
1. Name
2. Problem solved
3. Target users
4. How it works
5. What makes it different
6. One way to test it

Use simple English and clear formatting.""",

    "C": """Act as a creative startup mentor for college students.

Example:
Name: CampusSwap
Problem: Students have unused textbooks.
Solution: A student marketplace for exchanging
or selling used textbooks.
Difference: It focuses on the campus community.

Now generate 5 NEW startup ideas for college students.

For each idea, include its name, problem, solution,
target users, unique feature, and first testing step.

Make the ideas practical, original, and easy to understand.
Do not copy the example."""
}


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 45)
    print("       CREATIVE PROMPT TESTING STUDIO")
    print("=" * 45)
    print("1. View a prompt")
    print("2. Record an AI result")
    print("3. View saved results")
    print("4. Exit")


def choose_prompt():
    """Let the user select prompt A, B, or C."""
    print("\nAvailable prompts: A, B, C")
    choice = input("Choose a prompt: ").strip().upper()

    if choice not in PROMPTS:
        print("Invalid choice. Please select A, B, or C.")
        return None

    return choice


def view_prompt():
    """Show the selected prompt on the screen."""
    choice = choose_prompt()

    if choice is None:
        return

    print(f"\n--- PROMPT {choice} ---")
    print(PROMPTS[choice])
    print("\nCopy this prompt into ChatGPT to test it.")


def record_result():
    """Save an AI response and its quality scores."""
    choice = choose_prompt()

    if choice is None:
        return

    print("\nFirst, copy the prompt shown below into ChatGPT.")
    print("\n--- PROMPT ---")
    print(PROMPTS[choice])

    print(
        "\nPaste the actual ChatGPT response below."
        "\nType END on a new line when finished."
    )

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    ai_output = "\n".join(lines).strip()

    if not ai_output:
        print("No output entered. Nothing was saved.")
        return

    print("\nScore the actual AI response from 1 to 5.")

    criteria = [
        "Creativity",
        "Relevance",
        "Tone",
        "Level of detail"
    ]

    scores = {}

    for criterion in criteria:
        while True:
            try:
                score = int(input(f"{criterion} (1-5): "))

                if 1 <= score <= 5:
                    scores[criterion] = score
                    break

                print("Please enter a number from 1 to 5.")

            except ValueError:
                print("Invalid input. Please enter a whole number.")

    total = sum(scores.values())
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Prepare the experiment record in Markdown format.
    record = f"""
## Prompt {choice} — Experiment

**Date:** {date}

### Prompt Used
{PROMPTS[choice]}

### Actual AI Output
{ai_output}

### Evaluation Scores

| Criterion | Score (out of 5) |
|---|---:|
| Creativity | {scores['Creativity']} |
| Relevance | {scores['Relevance']} |
| Tone | {scores['Tone']} |
| Level of detail | {scores['Level of detail']} |
| **Total** | **{total}/20** |

### Observation
Write your own observation about this result.

---
"""

    # Add the record to the results file.
    with RESULTS_FILE.open("a", encoding="utf-8") as file:
        file.write(record)

    print(f"\nResult saved successfully to: {RESULTS_FILE}")
    print(f"Total score: {total}/20")


def view_results():
    """Display the saved experiment results."""
    if not RESULTS_FILE.exists():
        print("\nNo results file found yet.")
        return

    content = RESULTS_FILE.read_text(encoding="utf-8")

    if not content.strip():
        print("\nNo experiments saved yet.")
    else:
        print("\n--- SAVED EXPERIMENT RESULTS ---")
        print(content)


def main():
    """Run the program until the user chooses Exit."""
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            view_prompt()
        elif choice == "2":
            record_result()
        elif choice == "3":
            view_results()
        elif choice == "4":
            print("\nThank you for using the Prompt Testing Studio!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


# Start the program.
if __name__ == "__main__":
    main()
    

