"""
This is the second exercise where we introduce inheritance
Attendees will witness how to write a simple form of inheritance
by giving a Person a Hat.

Attendees will then inspect their TurnablePerson code, and 
adapt it so that it inherits from Person, thereby reusing
some methods and reducing code duplication.
"""
from exercise_1 import Person

class HatPerson(Person):
    """
    A HatPerson is a Child class (or 'subclass') of Person.
    It has all the same behaviour as a Person, except
    HatPerson has a hat.

    This is a simple form of 'inheritance'
    """
    ALLOWED_DIRECS = ['left', 'right']
    hat = None

    def __init__(self, pos, hat):
        """
        The constructor for HatPerson. We can resuse the
        construct of Person by calling it's __init__ method
        through `super()`.

        pos should be an integer
        hat should be a string of length 3
        """
        if len(hat) != 3:
            raise UserWarning('Hat string must be of length 3')
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
    ALLOWED_DIRECS = ['left', 'right']
    direc = None

    def __init__(self, pos, direc):
        if direc not in self.ALLOWED_DIRECS:
            raise UserWarning('direc must be one of {}'.format(
                              self.ALLOWED_DIRECS))
        print('---- WARNING: I AM NOT YET IMPLEMENTED! ----')
        # IMPLEMENT ME

        self.display()

    def change_direction(self, new_direc):
        """
        Update the internal state of the object based on some new input.
        """
        if new_direc not in self.ALLOWED_DIRECS:
            raise UserWarning('direc must be one of {}'.format(
                              self.ALLOWED_DIRECS))
        # IMPLMENT ME!

        self.display()

    def move_forward(self, steps=1):
        """
        Move the person `steps` in the direciton they are facing
        Hint: Person already has move_left and move_right. You can
        use these in this method by:
            self.move_forward(steps=steps)
        """
        # IMPLMENT ME!
        pass


    def move_backward(self, steps=1):
        """
        Move the person `steps` in the opposite direcion they are
        facing.
        """
        # IMPLMENT ME!
        pass


    def display(self):
        """
        Display the person, where their appearnance changes based
        on the direction they are facing.

        Try and use the parent class's display method. Think about
        what needs to change in a TurnablePerson's state.
        """
        # IMPLMENT ME!
        
        # Hint: change something about the person's stored appearance
        # here...

        # Then we can call the Person display method:
        super(TurnablePerson, self).display()

if __name__ == '__main__':
    pos = 5
    print('--- Constructing a  hatperson at position ' + str(pos))
    hatperson1 = HatPerson(pos=pos, hat='(^)')

    # Note how we can use move_right and move_left methods, despite
    # not explicitly defining these methods in the HatPerson class.
    print('--- Moving hatperson right 1')
    hatperson1.move_right(1)
    print('--- Moving hatperson left 2')
    hatperson1.move_left(2)
    print('--- Moving hatperson right 4')
    hatperson1.move_right(4)
    
    pos = 7
    print('--- Constructing a turnable person at position ' + str(pos))
    mytp1 = TurnablePerson(pos=pos, direc='right')
    print('--- Moving person forward 1')
    mytp1.move_forward(1)
    print('--- Moving person backward 2')
    mytp1.move_backward(2)
    print('--- Turning person to face left')
    mytp1.change_direction('left')
    print('--- Moving person forward 4')
    mytp1.move_forward(4)
