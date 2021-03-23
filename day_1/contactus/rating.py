class Rate:
    EXCELLENT = (True, False)
    RECOMMENDED = (True, False)
    FEEDBACK = ("VERY SAD", "SAD", "GOOD", "VERY GOOD", "EXCELLENT")

    def __init__(self, is_excellent, is_recommended, feedback):
        self.is_excellent = is_excellent
        self.is_recommended = is_recommended
        self.feedback = feedback

    @property
    def is_excellent(self):
        return self._is_excellent

    @is_excellent.setter
    def is_excellent(self, is_excellent):
        if is_excellent not in self.EXCELLENT:
            raise ValueError(
                f"<is_excellent> should be one of <{self.EXCELLENT}> not {is_excellent.__class__.__name__}"
            )
        self._is_excellent = is_excellent

    def __repr__(self):
        return f"[{self.feedback}]"
