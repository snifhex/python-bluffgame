from typing import NoReturn

class Player:
    def __init__(self, userid:str, username:str, cards=None) -> NoReturn:
        self.id = userid
        self.username = username
        self.cards = cards

    def __str__(self) -> str:
        return f"UserId: {self.id}, UserName: {self.username}, TotalCards: {len(self.cards)}"
