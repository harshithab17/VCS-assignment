"""
This program prints a welcome message and displays today's tasks.
It includes a helper function to check whether the task list is empty.
This docstring was generated using AI as part of Phase IV documentation.
The script demonstrates functions, lists, and conditional logic.
"""

def is_task_list_empty(tasks):
    """
    Returns True if the provided task list is empty.
    Used as a helper validator function for the VCS assignment.
    """
    return len(tasks) == 0


def greet():
    print("Hello! This is my Phase 1 Git project file.")
    print("Final merged UI version")
    print("This line is for PR demonstration")

    # New enhancement: task list
    tasks = ["Study VCS", "Do assignment", "Push to GitHub"]
    print("Today's tasks:", tasks)

    # Using helper function suggested by Copilot
    if is_task_list_empty(tasks):
        print("No tasks available today!")
    else:
        print("You have tasks to complete today!")


if __name__ == "__main__":
    greet()
