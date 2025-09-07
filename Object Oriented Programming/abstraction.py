from abc import ABC, abstractmethod

class Mobile(ABC):

    @abstractmethod
    def camera(self):
        pass 

    @abstractmethod
    def keypad(self):
        pass 

    @abstractmethod
    def ram(self):
        pass 

    @abstractmethod
    def storage(self):
        pass

class Samsung(Mobile):
    
    def camera(self):
        print("Samsung Camera")

    def keypad(self):
        print("Samsung Keypad")

    def ram(self):
        print("Samsung Ram")

    def storage(self):
        print("Samsung Storage")

s=Samsung()
s.camera()
s.keypad()
s.ram()
s.storage()