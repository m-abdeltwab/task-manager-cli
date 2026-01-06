from datetime import datetime


class Task:
    _id_counter = 1

    def __init__(
        self,
        title: str,
        description: str = "",
        priority: int = 1,
        due_date: datetime = None,
    ) -> None:
        """_summary_

        Args:
            title (str): Task title (required, not-empty)
            description (str, optional): Optional description "".
            priority (int, optional): Priority 1-5 (default 1).

        Raises:
            ValueError: If title is empty or priority invalid
        """

        # Validation
        # ---- Title ----
        if not title or not title.strip():
            raise ValueError("Task title can't be empty")

        # ---- priority ----
        if not isinstance(priority, int) or not 1 <= priority <= 5:
            raise ValueError(f"Priority must be 1-5, got {priority}")

        # ---- Due Date ----
        if due_date is not None:
            year, month, day = map(int, due_date.split(","))
            self.due_date = datetime(year, month, day)
        else:
            self.due_date = None

        # Instance properties
        self.title = title
        self.description = description
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
        if self.due_date is None or not self.completed:
            return False

        return datetime.now() > self.due_date

    # Magic Methods
    def __repr__(self) -> str:
        return f"Task(title={self.title}, priority={self.priority})"

    def __str__(self) -> str:
        status = "[✓]" if self.completed else "[○]"
        return f"{status} {self.title} (priority: {self.priority})"

    # Class methods
    @classmethod
    def reset_counter(cls):
        cls._id_counter = 1


task1 = Task(title="Go to gym", priority=1, due_date="2026, 01, 1")
# task1 = Task(title="Go to gym", priority=1)
print(task1.is_overdue())
task1.complete()
print(task1.is_overdue())
# print(task1.completed)
