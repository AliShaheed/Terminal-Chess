from piece import Piece 
class Player(Piece):
    def __init__(self, colour: str) -> None:
        super().__init__(colour)
