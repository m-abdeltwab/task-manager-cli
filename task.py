class Task:
    def __init__(self, title: str, description: str = "", priority: int = 1) -> None:
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
        if not isinstance(priority, int) and not 1 <= priority >= 5:
            raise ValueError(f"Priority must be 1-5, got {priority}")

        # Instance properties
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
