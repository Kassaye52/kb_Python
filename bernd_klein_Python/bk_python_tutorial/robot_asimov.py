class Robot:
    Three_Laws = (
    """A robot may not injure a human being or, through inaction, allo
    w a human being to come to harm.""",
    """A robot must obey the orders given to it by human beings, excep
    t where such orders would conflict with the First Law.,""",
    """A robot must protect its own existence as long as such protecti
    on does not conflict with the First or Second Law."""
    )
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year
    # other methods as usual