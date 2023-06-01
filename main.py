from residences import Residence, Apartament, House
from residences.error import IsNotResidenceError


def add_residence():
    r1 = Residence(3, 72.1, "Rua Aquela", 1599.99, "22/10/2021")

    ap1 = Apartament(
        4,
        120,
        "Rua dos Apartamentos",
        2500.01,
        "15/09/2022",
        22,
        500,
        2,
    )

    # print(Apartament.__mro__)
    h1 = House(5, 230, "Rua das Casas", 5400, "17/03/2022", 30)
    print(r1.created_at)
    print(ap1.created_at)
    print(h1.created_at)

    # print(type(r1))
    # print(type(ap1))
    # print(type(h1))

    # print("INSTACIAS")
    # print(isinstance(r1, Residence))
    # print(isinstance(h1, object))
    # print(House.__mro__)

    # print(h1 > 10)
    # try:
    #     print(h1 > 10)
    # except IsNotResidenceError as err:
    #     print(err.message)


def main():
    add_residence()


if __name__ == "__main__":
    main()
