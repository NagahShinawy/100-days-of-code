class Contact:
    REASONS = ["COMPLAIN", "SUGGEST", "INFO"]

    def __init__(self, reason, description):
        self.reason = reason
        self.description = description

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, reason):
        if reason not in self.REASONS:
            raise ValueError(f"Reason should be one of ({','.join(self.REASONS)})")
        self._reason = reason

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if len(description) < 10:
            raise ValueError("Description should be at least 10 chars")
        self._description = description

    def __repr__(self):
        return f"[{self.reason}] - [{self.description}]"
