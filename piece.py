from abc import abstractmethod

class Piece:
    def __init(self, x, y):
        self.__x = x
        self.__y = y
        self.__selected = False
    
    def get_pos(self):
        return (self.__x, self.__y)
    
    def set_pos(self, pos):
        self.__x, self.__y = pos

    def is_selected(self):
        return self.__selected
    
    @abstractmethod
    def is_valid_move(self):
        pass