class Keyword:
    def __init__(self, name: str):
        self.name: str = name

    def __str__(self) -> str:
        return self.name

# unit type
Infantry = Keyword("Infantry")

# faction
class FactionKeyword(Keyword):
    pass
AdeptusAstartes = FactionKeyword("Adeptus Astartes")
Necrons = FactionKeyword("Necrons")
