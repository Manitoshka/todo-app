class Task:
    def __init__(self, title: str, deadline: str, done: bool = False):
        self.title = title
        self.deadline = deadline
        self.done = done

    def to_dict(self):
        return {"title": self.title, "deadline": self.deadline, "done": self.done}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["deadline"], data["done"])

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, deadline):
        self.tasks.append(Task(title, deadline))

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]