"""
Solution to exercise 2
"""
from exercise_1 import Person

class HatPerson(Person):
    """
    A HatPerson is a Child class (or 'subclass') of Person.
    It has all the same behaviour as a Person, except
    HatPerson has a hat.

    This is a simple form of 'inheritance'
    """
    hat = None

    def __init__(self, pos, hat):
        """
        The constructor for HatPerson. We can resuse the
        construct of Person by calling it's __init__ method
        through `super()`.

        pos should be an integer
        hat should be a string of length 3
        """
        self.hat = hat
        super(HatPerson, self).__init__(pos)

    def display(self):
        """
        This method displays first the hat, then
        the rest of the person, by exploiting the Person's
        display method
        """
        lbuff = self.pos - self._LBOUND
        print(lbuff * '   ' + self.hat)
        super(HatPerson, self).display()


class TurnablePerson(Person):
    """
    This form of TurnablePerson inherits from Person.
    Because of that, we can make use of pre-existing code to
    make this implementation simpler.
    """
    def __init__(self, pos, direc):
        self.direc = direc 
        super(TurnablePerson, self).__init__(pos)

    def change_direction(self, new_direc):
        self.direc = new_direc
        self.display()

    def move_forward(self, steps=1):
        if self.direc == 'left':
            self.move_left(steps)
        elif self.direc == 'right':
            self.move_right(steps)
        else:
            print('BAD DIRECTION!')

    def move_backward(self, steps=1):
        if self.direc == 'left':
            self.move_right(steps)
        elif self.direc == 'right':
            self.move_left(steps)
        else:
            print('BAD DIRECTION!')

    def display(self):
        if self.direc == 'left':
            self.torso = '>| '
        else:
            self.torso = ' |<'

        super(TurnablePerson, self).display()

if __name__ == '__main__':
    pos = 5
    print('--- Construcintg a  hatperson at position ' + str(pos))
    hatperson1 = HatPerson(pos=pos, hat='/=\\')
    print('--- Moving hatperson right 1')
    hatperson1.move_right(1)
    print('--- Moving hatperson left 2')
    hatperson1.move_left(2)
    print('--- Moving hatperson right 4')
    hatperson1.move_right(4)

    print('')
    print('')
    pos = 7
    print('--- Construcintg a turnable person at position ' + str(pos))
    mytp1 = TurnablePerson(pos=pos, direc='right')
    print('--- Moving person forward 1')
    mytp1.move_forward(1)
    print('--- Moving person backward 2')
    mytp1.move_backward(2)
    print('--- Turning person around')
    mytp1.change_direction('left')
    print('--- Moving person forward 4')
    mytp1.move_forward(4)
       
