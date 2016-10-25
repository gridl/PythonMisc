import datetime
from enum import Enum


def main():
    d_text = input("Which direction [n,s,w,e,nw,ne,sw,se]? ")
    m = Moves.parse(d_text)

    if m is None:
        print("That's not a move!")
        return

    print(m)

    direct_moves = {Moves.North, Moves.South, Moves.West, Moves.East}
    if m in direct_moves:
        print("That's a direct move.")
    else:
        print("That's a diagonal move.")

class Moves(Enum):
    West = 1
    North = 2
    East = 3
    South = 4
    NorthEast = 5
    SouthEast = 6
    NorthWest = 7
    SouthWest = 8

    @staticmethod
    def parse(text: str):
        if not text:
            return None

        text = text.strip().lower()
        if text == 'w':
            return Moves.West
        if text == 'e':
            return Moves.East
        if text == 's':
            return Moves.South
        if text == 'n':
            return Moves.North

        if text == 'nw':
            return Moves.NorthWest
        if text == 'sw':
            return Moves.SouthWest
        if text == 'ne':
            return Moves.NorthEast
        if text == 'se':
            return Moves.SouthEast

        return Nonen


if __name__ == '__main__':
    main()