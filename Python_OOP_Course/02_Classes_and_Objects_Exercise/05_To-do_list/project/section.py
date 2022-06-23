from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in [t.name for t in self.tasks]:
            return f"Could not find task with the name {task_name}"

        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task.name}"

    def clean_section(self):
        removed_tasks = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                removed_tasks += 1

        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        view_result = f"Section {self.name}:\n"
        for current_task in self.tasks:
            view_result += current_task.details() + "\n"

        return view_result.strip()
