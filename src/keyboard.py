class ChangeLang:

    def __init__(self) -> None:
        self.__language = "EN"

    @property
    def language(self):
        return self.__language
    
    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(ChangeLang):

    def __init__(self, name: str, price: float | int, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}"



