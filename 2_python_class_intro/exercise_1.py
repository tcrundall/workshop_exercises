"""
This is the first exercise.
Attendees will witness how to write the Person class.

Attendees will then write their own TurnablePerson class,
by filling in the empty methods.

Since Person is already written, you can import this Class
into a python environment by opening a terminal in the same
directory and running either
 python
or
 ipython
then
 >> from exercise_1 import Person
You can then start playing around with the Person class:
 >> pers = Person(pos=5)
 >> pers.display()
 >> pers.move_right(3)
 >> pers.move_left(1)

Alternatively you can run the script at the bottom by:
$ python exercise_1.py
Though keep in mind, some code is missing so things might break.
"""

class Person():
    """
    A stick figure person that exists on a 1-D path.
    A person can move back or forward until it reaches
    the boundaries.
    """

    # These are Class variables. They are the same for every
    # instance of this class.
    # By convention, capitalised variables should stay constant
    # Also by convention, variables beginning with a '_' should
    # not be altered from outside the object
    _LBOUND = 1
    _RBOUND = 9

    head  = ' O '
    torso = ' |<'
    legs  = ' ^ '

    pos = None
    
    def __init__(self, pos):
        """
        This is the initialisation method. This is what's called
        when a Person object is created.
        """
        self.pos = pos
        self.display()

    def move_left(self, steps=1):
        """
        This moves the person left by a given number of steps.
        `steps` should be an integer
        """
        if self.pos - steps >= self._LBOUND:
            self.pos -= steps
        self.display()

    def move_right(self, steps=1):
        """
        This moves the person right by a given number of steps.
        `steps` should be an integer
        """
        if self.pos + steps <= self._RBOUND:
            self.pos += steps
        self.display()
    
    def display(self):
        """
        This displays a text based image of the person
        """
        lbuff = self.pos - self._LBOUND
        rbuff = self._RBOUND - self.pos
        # Print the person
        print(lbuff * '   ' + self.head)
        print(lbuff * '   ' + self.torso)
        print(lbuff * ' _ ' + self.legs + rbuff * ' _ ')
        
        # Print some integer labels
        labels = ['{:^3}'.format(i) for i in range(self._LBOUND,
                                                   self._RBOUND+1)]
        print(''.join(labels))                                           


class TurnablePerson():
    ALLOWED_DIRECS = ['left', 'right']
    pos = None
    direc = None
    
    def __init__(self, pos, direc):
        """
        The initialisation method of TurnablePerson. This method is automatically called 
        when a TurnablePerson is created.
        """
        print('---- WARNING: I AM NOT YET IMPLEMENTED! ----')
        if direc not in self.ALLOWED_DIRECS:
            raise UserWarning('direc must be one of {}'.format(self.ALLOWED_DIRECS))

        # IMPLEMENT ME

        self.display()

    def change_direction(self, new_direc):
        """
        Update the internal state of the object based on some new input.
        """
        if new_direc not in self.ALLOWED_DIRECS:
            raise UserWarning('direc must be one of {}'.format(self.ALLOWED_DIRECS))
        # IMPLEMENT ME!

        self.display()

    def move_forward(self, steps=1):
        """
        Move the person `steps` in the direciton they are facing
        Hint: The behaviour of this method will depend on the value in
        self.direc
        """
        # IMPLEMENT ME!

        self.display()

    def move_backward(self, steps=1):
        """
        Move the person `steps` in the direciton they are facing
        Hint: The behaviour of this method will depend on the value in
        self.direc
        """
        # IMPLEMENT ME!

        self.display()

    def display(self):
        """
        Display the person, where their appearance changes based
        on the direction they are facing.

        Try and use the parent class's display method. Think about
        what needs to change in a TurnablePerson's state.
        """
        if self.direc == 'left':
            self.torso = '>| '
        elif self.direc == 'right':
            self.torso = ' |<'
        else:
            print('DIRECTION NOT SET APPROPRIATELY')

        lbuff = self.pos - self._LBOUND
        rbuff = self._RBOUND - self.pos
        print(lbuff * '   ' + self.head)
        print(lbuff * '   ' + self.torso)
        print(lbuff * ' _ ' + self.legs + rbuff * ' _ ')
        labels = ['{:^3}'.format(i) for i in range(self._LBOUND,
                                                   self._RBOUND+1)]
        print(''.join(labels))                                           


# This weird if statement is just a fancy way of making sure the below
# code is only run if this file is executed like a script:
#   $ python exercise_1.py
# By doing this, we can import this file and the code below will not
# run.
if __name__ == '__main__':
    pos = 5
    print('--- Construcintg a  person at position ' + str(pos))
    person1 = Person(pos=pos)
    print('--- Moving person right 1')
    person1.move_right(1)
    print('--- Moving person left 2')
    person1.move_left(2)
    print('--- Moving person right 4')
    person1.move_right(4)

    print('')
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
    
