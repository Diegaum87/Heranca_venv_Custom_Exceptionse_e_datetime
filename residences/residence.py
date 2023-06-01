# class Residence(object)
from .error import IsNotResidenceError
from datetime import datetime as dt


class Residence:
    def __init__(
        self, num_rooms: int, area: float, adress: str, price: float, rented_date: str
    ) -> None:
        self.num_rooms = num_rooms
        self.area = area
        self.adress = adress
        self.price = price
        self.rented_date = rented_date
        self.created_at = dt.now()

    def __repr__(self) -> str:
        return f"<Moradia {self.adress} - {self.price}>"

    def __gt__(self, other: "Residence") -> bool:
        # return self.price > other.price
        if not isinstance(other, Residence):
            raise IsNotResidenceError(
                "Não é possível comparar Residence com outro tipo de dado"
            )
        else:
            return self.price > other.price

    def __lt__(self, other: "Residence") -> bool:
        return self.price > other.price


class Apartament(Residence):
    def __init__(
        self,
        num_rooms: int,
        area: float,
        adress: str,
        price: float,
        rented_date: str,
        floor_number: int,
        condominium_fee: float,
        num_elevators: int,
    ) -> None:
        # Super se refere a classe "pai/mãe"
        # super() é o self da classe pai
        super().__init__(num_rooms, area, adress, price, rented_date)
        self.floor_number = floor_number
        self.condominium_fee = condominium_fee
        self.num_elevators = num_elevators

    # Sobreescrita
    def __repr__(self) -> str:
        return f"<Moradia {self.adress} - {self.floor_number} - {self.price}>"


class House(Residence):
    def __init__(
        self,
        num_rooms: int,
        area: float,
        adress: str,
        price: float,
        rented_date: str,
        yard_area: float,
    ) -> None:
        super().__init__(num_rooms, area, adress, price, rented_date)
        self.yard_area = yard_area

    # Sobreescrita
    def __repr__(self) -> str:
        return f"<Moradia {self.adress} - {self.yard_area} - {self.price}>"
