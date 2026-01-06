from datetime import datetime
from typing import Optional


class Task:
    _id_counter = 1

    def __init__(
        self,
        title: str,
        priority: int = 1,
        due_date: Optional[datetime] = None,
    ) -> None:
        # Validation
        # ---- Title ----
        if not title or not title.strip():
            raise ValueError("Task title can't be empty")

        # ---- priority ----
        if not isinstance(priority, int):
            raise ValueError(f"Priority must be an Integer, got {type(priority)}")
        if not (1 <= priority <= 5):
            raise ValueError(f"Priority must be 1-5, got {priority}")

        # ---- Due Date ----
        if due_date is not None:
            year, month, day = map(int, due_date.split(","))
            self.due_date = datetime(year, month, day)
        else:
            self.due_date = None

        # Instance properties
        self.title = title
        self.priority = priority
        self.completed = False
        self.completed_at = None
        self.id = Task._id_counter

        # Increment Task Counter
        Task._id_counter += 1

    # Instance Methods
    def complete(self):
        self.completed = True
        self.completed_at = datetime.now()

    def is_overdue(self):
        if self.due_date is None or self.completed:
            return False
        return datetime.now() > self.due_date

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed,
            "completed_at": self.completed_at,
            "due_date": self.due_date,
        }

    # Magic Methods
    def __repr__(self) -> str:
        return f"Task(title={self.title}, priority={self.priority})"

    def __str__(self) -> str:
        status = "[✓]" if self.completed else "[○]"
        return f"{status} {self.title} (priority: {self.priority})"

    def __eq__(self, other) -> bool:
        if not isinstance(self, other):
            return NotImplementedError
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    # Class methods
    @classmethod
    def reset_counter(cls):
        cls._id_counter = 1

    @classmethod
    def from_dict(cls, data):
        task = cls(title=data["title"], priority=data["priority"])
        task.id = data["id"]
        return task
